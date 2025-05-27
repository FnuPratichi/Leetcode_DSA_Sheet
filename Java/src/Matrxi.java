public class Matrxi
{
    public static void main(String[] args)
    {
        int [] [] matrix = {{1,2,3},{5,6,7},{8,9,10},{11,12,13}};
        int size = matrix.length;
        for(int i=0; i<size ; i++)
        {
            for(int j=0;j<size-1; j++)
            {
                System.out.print(matrix[i][j] + "  ");
            }
            System.out.println();
        }
    }
}
