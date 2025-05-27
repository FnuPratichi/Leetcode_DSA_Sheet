public class Occurances {
    public static void main(String[] args) {
        int [] number = {1,2,3,3,2};
        int original = 3;
        int size = number.length;
        int count = 0;
        for(int  i=0; i< size; i++){
            if(original == number[i]){
                count+=1;
            }
        }
        System.out.print(count);
    }
}
