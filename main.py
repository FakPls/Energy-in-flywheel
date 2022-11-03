import matplotlib.pyplot as plt
import numpy as np

EnergyArray = []
TimeArray = []
wArray = []
powerArray = []

f = open("Data.txt", "w")

time = 0.0
dt = 0.1
M = 1
R = 0.5
w = 0.0
theta = 0.1
E = 0.0
T = 0.0

I = 1/2 * M * R * R
E = 0

while time < 100:
    temp = w
    E = 1/2 * I * w * w
    EnergyArray.append(E)
    time = time + dt
    TimeArray.append(time)
    w = theta / dt
    dw = w - temp
    a = dw/dt
    T = I*a
    p = w * T
    powerArray.append(p)
    wArray.append(w)
    theta = theta + 0.001
    print('Energy: ' + str(E) + ' Time: ' + str(time) + ' w: ' + str(w) + ' Power: ' + str(p))
    f.write('Energy: ' + str(E) + ' Time: ' + str(time) + ' w: ' + str(w) + ' Power: ' + str(p) + '\n')

plt.plot(TimeArray, EnergyArray, TimeArray, wArray, TimeArray, powerArray)
plt.show()
