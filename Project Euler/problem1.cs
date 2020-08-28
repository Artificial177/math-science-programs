using System;

namespace Mathematics
{
    public class Program
    {
        public static void Main(string[] args)
        {
            System.Console.WriteLine(findNums(1000));
        }

        public static int findNums(int max_bound) {
            int sum = 0;

            for (int x = 0; x < max_bound; x++)
            {
                if (x % 3 == 0){
                    sum += x;
                }
                else if (x % 5 == 0){
                    sum += x;      
                }  
            }
            return sum;
        }
    }
}
