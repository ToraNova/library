package mmls;
//A MMLSpost object

public class MMLSpost{

  //concerned fields
  private String ptitle;
  private String content;
  private String author;
  private String date;
  private String link;

  public MMLSpost(){
    //default constructor
    //avoid using this constructor
  }

  //important POST informations :
  /*
  title,author,date
  content
  */
  public MMLSpost(String a_title,String a_content,
                  String a_author,String a_date){
    ptitle = a_title;
    content = a_content;
    author = a_author;
    date = a_date;
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

}
