public class Palindrome
{
    public static void main(String[] args)
    {
        Palindrome obj = new Palindrome();
        obj.isPalindrome(121);
        obj.isPalindrome(12);
        obj.isPalindrome(111);

    }
    public void isPalindrome(int number) {
        // find reverse digit
        int temp;
        temp = number;
        int reverse = 0;
        while (temp != 0) {
            int remainder = temp % 10;
            reverse = (reverse * 10) + remainder;
            temp = temp / 10;
        }
        if(reverse == number){
            System.out.println("This is Palindrome since Original number is: " + number + " equal to reverse number: " + reverse);
        }
        else{
            System.out.println("This is not Palindrome since Original number is: " + number + " equal to reverse number: " + reverse);

        }

    }
}
