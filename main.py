#!/usr/bin/python3
def sum_to_n(n):
    sum = 0

    for i in range(1, n + 1):
        sum += i

def sum_evens(n):
    sum = 0
    
    for i in range(2, n + 1, 2):
        sum += i

def sum_odds(n):
    sum = 0

    for i in range(1, n + 1, 2):
        sum += i

    return sum

def sum_multiples_of_three(n):
    sum = 0

    for i in range(3, n + 1, 3):
        sum += i

    return sum

def sum_range(start, end):
    sum = 0

    for i in range(start, end + 1): # can this be a while loop?
        print(f"SUM BEFORE: {sum}")
        sum += 1
        print(f"SUM AFTER: {sum}")

    # return 

# # sum_to_n TEST
# test1 = sum_to_n(10)
# test2 = sum_to_n(5)
# test3 = sum_to_n(30)

# print(test1, test2, test3)

# # sum_evens TEST
# test1 = sum_evens(10)
# test2 = sum_evens(6)
# test3 = sum_evens(30)

# print(test1, test2, test3)

# # sum_odds TEST
# test1 = sum_odds(11)
# test2 = sum_odds(3)
# test3 = sum_odds(33)

# print(test1, test2, test3)

# # sum_multiples_of_three TEST
# test1 = sum_multiples_of_three(12)
# test2 = sum_multiples_of_three(6)
# test3 = sum_multiples_of_three(33)

# print(test1, test2, test3)

# sum_range TEST
test1 = sum_range(2, 12)
# test2 = sum_range(6, 23)
# test3 = sum_range(14, 33)

# print(test1, test2, test3)
print(test1)
# print(test3)