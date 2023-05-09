def find_max_odd(data):
    """
    Given the list of numbers, Find the maximum odd number in the list
    args:
        data: list of numbers
    returns: maximum odd number in the list
    """
    i=0
    k=0
    while i<len(data):
        if data[i]%2==1:
            k=data[i]
        i+=1
            
    return k
print(find_max_odd([1,4,7,9,12,13,18]))