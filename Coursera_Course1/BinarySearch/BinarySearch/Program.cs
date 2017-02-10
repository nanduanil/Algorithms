using System;
using System.Collections.Generic;
using System.Linq;
using System.Text;
using System.Threading.Tasks;

namespace BinarySearch
{
    class Program
    {
        static void Main(string[] args)
        {
            int[] searchArray = { 2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37, 41, 43, 47, 53, 59, 61, 67, 71, 73, 79, 83, 89, 97 };
            Console.WriteLine(BinarySearchArray(searchArray,32));
            Console.ReadLine();
            
        }

        static int BinarySearchArray(int[] searchArray, int findValue)
        {
            var index = -1;
            var searchScope = searchArray;
            int count = 1;
            while (searchScope.Length > 0)
            {
                var checkIndex = (int)Math.Floor((double)(searchScope.Length / 2));
                if (searchScope.Length == 1)
                {
                    if (searchScope[checkIndex] == findValue)
                    {
                        index = checkIndex;
                    }
                    break;
                }
                if (searchScope[checkIndex] > findValue)
                {
                    searchScope = searchScope.SubArray(0, checkIndex - 1);
                }
                else if (searchScope[checkIndex] < findValue)
                {
                    searchScope = searchScope.SubArray(checkIndex + 1, searchScope.Length-1);
                }
                else
                {
                    index = checkIndex;
                    break;
                }
                count++;
            }

            Console.WriteLine("Iterations : "+ count);
            return index;
        }
    }
}
