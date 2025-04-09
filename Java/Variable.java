public class Variable {
    public static void main(String args[]){
        String name = "Pratichi";
        int a = 10;
        int b = 20;
        float c = 10f;
        float d = 12f;
        boolean flag = true;
        char my_char = 'A';
        System.out.println(name);
        System.out.println(a+b);
        System.out.println(c+d);
        System.out.println(flag);
        System.out.println(my_char);

        int myNum = 15;
        myNum = 20;  
        System.out.println(myNum);   // overwrite the previous value:
        System.out.println("My num is:" + myNum);

        long number = 23344569708L;
        System.out.println("My long number is:" + number);

        double num2 = 3.1456;
        System.out.println("My double number is "+num2);

    }
}
