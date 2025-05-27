import java.awt.desktop.SystemEventListener;
import java.time.temporal.IsoFields;
import java.util.Scanner;
public class DetectNum {
    public static void main(String[] args){
        System.out.println("Enter the Number to detect if it is positive or negative");
        Scanner input = new Scanner(System.in);
        int number  = input.nextInt();
        System.out.println("Enter you number: "+ number);
        if(number > 0){
            System.out.print("This is a positive number");
        } else if (number == 0) {
            System.out.println("Number is zero");
        }
        else{
            System.out.print("Negative number");
        }



    }



}
