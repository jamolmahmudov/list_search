def find_min_count(data):
    """
    Given the list of numbers, Find count of minimum numbers in the list
    args:
        data: list of numbers
    returns: count of minimum numbers in the list
    """
    i=0
    a=data[0]
    k=0
    while i<len(data):
        if a>data[i]:
            a=data[i]
            k=data.count(a)
        i+=1
    return k
print(find_min_count([7,2,3,4,5,6,1,3,1,1,3,1]))
