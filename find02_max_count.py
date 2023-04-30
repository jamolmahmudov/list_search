def find_max_count(data):
    """
    Given the list of numbers, Find count of maximum numbers in the list
    args:
        data: list of numbers
    returns: count of maximum numbers in the list
    """
    i=0
    k=0
    a=0
    while i<len(data):
        if k<data[i]:
            k=data[i]
            a=data.count(k)
        i+=1
    return a
print(find_max_count.py([1, 2, 3, 5, 4, 5])) 
    
