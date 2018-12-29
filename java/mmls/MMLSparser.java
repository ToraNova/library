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
import java.util.List;
import java.util.ArrayList;

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

public class MMLSparser{
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

  //private document holder vars
  private Document target_doc;

  //util private vars

  //#############################################################################################
  //## CONSTRUCTORS
  //#############################################################################################

  public MMLSparser(){
    //default constructor
  }

  public MMLSparser(Document input_doc){
    target_doc = input_doc;
  }

  public MMLSparser(String pathdir,String filename){
    File input = new File( pathdir,filename);
    try{
      target_doc = Jsoup.parse(input, "UTF-8", url_mmls_main);
    }catch(Exception e){
      e.printStackTrace();
    }
  }

  //#############################################################################################
  //## INTERFACE METHODS
  //#############################################################################################

  public void testFunc(){
    //String student_id = "1161300548";
    //retrClassDat("1161300548");
    //readClassDat("1161300549");
    retrPOSTElement();
  }

  public void setDoc(Document a_target){
    target_doc = a_target;
  }

  public String parseSignIn(){
    //Author: C.Jason
    //parses the message of sign ins (result)
    Element alertString = target_doc.body().select("div.alert").first();
    if(alertString != null){
      System.out.println("Parsed SignIn Results : "+alertString.text());
    }
    return alertString.text();
  }

  public String parseSignInSilent(){
    //Author: C.Jason
    //parses the message of sign ins (result) DOES NOT PRINT
    Element alertString = target_doc.body().select("div.alert").first();
    return alertString.text();
  }

  public List<MMLScourse> readClassDat(String student_id){
    //Author: C.Jason
    //reads from /data/<student_id> file to obtain the class data
    //returns a list of size 0 upon failure
    List<MMLScourse> courselist = new ArrayList<MMLScourse>();
    File datdir = new File("data/"+student_id);
    File[] listOfFiles = datdir.listFiles();

    try{
      for (int i = 0; i < listOfFiles.length; i++) {
        if (listOfFiles[i].isFile()){
          System.out.println("File " + listOfFiles[i].getName() + " detected");
          courselist.add( MMLScourse.readFile(student_id,listOfFiles[i].getName()));
        }
      }
    }catch(Exception e){
      e.printStackTrace();
    }
    return courselist;
  }

  public List<MMLScourse> retrClassDat(String student_id){
    //Author: C.Jason
    //retrives the relevant class data and stores it on the /data dir
    List<MMLScourse> courselist = retrH3Element();
    for(MMLScourse course : courselist){
      //course.printStatus();
      course.saveFile(student_id); //saves to file
    }
    return courselist;
  }

  //#############################################################################################
  //## PRIVATE METHODS
  //#############################################################################################

  private List<MMLScourse> retrH3Element(){
    //Author: C.Jason
    //based on observation, the titles are all under h3 'panel-title' class
    //returns a MMLScourse list
    List<MMLScourse> out = new ArrayList<MMLScourse>();
    String linkstr,title;
    String tmp_coord_id,tmp_class_id;
    System.out.println("Parsing H3 elements with class Panel-title");
    Elements h3_panelheading_links = target_doc.body().select("h3[class=panel-title]").select("a[href]");
    //Elements h3_classlinks = h3_panelheading.select("a[href]");
    for(Element clink : h3_panelheading_links){
      linkstr = clink.attr("href");
      title = clink.text();
      //System.out.println("ClassTitle --- ClassURL: "+title+"\t"+linkstr);
      tmp_coord_id = linkstr.split("/")[3].split(":")[1];
      tmp_class_id = linkstr.split("/")[3].split(":")[0];
      out.add( new MMLScourse(title, tmp_class_id  , tmp_coord_id ));
    }
    return out;
  }

  private void retrPOSTElement(){
    /*Author: Nabil Nasurdin*/

    List<String> courseTitleList = new ArrayList<String>(); //init titleList
    List<String> postTitleList = new ArrayList<String>();
    List<String> postContent = new ArrayList<String>();
    List<String> postAuthor = new ArrayList<String>();
    List<String> postDate = new ArrayList<String>();

    try{

    //System.out.println(auth_session.get());

      //title of the home page
      System.out.println("--------------------THIS IS THE HOME TITLE----------------------------------");
      String title = target_doc.title();
      System.out.println("\n\t"+title+"\n");


      //classtitle
      System.out.println("--------------------THIS IS THE CLASS TITLE----------------------------------");
      Elements classTitle = target_doc.select("div[class^=panel-heading]");
      for(Element PaneHeading : classTitle){

      }
      System.out.println("\n"+classTitle.text());
      System.out.println("\n\n");

      /** OPTIONAL METHOD TO GET THE title
      Elements c = doc.select(".panel-heading:contains(-)");
      System.out.println("\n"+c.text());
      System.out.println("\n\n");
      **/

      //tab title - announcement/lecture notes/tutorial
      System.out.println("--------------------THIS IS THE TAB TITLE----------------------------------\n\n");
      Elements links = target_doc.select("a[data-toggle=tab]");
      for (Element link : links) {
      System.out.println(link.text()+"\n");
      }

      // title of the announcement
      System.out.println("\n---------title of the announcement -------------");
      Elements a = target_doc.getElementsByTag("font");
      System.out.println("\n\n"+a.text()+"\n\n");

      //	print content
      System.out.println("--------------------THIS IS THE CONTENT----------------------------------\n\n");
      Elements paragraphs = target_doc.getElementsByTag("p");
      for (Element paragraph : paragraphs) {
      System.out.println("\t\t"+paragraph.text());
      }
      System.out.println("\n\n");
      //lecturer and dates
      System.out.println("\n---------lecturer and dates--------");
      Elements i = target_doc.getElementsByTag("i");
      System.out.println(i.text());

    }catch (Exception e){
      e.printStackTrace();
    }
  }




}
