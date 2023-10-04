def mul_table(N, i):
	if (i > 10):
		return
	print(N,"*",i,"=",N * i)
	return mul_table(N, i + 1)
N = int(input("Enter the no.:"))

mul_table(N, 1)