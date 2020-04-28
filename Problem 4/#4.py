'''
This problem was asked by Stripe.

Given an array of integers, find the first missing positive integer in linear time and constant space.
In other words, find the lowest positive integer that does not exist in the array. The array can contain duplicates and negative numbers as well.

For example, the input [3, 4, -1, 1] should give 2. The input [1, 2, 0] should give 3.

You can modify the input array in-place.
'''

#hard4me
def solver(thislist):
    thisbool = True
    for number in range(len(thislist)):
        while thisbool:
            thislist, thisbool = swap(thislist, number)
        thisbool = True
    for number in range(len(thislist)):
        if number+1 != thislist[number]:
            return number+1
    return len(thislist)

def swap(thislist, number):
    if thislist[number] != number + 1 and thislist[number] <= len(thislist) and thislist[number] > 0:
        primero = thislist[number]
        segundo = thislist[thislist[number] - 1]
        thislist[thislist[number] - 1] = primero
        thislist[number] = segundo
        return thislist, True
    return thislist, False


print(solver([3, 4, -1, 1]))
print(solver([1,2,0]))
