

import mmls.MMLSclient;
import java.io.Console;

public class ClassTester{
  public static Console testconsole = System.console();

  public static void main(String [] args){
    String sid = "1161300548";
    String pw = new String(testconsole.readPassword("Please enter password for %s: ",sid));
    MMLSclient mmls0 = new MMLSclient(sid,pw);
    //String sid = mmls0.getSid();
    mmls0.testFunc();

	}
};
