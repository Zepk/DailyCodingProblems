'''
This problem was asked by Facebook.

Given the mapping a = 1, b = 2, ... z = 26, and an encoded message, count the number of ways it can be decoded.

For example, the message '111' would give 3, since it could be decoded as 'aaa', 'ka', and 'ak'.

You can assume that the messages are decodable. For example, '001' is not allowed.
'''


def count_decode(string):
    count = len(string)
    ones = 0
    zeros = 0
    for i in range(len(string)):
        if i < len(string)-1 and string[i] == '2' and int(string[i+1]) <= 6:
            count += 1
        elif string[i] == '1':
            ones += 1
        elif string[i] == '0':
            zeros += 1
    if string[-1] == '1':
        ones -= 1
    count += ones - zeros
    return count


a = '123456789101112'
b = '1234567891011'
c = '1111112'

print(count_decode(a))
print(count_decode(b))
print(count_decode(c))
