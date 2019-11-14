import numpy as np
import sys

def print_s(l,s,i,j):
    # if bar length is 2, which is minimum length -> print the last cut
    if (j-i)==2:
        return print(l[int(s[i,j])], end = ' ') 
    # if bar length is 1, no cut is possible 
    if (j-i)==1 or i==j:
        return None
    else:
        # ptint current cut and then cut left and right pieces recursively
        print(l[int(s[i,j])], end = ' ')
        print_s(l,s,i,int(s[i,j]))
        print_s(l,s,int(s[i,j]),j)


# Taking arguments and make array "l"
arguments = (sys.argv) 
f = open(arguments[1], "r")
line1 = f.readline().rstrip('\n').split(" ")
line2 = f.readline().rstrip('\n').split(" ")

# add "0" to beginning and "L" to the end
l=line2
l.insert(0,"0")
l.append(line1[0])

#make "m" and "s" matrices
m = np.zeros((6,6))
s = np.zeros((6,6))
n = len(l)-1

for l_c in range (2,n+1):
    for i in range(0,n-l_c+1):
        j=i+l_c
        m[i,j]=99990
        for k in range(i+1,j):
            q = m[i,k]+m[k,j]+(int(l[j])-int(l[i]))
            if q<m[i,j]:
                m[i,j]=q
                s[i,j]=k
print("Matrix 'm':")
print(m)
print("Matrix 's':")
print(s)
# show the array with start, end, and location of cuts
print("This is the array: "+str(l))
# print minimum cost
print("Minimum cost : "+ str(m[0,n]) )
# print locations of cust using function "print_s" recusrsively
print("Cheapest cuts:", end = ' ')
print_s(l,s,0,n)
print("")

