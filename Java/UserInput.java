import java.util.Scanner;

public class UserInput {
    public static void main(String args[]){
        Scanner scanner = new Scanner(System.in);
        System.out.println("What is your name?");
        String name = scanner.nextLine();
        System.out.println("Hello " + name);
        int age = scanner.nextInt();
        System.out.println("Your age is "+ age + "years old");

        
    }
    
}
