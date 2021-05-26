"""
Student: Shai Dahan
ID: 209462712
Assignment no. 1
Program: stats.py
"""

def str_to_List(alist): 
    "switch string to list of int"
    List1 = alist.split()
    List1 = list(map(int, List1))
    return List1

def avarge_of_numbers(alist):
    "check the avarge"
    Avarge1 = sum(alist)/len(alist)
    return Avarge1

def high_number_and_spot(alist):
    "search for the higher number and save is spot"
    spot = 0
    high_num = alist[0]
    for i in range(0 , len(alist)):
        if alist[i] >= high_num:
            high_num = alist[i]
            spot = i+1
    return (" max number is: {0}, his spot is: {1}".format(high_num,spot))

def lower_number_and_spot(alist):
    "search for the lower number and save is spot"
    spot1 = 1
    lower_num = alist[0]
    for i in range(0 , len(alist)):
        if alist[i] != lower_num:# this is to save the spot of the first lower number that was spot
            if alist[i] <= lower_num:
                lower_num = alist[i]
                spot1 = i + 1
    return (" lower number is: {0}, his spot is: {1}".format(lower_num,spot1))

def list_is_up(alist): 
    "check if the numbers in list as seires. שnd checks to see if the series is up or down or none"
    count_up = 0
    count_down = 0
    for i in range(0,len(alist)-1):
        if alist[i+1] >= alist[i]:
            count_up += 1
        if alist[i+1] <= alist[i]:
            count_down += 1
            
        if count_up == len(alist)-1:
            return  "its a rising series"
        elif count_down == len(alist)-1:
            return  "this series goes down"
        
    return "seires without order"# in case that it's not up or down it's be without order
        

Numbers = input("Enter numbers: ")
number_in_list = str_to_List(Numbers)
print("The avarge is: ", avarge_of_numbers(number_in_list))
print(high_number_and_spot(number_in_list))
print(lower_number_and_spot(number_in_list))
print(list_is_up(number_in_list))