

import mmls.MMLSclient;
import mmls.MMLSparser;
import mmls.Posthandler;
import java.io.Console;
import java.io.File;

public class ClassTester{
  public static Console testconsole = System.console();

  public static void main(String [] args){

    Posthandler postmaster;

    String sid = "1161300548";

    String pw = new String(testconsole.readPassword("Please enter password for %s: ",sid));
    MMLSclient mmls0 = new MMLSclient(sid,pw);

    //mmls0.saveHTML();
    MMLSparser mmps0 = new MMLSparser(mmls0.getLogin());

    if(checkFilExist("data/"+sid+"/Posthandler.dat")){
      //file exists, load from file
      postmaster = Posthandler.readFile(sid);
    }else{
      //create new postmaster
      postmaster = new Posthandler();
    }
    int newcount = postmaster.getCount();
    postmaster.checkList(mmps0.parsePost());
    postmaster.displayUnNotifiedPost(true);
    postmaster.saveFile(sid);
    System.out.println("Current post amount:"+Integer.toString(postmaster.getCount()));
    System.out.println("New posts :"+Integer.toString(postmaster.getCount()-newcount));
	}

  private static Boolean checkFilExist(String filename){
    File f = new File(filename);
    if(f.exists() && !f.isDirectory()) {
        // do something
        return true;
    }else{
      return false;
    }
  }

  private static Boolean checkDirExist(String filepath){
      //check if previous record of user exist
      File datdir = new File(filepath);
      File[] listOfFiles = datdir.listFiles();
      if(listOfFiles == null){
        return false;
      }
      if(listOfFiles.length > 0){
        return true;
      }else{
        return false;
      }
    }
};
