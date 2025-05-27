import java.util.Scanner;
public class SumNumber {
    public static void main(String[] args){
        Scanner input = new Scanner(System.in);
        System.out.print("Provide number1 for sum: ");
        int firstNum = input.nextInt();

        System.out.print("Provide second number for sum: ");
        int secondNum = input.nextInt();

        System.out.println("Total sum is:" + (firstNum + secondNum));
    }

}
