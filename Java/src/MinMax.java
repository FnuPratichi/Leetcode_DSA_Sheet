public class MinMax
{
    public static void main(String[] args)
    {
        int[] marks = {15,100,9,30,50};
        int size = marks.length;
        int max = marks[0];
        int min = marks[0];
        for(int i=1; i<size; i++)
        {
            if(marks[i] > max){
                max = marks[i];
            }
            if(marks[i] < min){
                min = marks[i];
            }
        }
        System.out.println(max);
        System.out.print(min);
    }
}
