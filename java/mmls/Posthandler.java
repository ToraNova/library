package mmls;
//handles arrays of MMLSposts

import java.util.List;
import java.util.ArrayList;

import java.io.File;
import java.io.Serializable;
import java.io.FileInputStream;
import java.io.FileOutputStream;
import java.io.ObjectInputStream;
import java.io.ObjectOutputStream;
import java.io.IOException;
import java.io.BufferedWriter;
import java.io.OutputStreamWriter;

public class Posthandler  implements Serializable{

  private List<MMLSpost> postlist;

  public Posthandler(){
    //default constructor
    postlist = new ArrayList<MMLSpost>();
  }

  private Boolean isInList(MMLSpost target, List<MMLSpost> list){
    //check if target is in list
    for(MMLSpost p : list){
      //for each post in list, check if it equals target
      if(target.equals(p)){
        //if true, means they are equal.
        return true;
      }
    }
    return false;//not in
  }

  public void addPost(MMLSpost target){
    postlist.add(target);
  }

  public List<MMLSpost> checkList(List<MMLSpost> newlist){
    //check the handler with a newlist. if there are new post,
    //add the post onto the newlist.
    //returns a list of new posts (usually only one new post)
    List<MMLSpost> newpostlist = new ArrayList<MMLSpost>();
    for(MMLSpost p : newlist){
      if( isInList(p,this.postlist)){
        //do nothing
      }else{
        //add it into list
        postlist.add(p);
        newpostlist.add(p);
      }
    }
    return newpostlist;
  }

  public List<MMLSpost> getPostList(){
    return postlist;
  }

  public MMLSpost getPost(int index){
    return postlist.get(index);
  }

  public void notifyPost(int index){
    postlist.get(index).notifyPost();
  }

  public List<Integer> getPostList(Boolean isNotified){
    //get the postlist, filter by notified or not
    List<Integer> out = new ArrayList<>();

    for(int i=0;i<this.postlist.size();i++){
      if(postlist.get(i).isNotified() == isNotified){
        postlist.get(i).postprint();
        out.add(i);
      }
    }
    return out;
  }

/*
  public List<MMLSpost> getPostList(Boolean isNotified){
    //get the postlist, filter by notified or not
    List<MMLSpost> out = new ArrayList<MMLSpost>();

    for(MMLSpost p : this.postlist){
      if(p.isNotified() ^ isNotified){
        p.postprint();
        out.add(p);
      }
    }
    return out;
  }
*/

  public int getCount(){
    return postlist.size();
  }

  //USED ON COMPUTER ONLY. DISPLAYING METHODS-----------------------------------------
  public void displayPost(int index){
    postlist.get(index).postprint();
  }
  public void displayAllPost(){
    for(MMLSpost p : this.postlist){
      p.postprint();
      System.out.println();
    }
  }

  public void displayUnNotifiedPost(Boolean setNotify){
    for(MMLSpost p : this.postlist){
      if(!p.isNotified()){
        p.postprint();
        if(setNotify){
          p.notifyPost();
        }
        System.out.println();
      }
    }
  }


  public void saveFile(String student_id){
    //saves the file under the directory student_id
    //the actual file id is the course_id (class_id)
    String filepath = "data/"+student_id;
    FileOutputStream fout = null;
    ObjectOutputStream writer = null;
    try{
      new File(filepath).mkdirs(); //ensure the directory is created
      fout = new FileOutputStream(filepath+'/'+"Posthandler.dat");
      writer = new ObjectOutputStream(fout);
      writer.writeObject(this);
    }catch(Exception e){
      e.printStackTrace();
    }finally{
      if (fout != null) {
				try {
					fout.close();
				} catch (IOException e) {
					e.printStackTrace();
				}
			}

			if (writer != null) {
				try {
					writer.close();
				} catch (IOException e) {
					e.printStackTrace();
				}
			}
    }
  }

  public static Posthandler readFile(String student_id){
    //construct the objects from a file
    String filepath = "data/"+student_id+"/Posthandler.dat";
    FileInputStream fin = null;
    ObjectInputStream reader = null;
    Posthandler out = null;
    try{
      fin = new FileInputStream(filepath);
      reader = new ObjectInputStream(fin);
      out = (Posthandler) reader.readObject();
    }catch(Exception e){
      e.printStackTrace();
    }finally{
      if (fin != null) {
        try {
          fin.close();
        } catch (IOException e) {
          e.printStackTrace();
        }
      }

      if (reader != null) {
        try {
          reader.close();
        } catch (IOException e) {
          e.printStackTrace();
        }
      }
      return out;
    }
  }

}
