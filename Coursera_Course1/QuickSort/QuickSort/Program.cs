using System;
using System.Collections.Generic;
using System.Linq;
using System.Text;
using System.Threading.Tasks;

namespace QuickSort
{
    class Program
    {
        static void Main(string[] args)
        {
            Random r = new Random(); //add some seed
            int[] array = new int[10]; //100 is just an example
            for (int i = 0; i < array.Length; i++)
                array[i] = r.Next(200);

            Program p = new Program();
            PrintArray(array);
            array = p.QuickSort(array);
            PrintArray(array);
            var input = Console.ReadLine();
        }

        static void PrintArray(int[] printArray)
        {
            Console.WriteLine("------------");
            foreach (Object obj in printArray)
                Console.Write("    {0}", obj);
            Console.WriteLine();
        }

        int[] QuickSort(int[] array)
        {
            int h = -1;
            int l = 0;
            int pivot = array[array.Length - 1];
            for (int i = 0; i < array.Length ; i++)
            {
                if (array[i] > pivot)
                {
                    h++;
                }
                else
                {
                    int temp = array[i];
                    array[i] = array[l];
                    array[l] = temp;
                    l++;
                    h++;
                }
            }
            PrintArray(array);
            int[] ltArray;
            int[] rtArray;
            if (l > 2)
            {
                ltArray = new int[l-1];
                Array.Copy(array, 0, ltArray, 0, l-1);
                ltArray = QuickSort(ltArray);
                ltArray.CopyTo(array, 0);
            }
            if (h > l)
            {
                rtArray = new int[(h + 1) - l];
                Array.Copy(array, l, rtArray, 0, (h + 1) - l);
                rtArray = QuickSort(rtArray);
                rtArray.CopyTo(array, l);
            }
            return array;
        }
    }
}
