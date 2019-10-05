def sortNumbers(list,string):
    if string == 'ASC' :
        list.sort()
        return list
    elif string == 'DESC':
        list.sort()
        l = list[::-1]
        return l


def sortData(reputation,manufactures,string):
    if (len(reputation)!=len(manufactures)):
        raise ValueError('Invalid input data')
    if string == 'ASC':
        for x in range(len(reputation)):
            for y in range(len(reputation) - 1):
                if reputation[y] > reputation[y+1]:
                    element = reputation[y]
                    SecElement = manufactures[y]
                    manufactures[y] = manufactures[y+1]
                    reputation[y] = reputation[y+1]
                    manufactures[y+1] = SecElement
                    reputation[y+1] = element
        answer = manufactures
        return answer
    elif string == 'DESC':
        for x in range(len(reputation)):
            for y in range(len(reputation) - 1):
                if reputation[y] < reputation[y+1]:
                    element = reputation[y]
                    SecElement = manufactures[y]
                    manufactures[y] = manufactures[y+1]
                    reputation[y] = reputation[y+1]
                    manufactures[y+1] = SecElement
                    reputation[y+1] = element
        answer = manufactures
        return answer






list = [1,1,1,1,1,1,1,2]
list2 = ['Praha', 'Brno', 'Pariz', 'Londyn', 'Bratislava', 'Pelhrimov', 'Jihlava', 'CB']
string = 'DESC'
print(sortData(list,list2,string))