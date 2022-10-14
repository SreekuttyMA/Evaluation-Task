n=int(input())
m=int(input())
mat = [list(range(1+i*n, 1+n*(i+1))) for i in range(n)]
col = len(mat[0])
row = len(mat)
diag= [[] for j in range( col - 1 + row)]
for x in range(col):
    for y in range(row):
        diag[x+y].append(mat[x][y])
# print(diag)

ele=diag[0],diag[1],diag[2],diag[3],diag[4]
list1=[]
for a in ele:
    for b in a:
        list1.append(b)
# print(list1)
result = []
c=0
while c < (len(list1)-2):
    result.append(list1[c:c+3])
    c+=3

for elemnt in result:
    print(elemnt[0],elemnt[1],elemnt[2])




        
        
