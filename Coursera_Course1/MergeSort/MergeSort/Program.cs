using System;
using System.Collections.Generic;
using System.Linq;
using System.Text;
using System.Threading.Tasks;

namespace MergeSort
{
    class Program
    {
        static void Main(string[] args)
        {
            int[] sortArray = new int[10]; //100 is just an example
            Random r = new Random(); //add some seed
            for (int i = 0; i < sortArray.Length; i++)
                sortArray[i] = r.Next(200);
            Console.WriteLine("Array to sort :");
            PrintArray(sortArray);
            Console.WriteLine();

            sortArray = MergeSort(sortArray);
            Console.WriteLine("Sorted Array :");
            PrintArray(sortArray);
            Console.ReadLine();
        }

        static int[] MergeSort(int[] sortArray)
        {
                int mid = (int)Math.Floor((decimal)sortArray.Length / 2);
                int[] loArray = new int[mid];
                int[] highArray = new int[sortArray.Length - mid];
                Array.Copy(sortArray, 0, loArray, 0, mid);
                Array.Copy(sortArray, mid, highArray, 0, sortArray.Length - mid);

                if (mid > 1) { MergeSort(loArray); }
                if(sortArray.Length - mid > 1) { MergeSort(highArray); }
                
                //Merge the arrays
                int loPoint = 0;
                int hiPoint = 0;

                for (int currentPoint = 0; currentPoint < sortArray.Length; currentPoint++)
                {
                    if (loPoint > loArray.Length - 1)
                    {
                        sortArray[currentPoint] = highArray[hiPoint];
                        hiPoint++;
                    }
                    else if (hiPoint > highArray.Length - 1)
                    {
                        sortArray[currentPoint] = loArray[loPoint];
                        loPoint++;
                    }
                    else
                    {
                        if (loArray[loPoint] < highArray[hiPoint])
                        {
                            sortArray[currentPoint] = loArray[loPoint];
                            loPoint++;
                        }
                        else
                        {
                            sortArray[currentPoint] = highArray[hiPoint];
                            hiPoint++;
                        }
                    }
                }
            Console.WriteLine("------");
            PrintArray(sortArray);
            return sortArray;
        }

        static void PrintArray(int[] printArray)
        {
            foreach (Object obj in printArray)
                Console.Write("    {0}", obj);
            Console.WriteLine();
        }
    }
}
