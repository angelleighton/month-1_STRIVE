#Your functions EX 5.2
def Get_largest (num_list):
    return max(num_list)

def Get_smallest (num_list):
    return min (num_list)

def Num_of_div3 (num_list):
    counter = 0
    for x in num_list:
        if x%3 == 0:
            counter +=1
    return counter

a = [2, 4, 6, 12, 15, 99, 100]
print(Get_largest (a))
print(Get_smallest (a))
print(Num_of_div3 (a))




