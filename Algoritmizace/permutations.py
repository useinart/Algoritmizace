def permutations(array):
    if len(array) == 0:
        return [[]]
    elif len(array) == 1:
        return [array]
    list = []
    for el in range(len(array)):
        m = array[el]
        remainL = array[:el] + array[el+1:]
        print(remainL)
        for perm in permutations(remainL):
            list.append([m] + perm)

    return list

array = [1,2,3]
print(permutations(array))


