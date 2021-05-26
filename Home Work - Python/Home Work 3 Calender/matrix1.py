"""
Student: Shai Dahan
ID: 209462712
Assignment no. 3
Program: matrix.py
"""

def matrica_sihlof(m1):
    "This fanction return a loop of matrica"
    alist = []
    for i in range(len(m1[0])):# this to run on columns
        alist2 = []
        for j in range(len(m1)):# and this for i on lanes
            alist2.append(m1[j][i])
        alist.append(alist2)
    return alist

def matrica_sihlof_one_line(m1):
    "Same fanction like matrica_sihlof only in list comprehension"
    return [[add[i] for add in m1]for i in range(len(m1[0]))]
    
def matrica_Multiplication(m1,m2):
    "this fanction is to multi 2 matica"
    m3 = []
    sum1 = 0
    m1 = matrica_sihlof(m1)
    for first in range(0,len(m1)):
        m4 = []
        for secound in range(len(m1)):
            sum1 = 0
            for third in range(0,len(m1[0])):
                sum1 += m2[third][first]*m1[secound][third]
            m4.append(float(sum1))
        m3.append(m4)
    return m3

def matrix_from_file():
    "Read file and use the def matrica_Multiplication after split the txt"
    file1 = open("matrices.txt","r")
    s = file1.read()[2:].split("B=")#split to get 2 list
    s = [st.split("\n") for st in s] 
    mt1 = [line.split() for line in s[0] if line] #split in space
    mt2 = [line.split() for line in s[1] if line] #split in space
    mt1 = [[int(mt1[i][j]) for j in range(0,len(mt1[0]))] for i in range(len(mt1))] #change to int
    mt2 = [[int(mt2[i][j])for j in range(len(mt2[0]))]for i in range(len(mt2))] #change to int
    return matrica_Multiplication(mt1,mt2)
     

def print_matrix_from_file(file1):
    "to print the restult from matrix from file"
    string = ""
    for i in file1:
        string += "".join(str(word)+"  " for word in i)+"\n"
    return string

A = [[1,4],[2,5],[3,6]]
B = [[1,2],[3,4],[5,6]]
res = print_matrix_from_file(matrix_from_file())
print(res)