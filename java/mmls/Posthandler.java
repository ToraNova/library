package mmls;
//handles arrays of MMLSposts

import java.util.List;
import java.util.ArrayList;

public class Posthandler{

  private List<MMLSpost> postlist; //main lists of posts

  public Posthandler(){
    //default constructor
    postlist = new ArrayList<MMLSpost>();
  }

  public void addPost(MMLSpost a_post){
    postlist.add(a_post);
  }

}
