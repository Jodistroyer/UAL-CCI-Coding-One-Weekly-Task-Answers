def product_of_list(lst):
    result = 1
    for number in lst:
        result *= number
    return result

list1 = [1, 2, 3, 4]
result1 = product_of_list(list1)
print(result1)

