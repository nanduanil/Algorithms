using System;
using System.Collections.Generic;
using System.Collections;
using System.Linq;
using System.Text;
using System.Threading.Tasks;

namespace HanoiDisks
{
    class Program
    {
        Stack<int> A = new Stack<int>(new int[] { 6, 5, 4, 3, 2, 1 });
        Stack<int> B = new Stack<int>();
        Stack<int> C = new Stack<int>();

        static void Main(string[] args)
        {
            Program prog = new Program();
            prog.Move(prog.A.Count(), ref prog.A, ref prog.B, ref prog.C);
            Console.ReadLine();
        }

        void Move(int countOfMove, ref Stack<int> from, ref Stack<int> to, ref Stack<int> spare)
        {
            if (countOfMove > 1)
            {
                Move(countOfMove - 1, ref from, ref spare, ref to);
                to.Push(from.Pop());
                PrintValues();
                Move(countOfMove - 1, ref spare, ref to, ref from);
            }
            else {
               to.Push(from.Pop());
               PrintValues();
            }
        }

        public void PrintValues()
        {
            Console.WriteLine("A :B : C: ");
            foreach (Object obj in this.A)
                Console.Write("    {0}", obj);
            Console.WriteLine();
            foreach (Object obj in this.B)
                Console.Write("    {0}", obj);
            Console.WriteLine();
            foreach (Object obj in this.C)
                Console.Write("    {0}", obj);
            Console.WriteLine();
            Console.WriteLine("---------------------");
        }
    }
}
