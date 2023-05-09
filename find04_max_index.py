def find_max_index(data):
    """
    Given the list of numbers, return the index of maximum number in the list
    args:
        data: list of numbers
    returns: index of maximum number in the list
    """
    i=0
    k=0
    a=0
    while i<len(data):
        if k<data[i]:
            k=data[i]
            a=data.index(k)
            
        i+=1
    return a
print(find_max_index([6, 8, 7, 4, 9]))
