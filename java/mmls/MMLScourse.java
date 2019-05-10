package mmls;

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

public class MMLScourse implements Serializable{

  //class constants
  private static final long serialVersionUID = 1L;
  private static final String invalid_compare = "You are not register to this class.";

  //class to store course details
  private String title;
  private String coord_id;
  private String class_id; //class id is also course id in our case.

  //start stop param
  private int startRange;
  private int ehaltRange;
  private int currentScn;

  private List<QRLinkInstance> results;

  //#############################################################################################
  //## CONSTRUCTORS
  //#############################################################################################

  public MMLScourse(String a_title,String a_class_id,String a_coord_id,int a_start,int a_end){
    //explicit start and end range func
    title = a_title;
    coord_id = a_coord_id;
    class_id = a_class_id;
    startRange = a_start;
    ehaltRange = a_end;
    refreshLinkInstances();
  }

  public MMLScourse(String a_title,String a_class_id,String a_coord_id){
    //default funcs
    this(a_title,a_class_id,a_coord_id,1,99999);
  }

  //#############################################################################################
  //## INTERFACE METHODS
  //#############################################################################################

  public void showLinksInstances(){
    for(QRLinkInstance q : results){
      System.out.println(q.getString());
    }
  }

  public void writeLinksInstances(){
    BufferedWriter bw = null;
    try{
      File fout = new File("csv",class_id+".csv");
  	  FileOutputStream fos = new FileOutputStream(fout);
      bw = new BufferedWriter(new OutputStreamWriter(fos));
      bw.write(" , ,QR LinkInstance data csv\n");
      bw.write("Course:,"+" ,"+getTitle()+'\n');
      bw.write("CourseID:,"+" ,"+class_id+'\n');
      bw.write("CoordID:,"+" ,"+coord_id+'\n');
      bw.newLine();
      bw.write("TTID,Validity,Result status\n");
    	for (QRLinkInstance q : results) {
    		bw.write(q.getString());
    		bw.newLine();
    	}
    }catch(Exception e){
      e.printStackTrace();
    }finally{
      if(bw != null){
        try{
          bw.close();
        }catch(Exception e){
          e.printStackTrace();
        }
      }
    }
  }

  public int getCurrentTarget(){
    return currentScn;
  }

  public void addLinkInstance(String result){
    //adds the result to the currentLinkInstance
    Boolean validity = false;
    if(new String(result).equals(invalid_compare)){
      validity=false;
    }else{
      validity=true;
    }
    QRLinkInstance nli = new QRLinkInstance(currentScn,validity,result);
    results.add(nli);
    incTarget();
  }

  public void setRange(int a_start,int a_end){
    //sets the starting range and ending range
    currentScn = a_start;
    startRange = a_start;
    ehaltRange = a_end;
  }

  public void setTarget(int a_target){
    //edits the current target
    currentScn = a_target;
  }

  public Boolean doneScan(){
    if(currentScn < ehaltRange+1){
      return false;
    }else{
      return true;
    }
  }

  public String generateAttendanceURL(int a_target){
    String aurl = ("https://mmls.mmu.edu.my/attendance:"+
      class_id+':'+
      coord_id+':'+
      Integer.toString(a_target)
    );
    return aurl;
    //return url_mmls_attn.format(class_id,coord_id,a_target);
  }

  public String getTitle(){
    return title;
  }

  public void printStatus(){
    //prints the status of the course
    System.out.format("MMLScourse [%s] status:  start=%d , end=%d\n",title,startRange,ehaltRange);
    System.out.format("Course properties: course_id=%s , class_id=%s\n",class_id,coord_id);
    System.out.format("Current Scan %d\n",currentScn);
  }

  @Override
  public String toString(){
    return new StringBuffer("class_id: ")
				.append(class_id).append(", coord_id: ")
				.append(coord_id).toString();
  }

  public void refreshLinkInstances(){
    results = new ArrayList<QRLinkInstance>();
    currentScn = startRange;
  }

  private void incTarget(){
    //increments the current target
    currentScn += 1;
  }

  public void saveFile(String student_id){
    //saves the file under the directory student_id
    //the actual file id is the course_id (class_id)
    String filepath = "data/"+student_id;
    FileOutputStream fout = null;
    ObjectOutputStream writer = null;
    try{
      new File(filepath).mkdirs(); //ensure the directory is created
      fout = new FileOutputStream(filepath+'/'+class_id);
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

  public static MMLScourse readFile(String student_id,String a_class_id){
    //construct the objects from a file
    String filepath = "data/"+student_id;
    FileInputStream fin = null;
    ObjectInputStream reader = null;
    MMLScourse out = null;
    try{
      fin = new FileInputStream(filepath+'/'+a_class_id);
      reader = new ObjectInputStream(fin);
      out = (MMLScourse) reader.readObject();
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
