package test;

//this is a test program

//import classes
import basic.Basic;

//testing modules
import org.junit.Test;
import static org.junit.Assert.assertEquals;

public class BasicTest{
  @Test
  public void testMulti(){
    Basic base = new Basic(); //create class
    int a = 1;
    int b = 2;

    assertEquals(3,base.add(a,b));
    assertEquals(2,base.mul(a,b));
  }

}
