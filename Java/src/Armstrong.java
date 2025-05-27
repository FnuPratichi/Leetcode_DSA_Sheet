public class Armstrong {
    public static void main(String[] args)
    {
        Armstrong obj = new Armstrong();

        obj.IsArmstrong(153);
        obj.IsArmstrong(152);
        obj.IsArmstrong(143);

    }

    public void IsArmstrong(int number)
    {
       int temp = number;
       int count = 0;
       while(temp!=0)
       {
           temp = temp/10;
           count+=1;
       }
        System.out.println("count od digit is: " + count);
        int sum1 = 0;
        temp = number;
        while(temp!=0)
        {
            int remainder = temp %10;
            sum1 = (int) (sum1 + Math.pow(remainder,count));
            temp = temp /10;
        }
        if(sum1 == number){
            System.out.println(number + " is an armstrong number" + "which has sum = " + sum1);
        }
        else {
            System.out.println(number + " is NOT an Armstrong number." + "which has sum = " + sum1);
        }

    }

}
