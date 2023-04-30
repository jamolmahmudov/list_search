def find_max_min_sum(data):
    """
    Given the list of numbers, return the sum of the maximum and minimum numbers in the list
    args:
        data: list of numbers
    returns: sum of the maximum and minimum numbers in the list
    """
    # i=0
    # max=0
    # min=0
    
    # while i<len(data):
    #     if max<data[i]:
    #         max=data[i]
    
    #     if min>data[i]:
    #         min=data[i]
    #     i+=1
    return data[0]+data[-1]
print(find_max_min_sum([1, 2, 3, 4, 5]))
