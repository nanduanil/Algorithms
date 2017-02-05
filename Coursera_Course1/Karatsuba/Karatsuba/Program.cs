using System;
using System.Collections.Generic;
using System.Linq;
using System.Text;
using System.Threading.Tasks;
using System.Numerics;

namespace Karatsuba
{
    class Program
    {
        static void Main(string[] args)
        {
            var x = "3141592653589793238462643383279502884197169399375105820974944592";
            var y = "2718281828459045235360287471352662497757247093699959574966967627";
            //var x = "1234567";
            //var y = "5678";
            var mul = KaratsubaMult(x, y);
            Console.WriteLine("Multiplication = " + mul);
            Console.WriteLine("Length = " + mul.ToString().Length);
            Console.ReadLine();
        }

        static BigInteger KaratsubaMult(string x, string y)
        {
            BigInteger mul;
            var lenFirst = x.Length;
            var lenSecond = y.Length;
            var largerLength = (lenSecond > lenFirst) ? lenSecond : lenFirst;
            x = x.PadLeft((largerLength), '0');
            y = y.PadLeft((largerLength), '0');

            if (largerLength > 1)
            {
                var partition = (int)Math.Ceiling((double)largerLength / 2);
                var a = x.Substring(0, partition);
                var b = x.Substring(partition);
                var c = y.Substring(0, partition);
                var d = y.Substring(partition);

                Console.WriteLine("a = " + a);
                Console.WriteLine("b = " + b);
                Console.WriteLine("c = " + c);
                Console.WriteLine("d = " + d);

                var aBig = new BigInteger();
                var bBig = new BigInteger();
                var cBig = new BigInteger();
                var dBig = new BigInteger();
                BigInteger.TryParse(a, out aBig);
                BigInteger.TryParse(b, out bBig);
                BigInteger.TryParse(c, out cBig);
                BigInteger.TryParse(d, out dBig);

                var a_Plus_b = aBig + bBig;
                var c_Plus_d = cBig + dBig;

                var acBig = KaratsubaMult(a,c);
                var bdBig = KaratsubaMult(b,d);
                var ad_Plus_bcBig = (KaratsubaMult(a_Plus_b.ToString(), c_Plus_d.ToString()) - (acBig + bdBig));

                var ac = acBig.ToString();
                // var bd = bdBig.ToString();
                var ad_Plus_bc = ad_Plus_bcBig.ToString();

                BigInteger.TryParse(ac.PadRight((ac.Length + 2 * (largerLength - partition)), '0'), out acBig);
                BigInteger.TryParse(ad_Plus_bc.PadRight((ad_Plus_bc.Length + largerLength - partition), '0'), out ad_Plus_bcBig);

                mul = acBig + ad_Plus_bcBig + bdBig;
                    
                    //( ac.ToString()) + ((BigInteger)Math.Pow(10,(largerLength - (long)partition)) * ad_Plus_bc) + bd;

            }
            else
            {
                mul = Convert.ToInt64(x) * Convert.ToInt64(y);
            }
            return mul;
        }
    }
}
