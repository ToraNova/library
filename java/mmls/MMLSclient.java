package mmls;

//reference :
//https://www.mkyong.com/java/how-to-send-http-request-getpost-in-java/
//dependent on jsoup. please include the .jar under ~/local-lib/java/

import java.io.BufferedReader;
import java.io.DataOutputStream;
import java.io.InputStreamReader;
import java.io.IOException;

import java.net.URLEncoder;
import java.util.HashMap;
import java.util.Map;

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
  private static final String url_host = "mmls.mmu.edu.my";
  private static final String url_mmls_main = "https://mmls.mmu.edu.my/";
  private static final String url_mmls_check = "https://mmls.mmu.edu.my/checklogin";
  private static final String url_mmls_home = "https://mmls.mmu.edu.my/home";
  private static final String url_mmls_attn = "https://mmls.mmu.edu.my/attendance:%s:%s:%s";
  private static final String url_mmls_atlg = "https://mmls/mmu.edu.my/attendancelogin";
  //private static final String url_mmls_check = "http://127.0.0.1:8000";
  private String stud_id;
  private String stud_pw;

  //auth factors server-side
  private String session_cookie; //important
  private String login_token;
  private Connection auth_session;

  public MMLSclient(String a_id,String a_pw){
    stud_id = a_id;
    stud_pw = a_pw;
  }

  public void testFunc(){
    //run testing code here.
    auth_session = login();
    try{
      System.out.println(auth_session.get());
    }
    catch (Exception e){
      e.printStackTrace();
    }
  }

  private Connection signClass(String course_id, String coord_id, String class_id){
    //attempts to sign for a class
    String sign_url =url_mmls_attn.format(course_id,coord_id,class_id);
    Connection initial = Jsoup.connect(sign_url);
    Connection login = Jsoup.connect(sign_url);
  }

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
      login = generateHeaders(login);
      auth = generateHeaders(auth);

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

  private Connection generateHeaders(Connection input){
    //generate the required login headers for the POST form
    input.userAgent("Mozilla/5.0 (X11; Ubuntu; Linux x86_64; rv:63.0) Gecko/20100101 Firefox/63.0");
    input.header("Accept-Encoding","gzip, deflate, br");
    input.header("Accept","text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8");
    input.header("Accept_Language","en-US,en;q=0.5");
    input.referrer(url_mmls_main);
    input.header("Content-Type","application/x-www-form-urlencoded");
    input.cookie("laravel_session",session_cookie);
    input.header("Upgrade-Insecure-Requests","1");
    return input;
  }
}
