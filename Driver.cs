using System;

using Microsoft.Quantum.Simulation.Core;
using Microsoft.Quantum.Simulation.Simulators;

namespace quantum_programming
{
    class Driver
    {
        static void Main(string[] args)
        {
            using (var qsim = new QuantumSimulator())
            {
                // Run_DeutschJozsa_Algorithm.Run(qsim).Wait();
                var res = Run_BernsteinVazirani_Algorithm.Run(qsim).Result;
                System.Console.WriteLine(res);
            }
        }
    }
}