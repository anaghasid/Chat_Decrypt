l1=[ [12,34,56,104], [78,67,123,89], [123,127,2,9], [45,7,65,68] ]


def fun1(l1,amt):
    shift=[0,0,0,0]
    for i in range(0,4):
        j=0
        while( j!=amt[ i ] ):
            shift[i]=shifter( l1[i])
            j+=1
    return shift

def arr(op):
    amt=[0,0,0,0]
    if op==1:
        amt=[2,1,0,3]
    elif op==2:
        amt=[1,2,0,3]
    elif op==3:
        amt=[0,3,0,3]
    elif op==4:
        amt=[2,3,1,0]
    elif op==5:
        amt=[3,0,0,2]
    elif op==6:
        amt=[0,1,2,3]
    elif op==7:
        amt=[1,1,2,1]
    return amt
        

def fun( l1,op):
    shift=[0,0,0,0]
    amt=arr(op)
   
    if op==1:
        shift=fun1(l1,amt)

    elif op==2:
        shift=fun1(l1,amt)

    elif op==3:
        shift=fun1(l1,amt)

    elif op==4:
        shift=fun1(l1,amt)

    elif op==5:
        shift=fun1(l1,amt)

    elif op==6:
        shift=fun1(l1,amt)

    elif op==7:
        shift=fun1(l1,amt)

            
    return [shift,op]
            

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
    

    
l=[0,0]
l[0]=fun(l1,1)
option=l[1]
print(l[0])



def unshift( l , op):
    amt=arr(op)
    shift=[0,0,0,0]
    op=l[1]
    for i in range(0,4):
        j=amt[i]
        while( j!=4):
            shift[i]=shifter( l1[i])
            j+=1
    return shift
    

l2=unshift(l,option)
print(l2)

      
                    
                    
                    
                    
                
                    



                   

      
                    
                    
                    
                    
                
                    



                   
