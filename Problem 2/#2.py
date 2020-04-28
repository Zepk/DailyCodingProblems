'''
This problem was asked by Uber.

Given an array of integers, return a new array such that each element at index i of the new array is the product of all the numbers in the original array except the one at i.

For example, if our input was [1, 2, 3, 4, 5], the expected output would be [120, 60, 40, 30, 24]. If our input was [3, 2, 1], the expected output would be [2, 3, 6].

Follow-up: what if you can't use division?
'''

# With Division
def solver(thislist):
    mult = 1
    endlist = []
    for number in thislist:
        mult *= number
    for number in thislist:
        endlist.append(int(mult/number))
    return endlist

#Without Division
print(solver([1,2,3,4,5]))

def solver2(thislist):
    endlist = []
    normaldict = {}
    reversedict = {}
    mult = 1
    for number in range(len(thislist)):
        mult *= thislist[number]
        normaldict.update({number:mult})
    mult = 1
    for number in reversed(range(len(thislist))):
        mult *= thislist[number]
        reversedict.update({number: mult})

    for i in range(len(thislist)):
        primero = 1
        segundo = 1
        if i-1 in normaldict:
            primero = normaldict[i-1]
        if i+1 in reversedict:
            segundo = reversedict[i+1]
        endlist.append(primero*segundo)
    return endlist

print(solver2([1,2,3,4,5]))