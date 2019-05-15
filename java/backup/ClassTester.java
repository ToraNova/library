

import mmls.MMLSclient;
import mmls.MMLSparser;
import java.io.Console;

public class ClassTester{
  public static Console testconsole = System.console();

  public static void main(String [] args){
    String sid = "1161300548";
    String pw = new String(testconsole.readPassword("Please enter password for %s: ",sid));
    MMLSclient mmls0 = new MMLSclient(sid,pw);
    MMLSparser mmps0 = new MMLSparser();

    mmps0.setDoc(mmls0.getLogin());
    mmps0.testFunc();

	}
};
