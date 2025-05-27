public class Reverse {
    public static void main(String[] args) {
        Reverse obj = new Reverse();
        System.out.println(obj.IsReverse(1012));
        System.out.println(obj.IsReverse(1011));
        System.out.println(obj.IsReverse(100));
        System.out.println(obj.IsReverse(10));
    }

    public int IsReverse(int a){
        int reverse = 0;
        while(a > 0){
            int lastDigit = a%10;
            reverse = (reverse * 10) + lastDigit;
            a = a/10;
        }
        return reverse;
    }
}
