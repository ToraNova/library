package mmls;

import java.util.List;

import java.io.Serializable;

public class QRLinkInstance implements Serializable{
  private int instanceNum;
  private Boolean validInstance;
  private String resultString;
  public QRLinkInstance(int a_in,Boolean a_valid,String a_result){
    instanceNum = a_in;
    validInstance = a_valid;
    resultString = a_result;
  }

  public String getString(){
    String vIStr = validInstance?"True":"False";
    String outstr = Integer.toString(instanceNum)+','+vIStr+','+resultString;
    return outstr;
  }
}
