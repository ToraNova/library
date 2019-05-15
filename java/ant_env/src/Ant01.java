package anttest;

//this is the main program

//import classes
import basic.Basic;

public class Ant01{
  public static void main(String args[]){
    Basic base = new Basic(); //create class
    int a = 1;
    int b = 2;

    int res1 = base.add(a,b);
    int res2 = base.mul(a,b);
    System.out.println("Add is:"+ base.add(a,b));
    System.out.println("Mul is:"+ base.mul(a,b));
  }

}
