def solve(self, A):
	    # A is a list of strings
	    n = len(A)
	    arr = [float(i) for i in A]
	    sumi, x, y, z =  0.0, arr[0], arr[1], arr[2]
	    for i in range(3, n):
	        sumi = x + y + z
	        if 1 < sumi < 2:
	            return 1
	       
            elif sumi > 2:
                if x > y and x > z:
                    x = arr[i]
                elif y > x and y > z:
                    y = arr[i]
                else:
                    z = arr[i]
            
            else:
                if x < y and x < z:
                    x = arr[i]
                elif y < x and y < z:
                    y = arr[i]
                else:
                    z = arr[i]
        
        sumi = x + y + z
        return int(1 < sumi < 2)