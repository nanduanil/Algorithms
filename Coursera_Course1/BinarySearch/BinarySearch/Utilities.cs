using System;
using System.Collections.Generic;
using System.Linq;
using System.Text;
using System.Threading.Tasks;

namespace BinarySearch
{
    static class Utilities
    {
        public static T[] SubArray<T>(this T[] data, int startIndex, int endIndex)
        {
            int length = (endIndex - startIndex)+1;
            T[] result = new T[length];
            Array.Copy(data, startIndex, result, 0,  length);
            return result;
        }
    }
}
