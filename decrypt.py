dec_string = ""
mat = [[104, 101, 108, 108], [111, 32, 104, 111], [119, 32, 105, 115], [32, 101, 118, 101], [114, 121, 111, 110], [101, 0, 0, 0]]
def getString(res_str, mat_arr):
    for i in range(4):
        for j in range(4):
            res_str += chr(mat_arr[i][j])
    return res_str

print(mat[0][0])
print(mat[0][1])
print(mat[0][3])
print(getString(dec_string, mat))