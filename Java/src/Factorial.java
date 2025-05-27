public class Factorial {
    public static void main(String[] args){
        Factorial obj = new Factorial();  // ✅ create an object
        obj.factorialfinder(5);
        obj.factorialfinder(0);
        obj.factorialfinder(1);

    }
    public int factorialfinder(int a)
    {
        int fact = 1;
        if(a == 0)
        {
            System.out.println("Factorial of 0 is 1");
        }
        else if (a>=1)
        {
            for(int i =1; i<=a; i++)
            {
                fact = fact * i;
            }
            System.out.println("Factorial of " + a + " is " + fact);
        }
        return fact;
    }
}
