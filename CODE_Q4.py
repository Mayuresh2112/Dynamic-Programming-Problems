def LCS(x,y,m,n):
    if m==0 or n==0:
        return 0
    elif x[m-1] == y[n-1]:
        return 1+LCS(x,y,m-1,n-1)
    else:
        return max(LCS(x, y, m, n - 1), LCS(x, y, m - 1, n))

x=input("Enter 1st String Sequence:- ")
y=input("Enter 2nd String Sequence:- ")
print("Length of LCS is:- ",LCS(x,y,len(x),len(y)))