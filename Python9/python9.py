import numpy as np
import numpy.linalg as npal

a = np.array([[4,0], [3, 1]])
print("a"+a)


q, r = npal.qr(a)

print("Factorización QR a: ")

print(npal.qr(a)[0])
print("x")
print(r)

b = np.array([[1,2], [1, 1]])
print("b"+b)


q, r = npal.qr(b)

print("Factorización QR b: ")
print(npal.qr(b)[0])
print("x")