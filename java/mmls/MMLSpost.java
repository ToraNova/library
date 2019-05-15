package mmls;
//A MMLSpost object

import java.io.Serializable;

public class MMLSpost implements Serializable{

  //concerned fields
  private String ptitle;
  private String content;
  private String author;
  private String date;
  private String course;

  private Boolean notified;

  public MMLSpost(){
    //default constructor
    //avoid using this constructor
  }

  //important POST informations :
  /*
  title,author,date
  content
  */
  public MMLSpost(String a_course,String a_title,String a_content,
                  String a_author,String a_date){
    course = a_course;
    ptitle = a_title;
    content = a_content;
    author = a_author;
    date = a_date;
    notified = false;
  }

  public boolean equals(MMLSpost target){
    //compares if both MMLSpost are the same
    if(this.ptitle.equals(target.ptitle) &&
      this.course.equals(target.course) &&
      this.content.equals(target.content) &&
      this.author.equals(target.author) &&
      this.date.equals(target.date)){
        return true;
    }else{
        return false;
    }
  }

  public void notifyPost(){
    this.notified = true;
  }

  public Boolean isNotified(){
    return notified;
  }

  //getters
  public String getTitle(){
    return ptitle;
  }

  public String getContent(){
    return content;
  }

  public String getAuthor(){
    return author;
  }

  public String getDate(){
    return date;
  }

  public String getCourse(){
    return course;
  }

  public void postprint(){
    System.out.println("Course Title:"+course);
    System.out.println("Post Title:"+ptitle);
    System.out.println("Post Author:"+author);
    System.out.println("Post Date:"+date);
    System.out.println("Content:"+content);
  }


}
