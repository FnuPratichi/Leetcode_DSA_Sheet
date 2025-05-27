public class Multiplication
{
    public static void main(String[] args)
    {
        table(10);

    }

    public static void table(int number)
    {
        int answer = 1;
        for(int i=1; i<11;i++) {
            answer = number * i;
            System.out.println("multiplication of 10 * " + i + " = " + answer);

        }
    }
}
