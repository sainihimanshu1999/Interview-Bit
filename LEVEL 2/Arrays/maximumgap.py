def maximumGap(self, A):
		arr = []
		for idx, i in enumerate(A):
			arr.append((i, idx))
		arr.sort()
		current = arr[0][1]
		diff = -1
		for i in arr:
			if i[1] < current:
				current = i[1]
			else:
				if i[1] - current > diff:
					diff = i[1] - current
		return diff