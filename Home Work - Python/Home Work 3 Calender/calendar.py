"""
Student: Shai Dahan
ID: 209462712
Assignment no. 2
Program: calendar.py
"""
MOUNTS = ["January","February","March","April","May","June","July","August",
          "September", "October","November","December"]
DAYS = ["Su","Mo","Tu","We","Th","Fr","Sa"]

def check_if_year_is_loap(year):
    "this for check if year is loop or not"
    if year%400 == 0 or (year%4 == 0 and not year%100 == 0):
        return True
    else:
        return False

def Days_in_mount(year,mount):
    " return the number of days in the mount"
    if mount in ["January","May","March","July","August","October","December"]:
        return 31
    elif mount in ["April","June","September","November"]:
        return 30
    elif mount in ["February"] and check_if_year_is_loap(year) == True:
        return 29
    elif mount in["February"] and check_if_year_is_loap(year) == False:
        return 28
    else:
        return print("Wrong mount")

def day_untail_year(year):
    "count all days untail year was input if year was loop it's add 366 days if not it's add 365"
    days = 0
    for i in range(0,(year-1899)):
        if check_if_year_is_loap(year - i) == True:
            days += 366
        elif check_if_year_is_loap(year - i) ==False:
            days += 365
    return days

def day_untail_mount(year,mount):
    "This is to count the days untail the mount was input"
    sum1 = 0
    for i in range(MOUNTS.index(mount)):
        sum1 += Days_in_mount(year,MOUNTS[i])
    return sum1

def first_day_in_mount(year,mount):
    count = (day_untail_year(year) + day_untail_mount(year,mount))%7 # i use modulo 7 to get index on DAYS for know where the first day is
    return count
    
def print_calender(year,mount):
    
    count_7 = 0# this to go 1 lane down when his finish print 7 days
    print("{0}  {1}".format(mount,year))
    for day in DAYS:
        print(day,end = "  ")
    print()
    for first_day in range(0,first_day_in_mount(year,mount)):
        print("  ",end = "  ")
        count_7 +=1
    for number in range(1,Days_in_mount(year,mount)+1):
        print("{0:>2}".format(number),end = "  ")
        count_7 += 1
        if count_7%7 == 0:
            print()
        
Year_enter = int(input("Please enter a year: "))
Mount_enter = input("Please enter a Mount: ")
print("-------------------------")
print_calender(Year_enter,Mount_enter)

      
            
            
            
            
