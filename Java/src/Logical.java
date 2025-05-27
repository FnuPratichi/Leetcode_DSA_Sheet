import java.util.Scanner;
public class Logical {
    public static void main(String[] args){
        Scanner input = new Scanner(System.in);
        System.out.print("Enter you gender");
        String gender = input.next();
        if(gender.equalsIgnoreCase("Male")|| gender.equalsIgnoreCase("Female")){
            System.out.print("You are allowed");
        } else if (gender.equals("Lesbian") || gender.equals("lesbian") ) {
            System.out.print("Not allowed");
        } else if (gender.equalsIgnoreCase("GB") || gender.equalsIgnoreCase("TQ")) {
            System.out.print("Not allowed");
        }
        else {
            System.out.print("Provide proper gender");
        }
    }
}
