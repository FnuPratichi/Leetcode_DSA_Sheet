import java.util.Scanner;
public class Prime {
    public static void main(String[] args){
        Prime obj = new Prime();
        obj.IsPrime(2);
        obj.IsPrime(3);
        obj.IsPrime(4);
        obj.IsPrime(5);
        obj.IsPrime(6);
        obj.IsPrime(99);

        }

    public void IsPrime(int a)
    {
        if(a <= 1)
        {
            System.out.println("Number is less than 1 , so not a prime number");
            return;
        }

        for(int i =2; i<=Math.sqrt(a); i++)
        {
            if(a % i ==0)
            {
                System.out.println(a + " not a prime number");
                return;
            }
        }
        System.out.println(a + " a prime number");


    }

    }


