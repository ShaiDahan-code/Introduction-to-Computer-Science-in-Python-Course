"""
Student: Shai Dahan
ID: 209462712
Assignment no. 2
Program: grades.py
"""

studentDic = {} # Dict for students Key = ID value = Name
alist = []
st = open("students.txt","r")
for i in range(0,4):    
    alist.append(st.readline().split())
st.close()
for j in range(0,len(alist)):# loop run on all alist
    studentDic[int(alist[j][0])] = alist[j][1] # cread his Key/ID
    for z in range(2,len(alist[j])):
        studentDic[int(alist[j][0])] +=" " + alist[j][z] # add to Key the Value = Name

greadsDic = {} # dict for greads Key = ID value = greads
alist = []
gr = open("grades.txt","r")
for i in range(0,4):
     alist.append(gr.readline().split())
gr.close()
for j in range(0,len(alist)): # loop run on all alist
    greadsDic[int(alist[j][0])] = [int(alist[j][1])] # cread his Key/ID
    for z in range(2,len(alist[j])):
        greadsDic[int(alist[j][0])] += [int(alist[j][z])]# add to Key the Value = greads in list

greads_sum = 0
max_sum = 0
max_ID = 0
for ID in greadsDic:  #i use this to get the avarge and who student got the best avarge.
    greads_sum = sum(greadsDic[ID])/len(greadsDic[ID]) # makeing avarge
    if max_sum < greads_sum:
        max_sum = greads_sum
        max_ID = ID
print("The student '{0}' got the '{1}' avarge. he is the best student!".format(studentDic[max_ID], max_sum))
print()

gread ={}
most_gread = 0
max_times_key = 0
for number in greadsDic: # run in loop to get the greats gread 
    for i in range(0,len(greadsDic[number])):
        if greadsDic[number][i] not in gread:
            gread[greadsDic[number][i]] = 1
        else:
           gread[greadsDic[number][i]] += 1
for max1 in gread:
    if gread[max1] >= most_gread:
        max_times_key = max1
        most_gread = gread[max1]

print("The gread that received most often is '{0}' and received: {1} times".format(max_times_key,most_gread))
print()

not_recive = []
for i in range(0,100):# enter to list all the greads that no one get
    if i not in gread:
        not_recive.append(i)
print(not_recive)