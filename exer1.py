#!/usr/bin/python3

#Exercise1. Modifiy print_matrix1 function to generate the same matrix found in:
#https://upload.wikimedia.org/wikipedia/commons/2/28/Smith-Waterman-Algorithm-Example-Step2.png
#or like sw.PNG

def print_matrix(a,x,y):
	mrows = len(x)+1
	ncols = len(y)+1

	# print aligned letters for first row
	print(" ", end='  ')
	print(" ", end='  ')
	for letter in y:
		print(letter, end='  ')

	print()
	for i in range(mrows):
		#print corresponding letter at start of each row
		if i!=0:
			print(x[i-1], end=' ')
		else:
			print(" ", end=' ')

		#print matrix value
		for j in range(ncols):
			print("%2d" % a[i][j], end=' ')

		print()

def print_trace(a,b,x,y):
	mrows = len(x)+1
	ncols = len(y)+1

	maxnum = 0
	maxcol = 0
	maxrow = 0

	string1 = ""
	string2 = ""

	# find max number in matrix
	for i in range(mrows):
		for j in range(ncols):
			if a[i][j] > maxnum:
				maxnum = a[i][j]
				maxrow = i
				maxcol = j

	# iterate until it reaches 0
	while a[maxrow][maxcol] != 0:
		if b[maxrow][maxcol] == 3: # if match
			# append to string
			string1 = string1 + x[maxrow-1]
			string2 = string2 + y[maxcol-1]

			# update maxrow and maxcol
			maxrow = maxrow - 1
			maxcol = maxcol - 1

		if b[maxrow][maxcol] == 2: # if delete
			# append to string
			string1 = string1 + "-"
			string2 = string2 + y[maxcol-1]
			 

			# update maxrow and maxcol
			maxrow = maxrow - 1

		if b[maxrow][maxcol] == 1: # if insert
			# append to string
			string1 = string1 + x[maxrow-1]
			string2 = string2 + "-"

			# update maxrow and maxcol
			maxcol = maxcol - 1

	# reverse resulting string
	string1 = string1[::-1]
	string2 = string2[::-1]

	# print resulting string
	ite = len(string1)

	# ~ print string 1
	for i in range(ite):
		print(string1[i], end=' ')
	print()

	# ~ print possible connect lines
	for i in range(ite):
		if string1[i] == "-" or string2[i] == "-":
			print(" ", end=' ')
		else:
			print("|", end=' ')
	print()

	# ~ print string 2
	for i in range(ite):
		print(string2[i], end=' ')
	print()

def gen_score(x, y, match_score=3, gap_cost=2):
	mrows = len(x)
	ncols = len(y)

	#initialize matrix to zeroes
	a = [0] * (mrows + 1)
	for i in range(mrows + 1):
		a[i] = [0] * (ncols + 1)
	
	#print_matrix(a,x,y)
	
	for i in range(1,mrows+1):
		for j in range(1,ncols+1):
			match = a[i-1][j-1] - match_score
			if(x[i-1] == y[j-1]):
				match = a[i-1][j-1] + match_score
			delete = a[i - 1][j] - gap_cost
			insert = a[i][j - 1] - gap_cost
			a[i][j]=max(match,delete,insert,0)

	#print_matrix(a,x,y)	
	return(a)

def gen_match(x, y, match_score=3, gap_cost=2):
	mrows = len(x)
	ncols = len(y)

	#initialize matrix to zeroes
	a = [0] * (mrows + 1)
	for i in range(mrows + 1):
		a[i] = [0] * (ncols + 1)
	
	for i in range(1,mrows+1):
		for j in range(1,ncols+1):
			match = a[i-1][j-1] - match_score
			if(x[i-1] == y[j-1]):
				match = a[i-1][j-1] + match_score
			delete = a[i - 1][j] - gap_cost
			insert = a[i][j - 1] - gap_cost

			if match == max(match,delete,insert,0):
				a[i][j] = 3
			elif delete == max(match,delete,insert,0):
				a[i][j] = 2
			elif insert == max(match,delete,insert,0):
				a[i][j] = 1
			else:
				a[i][j] = 0

	#print_matrix(a,x,y)	
	return(a)
	
x = "GGTTGACTA"	
y = "TGTTACGG"

a = gen_score(x,y)
b = gen_match(x,y)

print("Score Matrix: ")
print_matrix(a,x,y)
print()
print("Tracing Matrix: ")
print_matrix(b,x,y)
print()
print("Local Alignment: ")
print_trace(a,b,x,y)


