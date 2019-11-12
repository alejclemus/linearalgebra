import numpy as np
import numpy.linalg as npal

print('------------------------------------------------------')  
print("EJERICIO 1:")
print('------------------------------------------------------\n') 

a = np.array([[4,0], [3, 1]])
print("matriz A:")
print(a)


qa, ra = npal.qr(a)

print("Factorización QR A: ")

print(npal.qr(a)[0])
print("x")
print(ra)

b = np.array([[1,2], [1, 1]])
print("matriz B:")
print(b)


qb, rb = npal.qr(b)

print("Factorización QR B: ")
print(npal.qr(b)[0])
print("x")
print(rb)

c = np.matrix([[2,1], [1, -1], [2,1]])
print("matriz C:")
print(c)


qc, rc = npal.qr(c)

print("Factorización QR C: ")

print(npal.qr(c)[0])
print("x")
print(rc)

d = np.matrix([[4,8,1], [0, 2, -2], [3,6,7]])
print("matriz D:")
print(d)


qd, rd = npal.qr(d)

print("Factorización QR D: ")

print(npal.qr(d)[0])
print("x")
print(rd)

print('\n------------------------------------------------------')  
print("EJERICIO 2:")
print('------------------------------------------------------\n') 

print("a)")
aa = np.array([[2,3], [-2, -6], [1, 0]])
ab = np.array([[3], [-3], [6]])
print("A:")
print(aa)
print("b:")
print(ab)

print("-------------------------------")

q, r = npal.qr(qa)

print(r)
print("x")
print("[x1, x2]")
print("=")
print(np.transpose(q))
print("x")
print(ab)

print("-------------------------------")

print("Qt x b")
print(np.dot(np.transpose(q), ab))

print("-------------------------------")
print("R/")
print(npal.solve(r, np.dot(np.transpose(q), ab)))

print("b)")
ab = np.array([[2,4], [0, -1], [2, -1], [1, 3]])
bb = np.array([[-1], [3], [2], [1]])
print("A")
print(ab)
print("b")
print(bb)

print("-------------------------------")

q, r = npal.qr(ab)

print(r)
print("x")
print("[x1, x2]")
print("=")
print(np.transpose(q))
print("x")
print(bb)

print("-------------------------------")

print("Qt x b")
print(np.dot(np.transpose(q), bb))

print("-------------------------------")
print("R/")
print(npal.solve(r, np.dot(np.transpose(q), bb)))

print("c)")

ac = np.array([[3, -1, 2], [4,1,0], [-3, 2, -1], [1,1,5] , [-2,0,3]])
bc = np.array([[10], [10], [-5], [15], [0]])
print("A")
print(ac)
print("b")
print(bc)

print("-------------------------------")

q, r = npal.qr(ac)

print(r)
print("x")
print("[x1, x2, x3]")
print("=")
print(np.transpose(q))
print("x")
print(bc)

print("-------------------------------")

print("Qt x b")
print(np.dot(np.transpose(q), bc))

print("-------------------------------")
print("R/")
print(npal.solve(r, np.dot(np.transpose(q), bc)))

print("d)")
ad = np.array([[4,2 ,3, 0], [-2, 3, -1 ,1], [1 ,3 ,-4, 2], [1 ,0 ,1 ,-1] , [3 ,1 ,3 ,-2]])
bd = np.array([[10], [0], [2], [0], [5]])
print("A")
print(ad)
print("b")
print(bd)

print("-------------------------------")

q, r = npal.qr(ad)

print(r)
print("x")
print("[x1, x2, x3, x4]")
print("=")
print(np.transpose(q))
print("x")
print(bd)

print("-------------------------------")

print("Qt x b")
print(np.dot(np.transpose(q), bd))

print("-------------------------------")
print("R/")
print(npal.solve(r, np.dot(np.transpose(q), bd)))