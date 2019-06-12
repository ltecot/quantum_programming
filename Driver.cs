using System;

using Microsoft.Quantum.Simulation.Core;
using Microsoft.Quantum.Simulation.Simulators;

namespace bv_algorithm
{
    class Driver
    {
        static void Main(string[] args)
        {
            using (var qsim = new QuantumSimulator())
            {
                var watch = System.Diagnostics.Stopwatch.StartNew();

                // Run_DeutschJozsa_Algorithm.Run(qsim).Wait();


                int n = 10;
                long[] a = new long[n];
                Random r = new Random();
                for(int i = 0; i < n; i++) {
                    a[i] = r.Next(0, 2);
                }
                var res = Run_BernsteinVazirani_Algorithm.Run(qsim, new QArray<long>(a)).Result;
                if(res.Equals("Success!")) {
                    for(int i = 0; i < n; i++) {
                        System.Console.Write(a[i] + " ");
                    }
                    System.Console.WriteLine();
                } else {
                    System.Console.WriteLine("incorrect");
                }

                watch.Stop();
                double totalTime = watch.ElapsedMilliseconds / 1000.0;
                System.Console.WriteLine("Time elapsed: " + totalTime);
            }
        }
    }
}