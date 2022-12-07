def sum(L):
    totalSum = 0
    if len(L) > 0:
        for x in range(len(L)):
            totalSum = totalSum + L[x]

        return totalSum
    else:
        return 0

def listToInteger(L):
    if len(L) > 0:
        strings = [str(integer) for integer in L]
        concatString = "".join(strings)
        finalInt = int(concatString)
        return finalInt
    else:
        return 0


def solution(L):
    num = sum(L)
    if not num % 3:
        L.sort(reverse=True)
        return listToInteger(L)
    else:
        n = num % 3
        flag = False
    while not flag:
        if n in L:
            L.remove(n)
            L.sort(reverse=True)
            return listToInteger(L)
        elif (n > num):
            k = []
            for i in L:
                if i % 3 == 0:
                    k.append(i)
            if len(k) != 0:
                k.sort(reverse=True)
                return listToInteger(k)
            else:
                return 0

        else:
            n += 3

l = [8, 5, 3]
l2 = []
l3 = ['zero']
print(solution(l3))