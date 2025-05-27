public class ArraySum {
    public static void main(String[] args) {
        int [] myarray = {10,20,20};
        int size = myarray.length;
        int totalsum = 0;
        int avgsum = 0;
        for(int i =0; i<size ; i++){
            totalsum = totalsum + myarray[i];
        }
        avgsum = (totalsum) / size;
        System.out.println(totalsum);
        System.out.println(avgsum);

    }
}
