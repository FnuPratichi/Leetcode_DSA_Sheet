import java.util.Arrays;
public class ArrayClass {
    public static void main(String[] args)
    {
        int [] myarray = new int[10];
        int[] newarray = {1,2,3,4,5,6,7,8,9,10};
        for(int i=0; i<myarray.length; i++)
        {
            System.out.print(myarray[i]);
        }
        System.out.println("");
        System.out.println(Arrays.toString(newarray));

        String[] names = new String[5];
        String[] mynames = {"Anku", "Aman", "Ram", "Abby", "Emu"};
        System.out.println(Arrays.toString(newarray));
        System.out.println(Arrays.toString(mynames));

    }
}
