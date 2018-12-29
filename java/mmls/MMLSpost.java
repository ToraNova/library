
//A MMLSpost object

public class MMLSpost{

  //concerned fields
  private String ctitle;
  private String ptitle;
  private String content;
  private String author;
  private String date;
  private String link;

  public MMLSpost(){
    //default constructor
  }

  public MMLSpost(String a_title,String a_content,
                  String a_author,String a_date,String a_link){
    title = a_title;
    content = a_content;
    author = a_author;
    date = a_date;
    link = a_link;
  }

  //getters
  public String getTitle(){
    return title;
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

  public String getLink(){
    return link;
  }

}
