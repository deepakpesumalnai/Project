import numpy as np

my_first_array = np.array([1, 2, 3, 4, 5])
print(my_first_array)
print(type(my_first_array))

DistanceInKM = [1, 23, 4.5, 3.5, 23.56]
print(DistanceInKM)
DistanceInMeters = [items*1000 for items in DistanceInKM]
print(DistanceInMeters)
print(np.array(DistanceInKM)*1000)
print(len(DistanceInMeters))

a_1 = np.arange(1, 10, .5)
print(a_1.dtype)
print(a_1.ndim)
a_2 = range(1, 20, 1)
print(a_1)
print(list(a_2))

print(a_1[::-3])
print(list(a_2)[::-3])


my_first_array = np.array([1.1, 2.2, 3.3, 4.4, 15.5], float)
print(my_first_array)
print(my_first_array.mean())
print(np.median(my_first_array))
print(my_first_array.max())
print(my_first_array.argmax())
print(my_first_array > 2.2)

greater_than = my_first_array > 2.2
print(any(greater_than))
print(all(greater_than))
print(greater_than)

my_second_array = np.array([7, 8, 9], float)

print(np.concatenate((my_first_array, my_second_array)))
print(np.concatenate((my_second_array, my_first_array)))


