/*
 * Please ensure bouncy castle provider is installed
 * http://www.bouncycastle.org/latest_releases.html
 * for arch, one can install it under /usr/share/java
 * and perform softlink to remove the version number
 * from the filename
 *
 * compile:
 * javac -cp "/usr/share/java/bcprov-ext.jar" BC25519.java
 *
 * run (from the directory where BC25519.class is located):
 * java -cp ".:/usr/share/java/bcprov-ext.jar" BC25519
 */

//import org.bouncycastle.crypto.AsymmetricCipherKeyPair; //obtain the generator
//import org.bouncycastle.crypto.generators.Ed25519KeyPairGenerator; //obtain the generator
//import org.bouncycastle.crypto.params.Ed25519KeyGenerationParameters;
import java.math.BigInteger;
import java.io.BufferedWriter;
import java.io.OutputStreamWriter;
import java.io.FileOutputStream;
import java.io.Writer;
import java.io.IOException;
import java.nio.file.Files;
import java.nio.file.Paths;
import java.util.Base64; //provides base64 encode/decode
import java.security.SecureRandom; //provides the SecureRandom() function
import java.security.Security; //to add the bc instance as the security provider
import java.security.Key;
import java.security.PrivateKey;
import java.security.PublicKey;
import java.security.KeyPair;
import java.security.KeyPairGenerator;
import java.security.KeyFactory;
import java.security.MessageDigest;
import java.security.Signature;
import java.security.NoSuchAlgorithmException;
import java.security.InvalidKeyException;
import java.security.spec.InvalidKeySpecException;
import java.security.spec.PKCS8EncodedKeySpec;
import java.security.spec.X509EncodedKeySpec;

public class BC25519{

	/*
	 * Test driver function (Main)
	 */
	public static void main(String args[]){

		if( args.length < 1 ){
			System.out.println("Please specify operation <gen|sign|verify>");
			System.exit(1);
		}

		if( args[0].equals("gen") ){
			//generate public key
			generateKeyPair("public","secret");
		}else if(args[0].equals("sign")){
			//test sign a message
			byte[] s = signMessage( "secret", "Hello World" );

			StringBuilder sb = new StringBuilder();
			for (byte b : s) {
				sb.append(String.format("%02x", b));
			}
			System.out.println(sb.toString());

		}else if(args[0].equals("verify")){

			if( verifyMessage( "public", "signature", "Hello World") == 0){
				//signature verified
				System.out.println("OK");
			}else{
				//signature failed to verify
				System.out.println("FAIL");
			}

		}

		System.exit(0);
	}

	/*
	 * Takes in a message (string) and a signature as well as the public key, and verify if the signature
	 * is valid for the string
	 * 0 - valid
	 * 1 - invalid
	 */
	public static int verifyMessage(String pubkey_filename, String sign_filename, String message){
		Security.addProvider(new org.bouncycastle.jce.provider.BouncyCastleProvider());
		try{
			//Create object from public key string
			String raw = obtainRaw(pubkey_filename,false);
			if( raw == null ){
				return 2; //error
			}
			byte[] encoded = Base64.getDecoder().decode(raw);

			//CREATE PUBLIC KEY
			X509EncodedKeySpec spec = new X509EncodedKeySpec(encoded);
			KeyFactory keyFactory = KeyFactory.getInstance("Ed25519","BC");
			PublicKey pubkey = keyFactory.generatePublic(spec);

			//create verifier (same class as signing)
			MessageDigest md = MessageDigest.getInstance("SHA-512");
			md.update( message.getBytes() ); //update with what we want to digest
			byte[] d = md.digest(); //perform the digest

			//read the signature file
			raw = new String(Files.readAllBytes(Paths.get(sign_filename)));
			raw = raw.replaceAll("\n",""); //remove newlines
			//alternatively, one could always use base64 here!
			byte[] s = new BigInteger(raw,16).toByteArray(); //convert hex to string

			//attempt verification
			Signature sig = Signature.getInstance("Ed25519","BC"); //obtain a signature generator
			sig.initVerify(pubkey); //intiailize signature
			sig.update(d); //update the digest to be signed
			if(sig.verify(s)){
				//or return true here
				return 0;
			}else{
				//return false;
				return 1;
			}

		}catch(Exception e){
			System.out.println(e);
			return 1;
		}
	}

