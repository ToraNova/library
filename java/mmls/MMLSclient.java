package mmls;

//reference :
//https://www.mkyong.com/java/how-to-send-http-request-getpost-in-java/
//dependent on jsoup. please include the .jar under ~/local-lib/java/

import java.io.BufferedReader;
import java.io.DataOutputStream;
import java.io.InputStreamReader;
import java.io.IOException;
import java.io.File;

import java.text.DateFormat;
import java.text.SimpleDateFormat;

import java.util.HashMap;
import java.util.Map;
import java.util.Date;
import java.util.Calendar;

import org.apache.commons.io.FileUtils;

/*
/ Jsoup parsing library
/ https://www.mkyong.com/java/jsoup-html-parser-hello-world-examples/
*/
import org.jsoup.Jsoup;
import org.jsoup.Connection;
import org.jsoup.Connection.Response;
import org.jsoup.Connection.Request;
import org.jsoup.nodes.Document;
import org.jsoup.nodes.Element;
import org.jsoup.select.Elements;
import org.jsoup.Connection.Method;

public class MMLSclient{

  //url constants
  private static final String url_host = "mmls.mmu.edu.my";
  private static final String url_mmls_main = "https://mmls.mmu.edu.my/";
  private static final String url_mmls_check = "https://mmls.mmu.edu.my/checklogin";
  private static final String url_mmls_home = "https://mmls.mmu.edu.my/home";
  private static final String url_mmls_attn = "https://mmls.mmu.edu.my/attendance:%s:%s:%d";
  private static final String url_mmls_atlg = "https://mmls.mmu.edu.my/attendancelogin";
  //private static final String url_mmls_check = "http://127.0.0.1:8000"; //TEST URL
  //private static final String url_mmls_atlg = "http://127.0.0.1:8000"; //TEST URL
  private String stud_id;
  private String stud_pw;

  //auth factors server-side
  private String session_cookie; //important
  private String login_token;
  private Connection auth_session;

  //util private vars
  private static final String htmlDir = "html";
  private static final String dateStrForm = "yyyy/MM/dd HH:mm:ss";
  private static final String filedateStrForm = "_ddMMyy[HHmmss]";
  private static final String attendanceSINtime = "HH:mm:00";
  private static final String attendanceSINdate = "yyyy-MM-dd";
  private static DateFormat dateFormat;
  private static DateFormat fileDateFormat;
  private static DateFormat attendanceSINTformat;
  private static DateFormat attendanceSINDformat;

  //#############################################################################################
  //## CONSTRUCTORS
  //#############################################################################################

  public MMLSclient(String a_id,String a_pw){
    stud_id = a_id;
    stud_pw = a_pw;
    dateFormat = new SimpleDateFormat(dateStrForm); //init date format
    fileDateFormat = new SimpleDateFormat(filedateStrForm);
    attendanceSINTformat = new SimpleDateFormat(attendanceSINtime);
    attendanceSINDformat = new SimpleDateFormat(attendanceSINdate);
  }

  //#############################################################################################
  //## INTERFACE METHODS
  //#############################################################################################

  public void testFunc(){

  }

  public Document getLogin(){
    Date tmpdate = retrDate(); //prints current time and date
    //obtains the login returned doc and returns it as a Document
    auth_session = login();
    try{
      return auth_session.get(); //return the obtained document
    }
    catch (Exception e){
      e.printStackTrace();
      return null; //indicate fails
    }
  }

  public void saveHTML(){
    Date tmpdate = retrDate(); //prints current time and date
    //obtains the login returned doc and write it to a file
    auth_session = login();
    try{
      //writing to file
      String filename = stud_id+fileDateFormat.format(tmpdate)+".html";
      File f = new File(htmlDir,filename);
      FileUtils.writeStringToFile(f, auth_session.get().outerHtml(), "UTF-8");
      System.out.println("Written result to "+htmlDir+'/'+filename);
    }
    catch (Exception e){
      e.printStackTrace();
    }
  }

