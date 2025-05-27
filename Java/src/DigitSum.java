public class DigitSum
{
    public static void main(String[] args)
    {
        int number = 12345;
        int sum = sumOfDigits(number);
        System.out.println("Sum of digits: " + sum);  // Output: 15
    }
    public static int sumOfDigits(int num)
    {
        int sum = 0;
        while (num > 0)
        {
            sum += num % 10;  // get last digit
            num /= 10;        // remove last digit
        }
        return sum;
    }
}
