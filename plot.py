# Rough util to plot data

import matplotlib
import matplotlib.pyplot as plt
import numpy as np

simon_x = [1, 2, 3, 4, 5, 6]
simon_data = [  0.0000007152557373046,
                0.0047228336334228516,
                0.010866880416870117,
                0.03987264633178711,
                0.4229238033294678,
                24.408594131469727]
grover_x = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11]
grover_data = [ 0.004805326461791992,
                0.004302024841308594,
                0.007644176483154297,
                0.01414179801940918,
                0.029474973678588867,
                0.045203208923339844,
                0.09999322891235352,
                0.29058408737182617,
                1.608902931213379,
                12.953195095062256,
                94.55311107635498]


# Data for plotting
fig, ax = plt.subplots()
# ax.plot(simon_x, simon_data)
ax.plot(grover_x, grover_data)

ax.set(xlabel='Number of Qubits (n)', ylabel='Time (seconds)',
    #    title='Simons Algorithm')
       title='Grovers Algorithm')
# ax.grid()

# fig.savefig("simon.png")
fig.savefig("grover.png")
plt.show()