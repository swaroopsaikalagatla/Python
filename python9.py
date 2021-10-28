def greatest(*nos):
    result = nos[0]
    for num in nos:
        if num > result:
            result = num
    return result
print(greatest(10,50,30))