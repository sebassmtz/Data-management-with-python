import numpy as np

#get into elements of an array

a = np.array([[1, 2, 3], [4, 5, 6]])
print(a[1, 0])
print('----')
print(a[1][0])
print('----')
print(a[1:,0])
print('----')
print(a[:, 0:2])

#filter with a[condition] you get an array with the elements from (a) that matches the condition

print(a[(a%2 ==0) & (a > 2)])

#numpy arange:
#return evenly spaced values withina given interval
#numpy.arange(start, stop, step, dtype=None, *, like=None)
 
print(np.arange(-20, 1, 0.5, dtype=float))#starts at -20 ends at 1 without
#generating the 1 and spacing values by 0.5 and with Data type float.

#numpy linspace
#creates and return a reference to an array where its elements are the sequence of n equidistants values.
#from start to finish.
#equidistant: values equaly distant from each other. (google it)
print(np.linspace(start=0, stop=5, num=5))

temperatures = np.linspace(13.6, 18.2, 20) #temperatures lineal Y axis with numbers between 13.6 and 18.2.
print(temperatures)


#array initialization

zeros = np.zeros(50) #array filled with 0.0 type float64
print(zeros.dtype)
print(zeros)

print('----')
ones = np.ones((4, 3)) #matrizxs filled with 1.0 type float64
print(ones.dtype)
print(ones)

print('----')

identity = np.identity(4) #matrizxs filled with 0.0 and pricipal diagonal with 1.0 type float64
print(identity.dtype)
print(identity)

print('----')

eye = np.eye(4, k=1) #matrizxs filled with 0.0 and a diagonal 
print(eye.dtype)
print(eye)


a = np.array([1, 2, 3, 4, 5]) #create numpy array
#print(a)

#print(a.shape) #prints a tuple with the dimensions of the array

#print(a.ndim) #prints the number of dimensions

#print(a.size) #prints the number of elements

#you can do math operations with numpy arrays 
x = np.array([[1, 2, 3],[ 1, 1, 1]], dtype=np.int32)
y = np.array([[1, 0, 5], [6, 8, 1]])

#print(x)
#print(y)
#print('-----------')
#print(x + y)
#print('-----------')
#print(x*y)
#print('-----------')
#print(x**y)

#you can cast an array like so

z = x.astype(np.float64) #x as float
#print(z)

c = np.array([1.1, 2.3, 4.4, -3.1, -4.9, -0.6])
#print(c)

#cast c to int

cint = c.astype(np.int32)

#print(cint)

#string list to float numpy array

equis = ['1.1', '-2.54', '-2.44', '2.99', '0.99']
tmp = np.array(equis)

#print(tmp)

tmp_float = tmp.astype(np.float64)

#print(tmp_float)

tmp_int = tmp_float.astype(np.int32)

#print(tmp_int)

#attributes of a numpy array

#shape, ndim, size already explained
#dtype obtains the type of the elements.

print('----------------------')

#Arrays and diferent dimensions.

#print(list(range(1, 13)))
arreglo=np.array(range(1, 13))
#print(arreglo)
arreglo.shape=(3,4) #change the shape from list to a matriz. the dimensions must match the 
#number of elements (12 elements from the list, dimensions must be (1,12), (4,3), (6,2) etc)...
matriz=arreglo
#print(matriz)


matriz2=matriz.reshape(3,4) #reshape obtains the reshaped object
#shape change the attribute
matriz2


#print(np.ravel(matriz2)) #flatened object with all the elements
#print("----------")
np.ravel(matriz2,order='F')
#the order parameter: 
# C to flat and order in the principal row order, default value.
# F to flat and order in the principal column order.
# K to flat and order in the order the elements were storaged.
# A to flat and order with the natural index.

#print(list(range(1, 25)))
cubo = np.array(range(1, 25))
print(cubo.size)


cubo.shape = (2, 2, 6) #three dim array: 2 number of arrays(matriz), 2 rows, 6 columns.
print(cubo)
print(cubo.shape)
print(cubo.ndim)