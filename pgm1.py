def transpose(m):
    
    res=[[0,0,0],[0,0,0]]
    for i in range(len(m)):
        for j in range(len(m[0])):
            res[j][i]=m[i][j]
    for x in res:
        print(x)

if __name__ == '__main__':
    matrix=[[4,7],[5,2],[9,3]]
    transpose(matrix)