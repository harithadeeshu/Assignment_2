#Sample List : [(2, 5), (1, 2), (4, 4), (2, 3), (2, 1)]

def last(n):
	return n[-1]

a=[(2, 5), (1, 2), (4, 4), (2, 3), (2, 1)]
print("Sorted:")
print(sorted(a, key=last))
