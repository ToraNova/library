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
import java.io.BufferedWriter;
import java.io.OutputStreamWriter;
import java.io.FileOutputStream;
import java.io.Writer;
import java.io.IOException;
import java.util.Base64; //provides base64 encode/decode
import java.security.SecureRandom; //provides the SecureRandom() function
import java.security.Security; //to add the bc instance as the security provider
import java.security.Key;
import java.security.KeyPair;
import java.security.KeyPairGenerator;
import java.security.MessageDigest;
import java.security.NoSuchAlgorithmException;

public class BC25519{

	public static void main(String args[]){

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

			System.out.printf("Encoding public key : %s\n",pubkey.getFormat());
			Writer w = new BufferedWriter(new OutputStreamWriter(new FileOutputStream("public"),"utf-8"));
			w.write("-----BEGIN PUBLIC KEY-----\n");
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
			System.out.printf("Truncated keylength now %d from %d\n",truncatedKey.length,originalKey.length);

			System.out.printf("Encoding secret key : %s\n",secret.getFormat());
			w = new BufferedWriter(new OutputStreamWriter(new FileOutputStream("secret"),"utf-8"));
			w.write("-----BEGIN PRIVATE KEY-----\n");
			w.write(Base64.getEncoder().encodeToString( truncatedKey )); //comment this out to use back the originalkey
			//w.write(Base64.getEncoder().encodeToString( originalKey ));
			w.write("\n-----END PRIVATE KEY-----\n");
			w.close();

		}catch(Exception e){
			//exception has occurred
			System.out.println(e);
		}

		System.out.println("OK");
	}
};
