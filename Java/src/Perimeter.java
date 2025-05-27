import java.util.Scanner;
public class Perimeter {
    public static void main (String[] args){
        Scanner input  = new Scanner(System.in);
        System.out.print("Enter Length: ");
        float length = input.nextFloat();
        System.out.print("Enter breadth: ");
        float breadth = input.nextFloat();
        System.out.print("Enter height: ");
        float height = input.nextFloat();

        float perimeter = length * breadth * height;
        System.out.println("Perimeter is:  " + perimeter);


    }

}
