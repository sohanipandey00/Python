def mul_table(N, i):
	if (i > 1):
		return
	print(N,"*",N,"=",N * N)
	return mul_table(N, i + 1)
N = int(input("Enter the no.:"))

mul_table(N, 1)