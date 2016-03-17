# Matrix Algebra

import numpy as np

A = np.array([[1, 2, 3],
	 	      [2, 7, 4]])
B = np.array([[1, -1],
	 	      [0, 1]])
C = np.array([[5, -1],
	 	      [9, 1],
	 	      [6, 0]])
D = np.array([[3, -2, -1],
	 	      [1, 2, 3]])
u = np.array([[6, 2, -3, 5]])
v = np.array([[3, 5, -1, 4]])
w = np.array([[1],
			  [8],
			  [0],
			  [5]])
a = 6
At = np.matrix.transpose(A)
Ct = np.matrix.transpose(C)
Dt = np.matrix.transpose(D)
BBBB = np.dot(np.dot(B, B), np.dot(B, B)) # Is there a better way to do this?
DDD = np.multiply(3, D)

print '\n#############################1. Matrix Dimensions#############################\n'
print '1.1) A = ' + str(A.shape)
print '1.1) B = ' + str(B.shape)
print '1.1) C = ' + str(C.shape)
print '1.1) D = ' + str(D.shape)
print '1.1) u = ' + str(u.shape)
print '1.1) w = ' + str(w.shape)

print '\n#############################2. Vector Operations#############################\n'
print '2.1) u + v = ' + str(np.add(u, v)) + '\n'
print '2.2) u - v = ' + str(np.add(u, -v)) + '\n'
print '2.3) au = ' + str(np.multiply(a, u)) + '\n'
print '2.4) u . v = ' + str(np.inner(u, v)) + '\n'
print '2.5) ||u|| = ' + str(np.linalg.norm(u)) + ' - doing this by hand yielded 8.49'

print '\n#############################2. Matrix Operations#############################\n'
print '3.1) A + C = Undefined' + '\n'
print '3.2) A - C^t = \n' + str(np.add(A, -Ct)) + '\n'
print '3.3) C^t + 3D = \n' + str(np.add(Ct, DDD)) + '\n'
print '3.3) BA = \n' + str(np.dot(B, A)) + '\n'
print '3.4) BA = \n' + str(np.dot(B, A)) + '\n'
print '3.5) BA^t = Undefined' + '\n'
print '3.6) BC = Undefined' + '\n'
print '3.7) CB = \n' + str(np.dot(C, B)) + '\n'
print '3.8) B^4 = \n' + str(BBBB) + '\n'
print '3.9) AA^t = \n' + str(np.dot(A, At)) + '\n'
print '3.10) D^tD = \n' + str(np.dot(Dt, D)) + '\n'