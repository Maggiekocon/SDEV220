def add(a,b):
    return a+b

def subtract(a,b): 
    return a - b

def mult(a,b):
    return a*b


def find_duplicates_in_set(nums):
    seen = set()
    duplicates = set()

    for num in nums:
        if num in seen:
            duplicates.add(num)
        else:
            seen.add(num)
    return list(duplicates)



