mat = [[104, 101, 108, 108], [111, 32, 104, 111], [119, 32, 105, 115], [32, 101, 118, 101], [114, 121, 111, 110], [101, 0, 0, 0]]
mat2 = [[109, 101, 108, 108], [116, 32, 104, 111], [124, 32, 105, 115], [37, 101, 118, 101], [114, 121, 111, 110], [101, 0, 0, 0], [0, 0, 0, 0], [0, 0, 0, 0]]

def makeMatrix(string1):
    mat_arr = []
    i=0
    leng = len(string1)
    if (leng%16)!=0:
        rem = 16 - leng%16
        for i in range(0,rem):
            string1 = string1 + chr(0)

    leng = len(string1)
    count = 0
    i=0
    while i<leng:
        temp_l = []
        for j in range(i, (i+4)):
            if j<leng:
                # print(string1[j],end=" ")
                temp_l.append(ord(string1[j]))

        i = j + 1
        if(i>leng):
            break
        mat_arr.append(temp_l)
        count += 1
    return mat_arr

def getString(mat_arr):
    res_str = ""
    for i in range(4):
        for j in range(4):
            res_str += chr(mat_arr[i][j])
    return res_str


def offsetReverse(matrix,n):
    match n:
        case 1:
            for i in range(len(matrix[0])):
                matrix[0][i] -= 5 #row addition
        case 2:
            for i in range(len(matrix[0])):
                matrix[i][0]-= 5 #column addition
        case 3:
            for i in range(len(matrix[0])):
                matrix[1][i]-=5
                matrix[0][i]-=5 #2 rows addition
        case 4:
            for i in range(len(matrix[0])):
                matrix[3][i]+=5
                matrix[2][i]+=5 #2 row subtraction
                
        case 5:
            for i in range(len(matrix[0])):
                matrix[i][3] +=5
                matrix[i][0] +=5
                matrix[i][2] -=5
                matrix[i][1] -=5
                
        case 6:
            for i in range(len(matrix[0])):
                matrix[i][i]-=5 #diagonal 
        case 7:
            matrix[-1, -1]-=5
            matrix[-1, 0]-=5
            matrix[0, -1]-=5
            matrix[0, 0]-= 5
    return matrix

ded = "elmlev%e i|s hto"
mat = makeMatrix(ded)
print(getString(mat))

mat3 = offsetReverse(mat2,2)
print(getString(mat3))