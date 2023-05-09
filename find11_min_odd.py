def find_min_odd(data):
    """
    Given the list of numbers, Find the minimum odd number in the list
    args:
        data: list of numbers
    returns: minimum odd number in the list
    """
    i=0
    a=data[0]
    while i<len(data):
        if a>data[i] and data[i]%2==1:
            a=data[i]
        i+=1
    return a
print(find_min_odd([2,5,3,1,2,6]))

