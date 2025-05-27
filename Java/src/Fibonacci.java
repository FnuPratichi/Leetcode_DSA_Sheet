import java.util.Arrays;

public class Fibonacci
{
    public static void main(String[] args)
    {
        Fibonacci obj = new Fibonacci();
        obj.IsFib(5);
    }

    public void IsFib(int number)
    {
        if(number < 0) return;
        if(number ==0) return;
        int first = 0 , second = 1;

        for(int i =0; i<=number; i++)
        {
            System.out.print(first + " ");
            int third = first+second;
            first = second;
            second = third;


        }
    }
}
