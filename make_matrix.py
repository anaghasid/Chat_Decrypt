import random

samp_string = "hello how is everyone"
mat_arr = []

def makeMatrix(string1, mat_arr):
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

def interchange(l1,p):
  match p:
    case 1:
      row(0,1,l1)
      row(2,3,l1)
    case 2:
      row(0,3,l1)
      row(2,1,l1)
      row(0,1,l1)
    case 3:
      col(0,1,l1)
      col(2,3,l1)
      col(3,1,l1)
    case 4:
      row(0,2,l1)
      col(1,3,l1)
      row(1,3,l1)
    case 5:
      row(1,3,l1)
      col(0,1,l1)
      col(1,2,l1)
    case 6:
      col(1,3,l1)
      row(2,1,l1)
      col(2,1,l1)
    case 7:
      row(1,3,l1)
      row(1,2,l1)
      col(1,2,l1)
    case 8:
      row(0,1,l1)
      row(0,2,l1)
      row(2,3,l1)
    case 9:
      row(0,1,l1)
      col(0,1,l1)
      col(1,2,l1)
  return l1

def row(a,b,l1):
  l1[a],l1[b]=l1[b],l1[a]
  
def col(a,b,l1):
  for i in l1:
    i[a],i[b]=i[b],i[a]

def printMatrix(mat):
    for i in range(4):
        for j in range(4):
            print(mat[i][j],end=" ")
        print()
    print()



def offsetReverse(matrix):
    n=random.randint(1,7)
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
            matrix[0, 0]-= 5
            matrix[0, -1]-=5
            matrix[-1, 0]+=5
            matrix[-1, -1]+=5
    return matrix


makeMatrix(samp_string, mat_arr)
printMatrix(mat_arr)
# print("After offset: ",offset(mat_arr))
printMatrix(interchange(mat_arr,4))

