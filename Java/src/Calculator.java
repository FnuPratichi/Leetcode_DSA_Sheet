import java.util.Scanner;
public class Calculator {
    public static void main(String[] args){
        Scanner input = new Scanner(System.in);
        double num1 = input.nextDouble();
        double num2 = input.nextDouble();
        System.out.println("Sum is " + (num1 + num2));
        System.out.println("Difference is " + (num2 - num1));
        System.out.println("Multiplication is " + num1 * num2);
        System.out.println("Division is " + num1 / num2);
        System.out.println("Mod is " + num1 % num2);


        float a = 10f;
        float b = 20f;
        System.out.println("Multilpication is: " + ((int)a*b));




    }




}
