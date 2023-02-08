m,n = list(map(int,input().split()))
matrix=[]
total=0
for i in range(m):
    numbers=list(map(int,input().split()))
    matrix.append(numbers)
for i in range(m):
    for j in range(n):
        if i==0 or i==m-1:
            total+=matrix[i][j]
        else:
            if j==0 or j==n-1:
                total+=matrix[i][j]
print(total)
