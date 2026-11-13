import numpy as np

a = np.array([3, 4])
b = np.array([3, 4, 5])

c = np.array([
    [3, 4],
    [5, 6]
])

d = np.array([
    [3,4,6],
    [1,2,3],
    [6,4,9]
])

print("Vetor A", a.shape,  a.ndim, a.size)
print("Vetor B", b.shape, b.ndim, b.size)
print("Matriz C", c.shape, c.ndim, c.size)
print("Matriz D", d.shape, d.ndim, d.size)