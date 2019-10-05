def polyEval(polynom, x):
    answer = 0
    for num in range(len(polynom)):
        if num == 0:
            answer += polynom[num]
        else:
            answer += polynom[num] * (x ** num)
    return answer





def polySum(polynom1,polynom2):
    sum = []
    if len(polynom1) > len(polynom2):
        while len(polynom1) != len(polynom2):
            polynom2.append(0)
    elif len(polynom2) > len(polynom1):
        while len(polynom2) != len(polynom1):
            polynom1.append(0)
    for num in range(len(polynom1)):
        sumNum = polynom1[num] + polynom2[num]
        sum.append(sumNum)
    while sum[num] == 0:
        del sum[num]
        num=-1
    return sum



def polyMultiply(poly1,poly2):
    answer = []
    while len(answer) != ((len(poly1) + len(poly2)) - 1 ):
        answer.append(0)
    for x in range(len(poly1)):
        for y in range(len(poly2)):
            answer[x+y] += poly1[x] * poly2[y]
    return answer


#[2, 4, 11, -5, -9, -35]








polynom1 = [1, 2, 5]
polynom2 = [2, 0, 1, -7]
print(polyMultiply(polynom1,polynom2))
