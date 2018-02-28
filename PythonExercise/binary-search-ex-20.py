## ex 20
## Element Search 

## Write a function that takes an
## ordered list of numbers
##(a list where the elements are in order from smallest to largest)
## and another number. The function decides whether or not the given number
## is inside the list and returns (then prints) an appropriate boolean.


'''
def find(ordered_list, num):
    ordered_list = sorted(ordered_list)
    for i in ordered_list:
        if i == num:
            return True
    return False

if __name__=="__main__":
    
    l = [2, 4, 6, 8, 10]
    print(find(l, 5)) # prints False
    print(find(l, 10)) # prints True
    print(find(l, -1)) # prints False
    print(find(l, 2)) # prints True
'''


# using binary search
# using dynamic programming

def find(ordered_list, num):
    if len(ordered_list) == 1: #edge case when length of list is just 1
        return True if ordered_list[0] == num else False

    middle_index = int(len(ordered_list) / 2)
    if ordered_list[middle_index] == num:
        return True
    elif ordered_list[middle_index] > num:
        return find(ordered_list[:middle_index:], num)
    else:
        return find(ordered_list[middle_index::], num)


if __name__=="__main__":
  l = [2, 4, 6, 8, 10]
  print(find(l, 5)) # prints False
  print(find(l, 10)) # prints True
  print(find(l, -1)) # prints False
  print(find(l, 2)) # prints True
        