	/*
	 * Takes in a message (string) and signs it with the secret
	 * signature is deterministic, using message digest SHA512
	 */
	public static byte[] signMessage(String secret_filename, String message){
		Security.addProvider(new org.bouncycastle.jce.provider.BouncyCastleProvider());
		try{
			//Create object from unencrypted private key
			//first remove the header lines
			String raw = obtainRaw(secret_filename,true);
			if( raw == null ){
				return null; //error
			}
			byte[] encoded = Base64.getDecoder().decode(raw);

			//CREATE PRIVATE KEY
			PKCS8EncodedKeySpec kspec = new PKCS8EncodedKeySpec(encoded);
			KeyFactory kf = KeyFactory.getInstance("Ed25519","BC");
			PrivateKey secret = kf.generatePrivate(kspec); //obtained the private key from file

			MessageDigest md = MessageDigest.getInstance("SHA-512");
			md.update( message.getBytes() ); //update with what we want to digest
			byte[] d = md.digest(); //perform the digest

			Signature sig = Signature.getInstance("Ed25519","BC"); //obtain a signature generator
			//sig.initSign(secret, new SecureRandom()); //intiailize signature (probabilistic)
			sig.initSign(secret); //intiailize signature
			sig.update(d); //update the digest to be signed
			byte[] out = sig.sign();

			return out;
		}catch( Exception e ){
			System.out.println(e);
			return null;
		}
	}

	/*
	 * Keypair generation function. generate a 256bit Ed25519 keypair and output them to file
	 * set truncate to true if we wanna interface with openSSL
	 */

	public static int generateKeyPair(String pubkey_filename, String secret_filename, boolean truncate){
		Security.addProvider(new org.bouncycastle.jce.provider.BouncyCastleProvider());

		//Create public and private keys
		try{
			KeyPairGenerator generator = KeyPairGenerator.getInstance("Ed25519","BC");

			//initialize SPRNG
			SecureRandom rand = new SecureRandom();
			generator.initialize(256, rand);

			KeyPair pair = generator.generateKeyPair();
			Key pubkey = pair.getPublic();
			Key secret = pair.getPrivate();

			System.out.printf("Encoding public key : %s\n",pubkey.getFormat()); //optional printouts
			Writer w = new BufferedWriter(new OutputStreamWriter(new FileOutputStream(pubkey_filename),"utf-8"));
			w.write("-----BEGIN PUBLIC KEY-----\n"); //PEM format
			w.write(Base64.getEncoder().encodeToString(pubkey.getEncoded()));
			w.write("\n-----END PUBLIC KEY-----\n");
			w.close();

			/*
			 * ToraNova chia_jason96@live.com
			 * There are incompatibilities as there are additional 33bytes written to the private stream
			 * which I don't udnerstand serve what purpose
			 * to change back, edit truncatedKey -> originalKey on the write
			 */
			byte[] originalKey = secret.getEncoded();
			byte[] truncatedKey = new byte[ originalKey.length - 35 ]; //remove the last 33
			truncatedKey[0] = 0x30; //PLEASE DO NOT EDIT THIS!
			truncatedKey[1] = 0x2E; //PLEASE DO NOT EDIT THIS! 2E corresponds to 46 bytes which is the size including asn1 headers
			for(int i = 2;i < truncatedKey.length;i++){
				truncatedKey[i] = originalKey[i];
			}
			System.out.printf("Truncated keylength now %d from %d\n",truncatedKey.length,originalKey.length); //optional printouts

			System.out.printf("Encoding secret key : %s\n",secret.getFormat()); //optional printouts
			w = new BufferedWriter(new OutputStreamWriter(new FileOutputStream(secret_filename),"utf-8"));
			w.write("-----BEGIN PRIVATE KEY-----\n"); //PEM format
			if(truncate){
				w.write(Base64.getEncoder().encodeToString( truncatedKey )); //comment this out to use back the originalkey
			}else{
				w.write(Base64.getEncoder().encodeToString( originalKey ));
			}
			w.write("\n-----END PRIVATE KEY-----\n");
			w.close();

		}catch(Exception e){
			//exception has occurred
			System.out.println(e);
			return 1;
		}
		return 0;
	}

	/*
	 * Overloaded
	 */
	public static int generateKeyPair(String pubkey_filename, String secret_filename){
		return generateKeyPair(pubkey_filename, secret_filename, true);
	}

	/*
	 * Support function to obtain the raw base64 string, removing the header/trailer as well as newline chars
	 * if secret set to true, then the string BEGIN PRIVATE KEY will be searched for instead of BEGIN PUBLIC KEY
	 */
	private static String obtainRaw(String filename, boolean secret){
		try{
			String raw = new String(Files.readAllBytes(Paths.get(filename)));
			//first remove the header lines
			if(secret){
				raw = raw.replaceAll("(-+BEGIN PRIVATE KEY-+\\r?\\n|-+END PRIVATE KEY-+\\r?\\n?)", "");
				//raw = raw.replace("-----BEGIN PRIVATE KEY-----", "");
				//raw = raw.replace("-----END PRIVATE KEY-----", "");
			}else{
				raw = raw.replaceAll("(-+BEGIN PUBLIC KEY-+\\r?\\n|-+END PUBLIC KEY-+\\r?\\n?)", "");
				//raw = raw.replace("-----BEGIN PUBLIC KEY-----", "");
				//raw = raw.replace("-----END PUBLIC KEY-----", "");
			}
			raw = raw.replace("\n", "");
			return raw;

		}catch(Exception e){
			System.out.println(e);
			return null;
		}
	}

};
