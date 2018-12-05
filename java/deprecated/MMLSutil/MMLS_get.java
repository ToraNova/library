package MMLSutil;
// https://stackoverflow.com/questions/1359689/how-to-send-http-request-in-java
import java.net.HttpURLConnection;
import java.net.URL;

import java.io.BufferedReader;
import java.io.InputStreamReader;
import java.io.InputStream;
import java.io.IOException;
import java.io.FileWriter;
import java.io.File;
import java.io.DataOutputStream;

import java.util.Base64;

public class MMLS_get{

	//essential
	private String student_id;
	private String student_pw;
	private HttpURLConnection conn;
	private URL conn_url;
	private String conn_cred_encoding;

	//tmp vars
	private InputStream conn_stream;
	private BufferedReader conn_reader;
	private StringBuilder conn_response;
	private DataOutputStream conn_writer;
	private int conn_rcode;

	//constructor with student ID
	public MMLS_get(String a_id,String a_pw){
		student_id = a_id;
		student_pw = a_pw;
		conn_cred_encoding = String.format(
			"_token=pccp72wN1EJJThPs8DYFoSM0CqIYN0DVllXWn3aN&stud_id=%s&stud_pswrd=%s",a_id,a_pw);
	}

	private void establishConn(String targetURL) throws IOException{
		//inhouse method to establish the conn var by a URL
		//this method throws an exception upon failure. please catch it
		try{
			conn_url = new URL(targetURL);
			conn = (HttpURLConnection) conn_url.openConnection();
			conn.setRequestMethod("POST"); //get request
			conn.setRequestProperty("Content-Type","application/x-www-form-urlencoded"); //small payload,non binary
			conn.setRequestProperty("Content-Language","en-US");//language
			conn.setDoOutput(true); //requires this for writing to a conn.
			//POST
			conn_writer = new DataOutputStream(conn.getOutputStream());
			conn_writer.writeBytes(conn_cred_encoding);
			conn_writer.flush();
			conn_writer.close();
			conn_rcode = conn.getResponseCode();
			System.out.format("connection result code : %d",conn_rcode);
			//GET RESPONSE
			conn_stream = conn.getInputStream();
			conn_reader = new BufferedReader(new InputStreamReader(conn_stream)); //the conn_reader can be used to read
		}
		catch (Exception e){
			e.printStackTrace(); //catch Exception
			throw e; //throw the exception
		}

	}

	private String rawRead(String targetURL) throws IOException{
		//reads a URL raw
		try{
			establishConn(targetURL);
			conn_response = new StringBuilder();
			String tmpline;
			while( (tmpline = conn_reader.readLine()) != null){
				conn_response.append(tmpline);
				conn_response.append('\r');
			}
			conn_reader.close(); //close the buffered reader
			return conn_response.toString();
		}
		catch (Exception e){
			e.printStackTrace();
			throw e;
		}
	}

	public void saveRead(String targetURL){

		try{
			File outfile = new File("out.html");
			outfile.createNewFile();
			FileWriter writer = new FileWriter(outfile);
			String tmp_response = rawRead(targetURL);
			writer.write(tmp_response);
			writer.flush();
			writer.close();
		}
		catch (Exception e){
			e.printStackTrace();
		}
	}

	//util methods
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
