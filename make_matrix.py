string1 = "hello how is everyone"

i=0
leng = len(string1)
print(leng)
# string2 = string1[::-1]
if (leng%16)!=0:
    rem = 16 - leng%16
    print(leng,rem)
    for i in range(0,rem):
        string1 = string1 + chr(0)
print(string1)

leng = len(string1)
print(leng)
count = 0
mat_arr = []
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

print("Matrix: ",mat_arr)


