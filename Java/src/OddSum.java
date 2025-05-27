public class OddSum {
    public static void main(String[] args){
        OddSum obj = new OddSum();
        int result = obj.OddNum();
        System.out.println("Sum of odd numbers: " + result);
    }

    public int OddNum()
    {
        int total = 0;
        int [] num = {1,2,3,4,5,6,7,8,9,10};
        for(int i =0; i< num.length; i++)
        {
            if(num[i]%2!=0)
            {
                total = total + num[i];
            }
        }
        return total;
    }
}
