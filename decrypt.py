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
                if(string1[j]=='~'):
                   temp_l.append(0)
                else:
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
                matrix[0][i] = (matrix[0][i] - 5)%128 #row addition
        case 2:
            for i in range(len(matrix[0])):
                matrix[i][0] = (matrix[i][0] - 5)%128 #column addition
        case 3:
            for i in range(len(matrix[0])):
                matrix[1][i] = (matrix[1][i]-5)%128
                matrix[0][i] = (matrix[0][i]-5)%128 #2 rows addition
        case 4:
            for i in range(len(matrix[0])):
                matrix[3][i] = (matrix[3][i]+5)%128
                matrix[2][i] = (matrix[2][i]+5)%128 #2 row subtraction
                
        case 5:
            for i in range(len(matrix[0])):
                matrix[i][3] = (matrix[i][3] +5)%128
                matrix[i][0] = (matrix[i][0] +5)%128
                matrix[i][2] = (matrix[i][2] -5)%128
                matrix[i][1] = (matrix[i][1] -5)%128
                
        case 6:
            for i in range(len(matrix[0])):
                matrix[i][i] = (matrix[i][i]-5)%128 #diagonal 
        case 7:
            matrix[-1,-1] = (matrix[-1,-1]-5)%128
            matrix[-1,0] = (matrix[-1,0]-5)%128
            matrix[0,-1] = (matrix[0,-1]-5)%128
            matrix[0,0] = (matrix[0, 0]-5)%128
    return matrix

def interchangeInverse(l1,p):
  match p:
    case 1:
      row(0,1,l1)
      row(2,3,l1)
    case 2:
      row(0,3,l1)
      row(2,1,l1)
      row(2,3,l1)
    case 3:
      col(0,1,l1)
      col(2,3,l1)
      col(0,2,l1)
    case 4:
      row(1,3,l1)
      col(1,3,l1)
      row(0,2,l1)
    case 5:
      col(1,2,l1)
      col(0,1,l1)
      row(1,3,l1)
    case 6:
      col(2,1,l1)
      row(2,1,l1)
      col(1,3,l1)
    case 7:
      col(1,2,l1)
      row(1,2,l1)
      row(1,3,l1)
    case 8:
      row(2,3,l1)
      row(0,2,l1)
      row(0,1,l1)
    case 9:
      col(1,2,l1)
      col(0,1,l1)
      row(0,1,l1)
  return l1

def row(a,b,l1):
  l1[a],l1[b]=l1[b],l1[a]
  
def col(a,b,l1):
  for i in l1:
    i[a],i[b]=i[b],i[a]


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

def unshift(l1, amt):
    shift=[0,0,0,0]
    for i in range(0,4):
        j=amt[i]
        while(j!=4):
            shift[i]=shifter(l1[i])
            j+=1
    return shift

def decodeFun(key,mat):
   for i in range(14,0,-2):
      match key[i]:
         case 1: offsetReverse(mat,key[i+1])
         case 2: transpose(mat,key[i+1])
         case 3: unshift(mat,key[i+1])
        #  case 4: offsetReverse(mat,key[i+1])


ded = "sfz♣lm~or ~~n~~m"
mat1 = makeMatrix(ded)

# m = [[108, 111, 98, 98], [101, 104, 101, 113], [102, 100, 0, 0], [0, 0, 0, 5]]
# print(unshift(m,[0,3,0,3]))
mat2 = unshift(mat1,[0,3,0,3])
# print(mat2)
# # mat3 = interchangeInverse(mat1,4)
mat2 = transpose(mat1)
mat2 = offsetReverse(mat2,2)
print(getString(mat2))