  public Document signClass(MMLScourse targetCourse,int a_target){
    //attempts to sign for a class
    Calendar cal = Calendar.getInstance(); // creates calendar
    cal.setTime(new Date()); //sets current time
    String sdate = attendanceSINDformat.format(cal.getTime());
    cal.add(Calendar.MINUTE, -5); //set starttime 2 hours before currentTime
    String stime = attendanceSINTformat.format(cal.getTime());
    cal.add(Calendar.MINUTE, 10); //set endtime 2 hours after currentTime
    String etime = attendanceSINTformat.format(cal.getTime());

    String sign_url = targetCourse.generateAttendanceURL(a_target);
    System.out.format("Attempting to REGISTER for %s with url %s\n",targetCourse.getTitle(),sign_url);
    Connection initial = Jsoup.connect(sign_url);
    Connection login = Jsoup.connect(url_mmls_atlg);
    login.followRedirects(true); //set this to true to auto follow
    String formClassID;
    try{
      initial.execute();
      Response initial_response = initial.response();
      //check on the presence of the cookie for laravel session
      //the cookie expires in 2hours.
      if(initial_response.hasCookie("laravel_session")){
        session_cookie = initial_response.cookie("laravel_session");
      }else{
        session_cookie = "invalid";
      }
      //obtain the login token
      Document ir_doc = initial_response.parse();
      login_token = getToken(ir_doc);
      formClassID = getFormClassID(ir_doc);
      //POST form building
      login.data("_token",login_token);
      login.data("stud_id",stud_id);
      login.data("stud_pswrd",stud_pw);
      login.data("timetable_id", Integer.toString(a_target) );
      login.data("starttime",stime);
      login.data("endtime",etime);
      login.data("class_date",sdate);
      login.data("class_id",formClassID);
      //Map<String,String> login_form_headers = generateHeaders(msgLen);
      //login.headers(login_form_headers);
      login = generateHeaders(login,sign_url);
      //auth = generateHeaders(auth);
      Document login_response = login.post(); //execute the POST

      //debugging prints
      System.out.format("Laravel Session cookie: %s\nLogin token: %s\n",session_cookie,login_token);
      System.out.format("Using edited time s= %s , e= %s , date = %s\n",stime,etime,sdate);
      return login_response;
    }
    catch (Exception e){
      e.printStackTrace();
      return null;
    }
  }

  //#############################################################################################
  //## PRIVATE METHODS
  //#############################################################################################

  private Connection login(){
    //attempts to login onto the MMLS system.
    Connection initial = Jsoup.connect(url_mmls_main);
    Connection login = Jsoup.connect(url_mmls_check);
    Connection auth = Jsoup.connect(url_mmls_home);
    login.followRedirects(false); //set this to true to auto follow

    try{
      initial.execute();
      Response initial_response = initial.response();
      //check on the presence of the cookie for laravel session
      //the cookie expires in 2hours.
      if(initial_response.hasCookie("laravel_session")){
        session_cookie = initial_response.cookie("laravel_session");
      }else{
        session_cookie = "invalid";
      }
      //obtain the login token
      login_token = getToken(initial_response.parse());

      //POST form building
      login.data("_token",login_token);
      login.data("stud_id",stud_id);
      login.data("stud_pswrd",stud_pw);

      //Map<String,String> login_form_headers = generateHeaders(msgLen);
      //login.headers(login_form_headers);
      login = generateHeaders(login,url_mmls_main);
      auth = generateHeaders(auth,url_mmls_main);

      Document login_response = login.post(); //execute the POST

      //debugging prints
      System.out.format("Laravel Session cookie: %s\nLogin token: %s\n",session_cookie,login_token);
      System.out.format("Attempting to login onto mmls with sid %s\n",stud_id);
      System.out.format("Response title from mmls login : %s\n", login_response.title());

      return auth;
    }
    catch (Exception e){
      e.printStackTrace();
      return null;
    }
  }

  private String getToken(Document response){
    try{
      //obtains the invisible form token
      Element token_input = response.getElementsByAttributeValue("name","_token").last(); //obtain the token element
      return token_input.attr("value");
    }
    catch (Exception e){
      e.printStackTrace();
      return null;
    }
  }

  private String getFormClassID(Document response){
    try{
      //obtains the invisible form token
      Element form_input = response.getElementsByAttributeValue("name","class_id").last(); //obtain the token element
      return form_input.attr("value");
    }
    catch (Exception e){
      e.printStackTrace();
      return null;
    }
  }

  private Connection generateHeaders(Connection input,String referral_link){
    //generate the required login headers for the POST form
    input.userAgent("Mozilla/5.0 (X11; Ubuntu; Linux x86_64; rv:63.0) Gecko/20100101 Firefox/63.0");
    input.header("Accept-Encoding","gzip, deflate, br");
    input.header("Accept","text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8");
    input.header("Accept_Language","en-US,en;q=0.5");
    input.referrer(referral_link);
    input.header("Content-Type","application/x-www-form-urlencoded");
    input.cookie("laravel_session",session_cookie);
    input.header("Upgrade-Insecure-Requests","1");
    return input;
  }

  private Date retrDate(){
    //prints current time and date
    Date date = new Date();
    System.out.println("Client time :"+dateFormat.format(date));
    return date;
  }
}
