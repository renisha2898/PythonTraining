def print_matrix(mat):
    for i in range (len(mat)):
        for j in range (len(mat)):
            print(str(mat[i][j]), end = " ")
        print()
def transpose_matrix(mat):
    for i in range(len(mat)):
        for j in range(i,len(mat)):
            mat[i][j], mat[j][i] = mat[j][i],mat[i][j]
def reverse_rows(mat):
    for i in range (len(mat)):
        k = len(mat) - 1;
        for j in range(0,k):
            mat[i][j], mat[i][k] = mat[i][k], mat[i][j]
            k = k - 1
def reverse_columns(mat):
 for i in range (len(mat)):
    k = len(mat) - 1;
    for j in range(0,k):
        mat[j][i], mat[k][i] = mat[k][i], mat[j][i]
        k = k - 1

if __name__ == '__main__':
    
    mat = [[1,2,3], 
           [4,5,6],
           [7,8,9]];
    print_matrix(mat)
    transpose_matrix(mat)
    
    
    #reverse_rows(mat)
    reverse_columns(mat)  #(for Anticlockwise rotation)
    
    print("\nThe array after rotation is ")
    print_matrix(mat)
