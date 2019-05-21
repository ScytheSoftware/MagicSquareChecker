
#This program checks for 3x3 magical squares. the user enters their own 3x3 matrix.

import os
import time
import numpy as np

def clear_screen():
	os.system("cls" if os.name == "nt" else "clear")
#nt is a window check, if you are on window use cls, else clear(Mac)


XAxis = 3 
YAxis = 3 

matrix_3x3 = [
	[0,0,0],
	[0,0,0],
	[0,0,0]
]



for i in range(XAxis):
	for j in range(YAxis):
		print("Current Matrix: ")
		print(np.array(matrix_3x3))
		print("")
		print("Enter in the the position ", "X: ", i, "Y: ", j)
		print("")
		tempnum = input("Enter a number: ")
		matrix_3x3[i][j] = int(tempnum)
		clear_screen()


print(np.array(matrix_3x3))


def is_magic(square):
	m_chk, m_dia = 0, 0
	for y in range(len(square)):
		row, col = 0, 0
		for x in range(len(square)):
			row += square[x][y]
			col += square[y][x]
		if row != col:
			return False
		m_dia += square[y][y]
		m_chk += square[len(square)-y-1][y]
	if m_chk == row == col == m_dia:
		return True
	return False

print(is_magic(np.array(matrix_3x3)))
