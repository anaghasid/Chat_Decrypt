l1=[ [12,34,56,104], [78,67,123,89], [123,127,2,9], [45,7,65,68] ]


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
            

def shifter( l2):
    val1=l2[0]
    val2=l2[1]
    val3=l2[2]
    val4=l2[3]

    l2[0]=val4
    l2[1]=val1
    l2[2]=val2
    l2[3]=val3
    return l2
    

    
l=[]
l=shiftMatrix(l1,1)
print(l)



def unshift( l , amt):
    shift=[0,0,0,0]
    for i in range(0,4):
        j=amt[i]
        while( j!=4):
            shift[i]=shifter(l1[i])
            j+=1
    return shift
    

l2=unshift(l,[2,1,0,3])
print(l2)

      
                    
                    
                    
                    
                
                    



                   
