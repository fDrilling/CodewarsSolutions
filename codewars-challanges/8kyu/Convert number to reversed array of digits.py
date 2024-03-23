# Given a random non-negative number, you have to return 
# the digits of this number within an array in reverse order.

# Example(Input => Output):
# 35231 => [1,3,2,5,3]
# 0 => [0]


# My solution
def digitize(n):
    list = []
    for i in str(n):
        list.append(int(i))
    list.reverse()   
    return list