import java.util.Scanner;
public class Oddeven
{
    public static void main(String[] args)
    {
        System.out.println("Enter the number to check if it is odd or even");
        Scanner input = new Scanner(System.in);
        int number = input.nextInt();
        if(number%2 == 0) {
            System.out.printf("Number is even");
        }
        else{
            System.out.println("Entered number is Odd Number");
        }
    }
}
