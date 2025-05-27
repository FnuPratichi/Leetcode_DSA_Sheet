public class MatrixArray
{
    public static void main(String[] args)
    {

        int [] myarray = new int [10];
        String [] names = new String[5];

        int [] [] matrix = {{1,2}, {3,4}};

        for(int i=0; i<matrix.length; i++)
        {
            for(int j =0; j< matrix.length;j++){
                System.out.print(" " + matrix[i][j]);
            }
            System.out.println(" ");

        }
    }
}



