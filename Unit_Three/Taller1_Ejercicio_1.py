# Ejercicio 1: Organizar de forma aleatoria el arreglo.
import numpy as np
import matplotlib.pyplot as plt

temperatures1 = np.linspace(13.6, 18.2, 20)
time_points = range(1, 21)

plt.plot(time_points, temperatures1, )
plt.title('sample xd')
plt.ylabel('temp')
plt.xlabel('time')
plt.show()

#excercise randomize the graph with the temperatures.

ri = np.random.rand(20) #Ri generated with numpy numbers between 0 and 1
min = 13
max = 25
temperatures = min+(max-min)*ri #random temperatures with max min distribution.
print(temperatures)
time_points = range(1, 21)
print(len(time_points))

plt.plot(time_points, temperatures, )
plt.title('sample xd')
plt.ylabel('temp')
plt.xlabel('time')
plt.show()