
// https://stackoverflow.com/questions/1359689/how-to-send-http-request-in-java
package MMLSutil;
public class MMLS_get{

	private String student_id;

	//constructor with student ID
	public MMLS_get(String a_id){
		student_id = a_id;
	}

	//public methods
	public String getSid(){
		return student_id;
	}
	public void printSid(){
		System.out.println(student_id);
	}
	public void changeSid(String a_id){
		student_id = a_id;
	}

}
