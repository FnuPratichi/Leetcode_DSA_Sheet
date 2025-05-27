public class TypeConversion {
    public static void main (String[] args){
        float number = 6;
        System.out.println(number);

        double myNum = 8.0d; //we are converting from double to int
        int newNum = (int) myNum;
        System.out.println(newNum);


        /* Calculate the percentage of the user's score in relation to the maximum available score.
Convert userScore to float to make sure that the division is accurate */
        int maxScore = 500;
        int yourScore = 450;
        float yourPercent = ((float)yourScore / maxScore) * 100f ;
        System.out.println(yourPercent);




    }
}
