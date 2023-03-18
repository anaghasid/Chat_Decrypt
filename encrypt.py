import random


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


def offset(matrix,n):
    match n:
        case 1:
            for i in range(len(matrix[0])):
                matrix[0][i] = (matrix[0][i] + 5)%128 #row addition
        case 2:
            for i in range(len(matrix[0])):
                matrix[i][0] = (matrix[i][0]+ 5)%128 #column addition
        case 3:
            for i in range(len(matrix[0])):
                matrix[0][i] = (matrix[0][i]+5)%128 #2 rows addition
                matrix[1][i] = (matrix[1][i]+5)%128
        case 4:
            for i in range(len(matrix[0])):
                matrix[2][i] = (matrix[2][i]-5)%128 #2 row subtraction
                matrix[3][i] = (matrix[3][i]-5)%128
                
        case 5:
            for i in range(len(matrix[0])):
                matrix[i][1] = (matrix[i][1] +5)%128
                matrix[i][2] = (matrix[i][2] +5)%128
                matrix[i][0] = (matrix[i][0] -5)%128
                matrix[i][3] = (matrix[i][3] -5)%128
                
        case 6:
            for i in range(len(matrix[0])):
                matrix[i][i] = (matrix[i][i]+5)%128 #diagonal 
        case 7:
            matrix[0,0] = (matrix[0, 0]+5)%128
            matrix[0,-1] = (matrix[0,-1]+5)%128
            matrix[-1,0] = (matrix[-1,0]+5)%128
            matrix[-1,-1] = (matrix[-1,-1]+5)%128
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
    case 4:
      row(0,1,l1)
      col(0,1,l1)
      col(1,2,l1)
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

def fun1(l1,amt):
    shift=[0,0,0,0]
    for i in range(0,4):
        j=0
        if j==amt[i]:
            shift[i] = l1[i]
        while( j!=amt[ i ] ):
            shift[i]=shifter(l1[i])
            j+=1
    return shift


def shiftMatrix(l1,op):
    shift=[0,0,0,0]
   
    if op==1:
        shift=fun1(l1,[2,1,0,3])

    elif op==2:
        shift=fun1(l1,[1,2,0,3])

    elif op==3:
        shift=fun1(l1,[0,3,0,3])

    elif op==4:
        shift=fun1(l1,[2,3,1,0])

    elif op==5:
        shift=fun1(l1,[3,0,0,2])

    elif op==6:
        shift=fun1(l1,[0,1,2,3])

    elif op==7:
        shift=fun1(l1,[1,1,2,1])        
    return shift
            
def shifter(l2):
    val1=l2[0]
    val2=l2[1]
    val3=l2[2]
    val4=l2[3]

    l2[0]=val4
    l2[1]=val1
    l2[2]=val2
    l2[3]=val3
    return l2
    

def getString(mat_arr):
    res_str = ""
    for i in range(4):
        for j in range(4):
            if mat_arr[i][j]==0:
                res_str += '~'
            else:
                res_str += chr(mat_arr[i][j])
    return res_str

def transpose(l1):
    l2 = []
    # iterate over list l1 to the length of an item
    for i in range(len(l1[0])):
       
        row =[]
        for item in l1:
            # appending to new list with values and index positions
            # i contains index position and item contains values
            row.append(item[i])
        l2.append(row)
    return l2

def generateKey():
    s = ""
    for i in range(8):
        n1 = random.randint(1,3)
        n2 = random.randint(1,7)
        s += str(n1)
        s += str(n2)
    return s

def encodeFun(key,mat):
    for i in range(0,14,2):
        match int(key[i]):
            case 1: mat = offset(mat,int(key[i+1]))
            case 2: mat = transpose(mat)
            case 3: mat = shiftMatrix(mat,int(key[i+1]))
    return mat

# mat_arr = offset(mat_arr,2)
# # mat_arr = interchange(mat_arr,3)
# mat_arr = transpose(mat_arr)

# s = generateKey()
samp_string = "normal num"
mat_arr = makeMatrix(samp_string)
s= "3523363124363235"
# mat_arr = shiftMatrix(mat_arr,3)
# mat_arr = transpose(mat_arr)
# mat_arr = shiftMatrix(mat_arr,6)
# mat_arr = shiftMatrix(mat_arr,1)
# mat_arr = transpose(mat_arr)
# mat_arr = shiftMatrix(mat_arr,6)
# mat_arr = shiftMatrix(mat_arr,2)
# mat_arr = shiftMatrix(mat_arr,5)

mat_arr = encodeFun(s,mat_arr)

print(s)

print("String after operations: ",getString(mat_arr))

