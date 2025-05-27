import java.awt.desktop.SystemEventListener;
import java.util.Scanner;

public class Learningif {
    public static void main(String[] args){
        System.out.print("Enter the age: ");
        Scanner inputAge = new Scanner(System.in);
        int age = inputAge.nextInt();
        if(age<10){
            System.out.print("You are not eligible");
        } else if (age > 15 & age<=30 ) {
            System.out.print("YOu are the best fit");
        } else if (age == 15) {
            System.out.print("you are 15 yrs old");

        } else{
            System.out.print("You are very old , older than 30");
        }
    }

}

