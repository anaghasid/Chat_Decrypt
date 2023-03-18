import random

samp_string = "hello how is everyone"
mat_arr = []

def makeMatrix(string1, mat_arr):
    i=0
    leng = len(string1)
    # string2 = string1[::-1]
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


def offset(matrix):
    n=random.randint(1,7)
    match n:
        case 1:
            for i in range(len(matrix[0])):
                matrix[0][i] += 5 #row addition
        case 2:
            for i in range(len(matrix[0])):
                matrix[i][0]+= 5 #column addition
        case 3:
            for i in range(len(matrix[0])):
                matrix[0][i]+=5 #2 rows addition
                matrix[1][i]+=5
        case 4:
            for i in range(len(matrix[0])):
                matrix[2][i]-=5 #2 row subtraction
                matrix[3][i]-=5
                
        case 5:
            for i in range(len(matrix[0])):
                matrix[i][1] +=5
                matrix[i][2] +=5
                matrix[i][0] -=5
                matrix[i][3] -=5
                
        case 6:
            for i in range(len(matrix[0])):
                matrix[i][i]+=5 #diagonal 
        case 7:
            matrix[0, 0]+= 5
            matrix[0, -1]+=5
            matrix[-1, 0]+=5
            matrix[-1, -1]+=5
    return matrix


makeMatrix(samp_string, mat_arr)
print("Matrix: ",mat_arr)
print("After offset: ",offset(mat_arr))
