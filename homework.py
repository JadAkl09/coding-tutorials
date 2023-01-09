def possibilities(n):
    if n <= 2:
        return n
    return possibilities(n-2) + possibilities(n-1)
    
# print(possibilities(40))

def poss(n):
    results = [1,2]
    for i in range(n):
        results.append(results[-1] + results[-2])
    return results[-1]
    

def exposed_pos(n):
    initial_possiblities = [0,1,2]
    initial_possiblities += (n-2) * [0]
    # for i in range(n-2):
    #     initial_possiblities.append(0)
    return __pos(n, initial_possiblities)

def __pos(n, computedPossiblities):
    if computedPossiblities[n] > 0:
        return computedPossiblities[n]
    result = __pos(n-2, computedPossiblities) + __pos(n-1, computedPossiblities)
    computedPossiblities[n] = result
    return result

#print(exposed_pos(30))

# Homework 

# 1. Divisor game: start with number n, each player must choose a divisor x of n (0 < x < n) and replace n by n - x. If no move possible, you lose. Return true if you win starting from n.

def divisor(n):
    i=2
    for i in range(n):
        if n % i == 0: 
            x = int(input("Choose a divisor of n "))
            while x < 0 or x > n:
                x = int(input("Your number has to be in betwwen 0 and n "))
            n -= x
        else:
            return "The game is finished"
#divisor(23)


# 2. - Selling stocks: given an array of stock prices recorded on each day, return the max profit that can be obtained by buying on some day and selling on some future day. Eg
#     - [1,2,3,4] → 3 (buy for one, sell for 4)
#     - [3,6,1,5] → 4 (buy for 1, sell for 5)
#     - [7,5,3,2] → 0 (no profit can be made)

# 3. complete the implementation of pos using the top down approach

def square(n):
    result = []
    for i in range(n):
        result.append(i**2)
    return result

#print(square(10))

#  print([expr for expr in iterable])

#print([x**2 for x in range(10)])

#print([x**2 for x in range(10) if x % 2 == 0])

# [(0,1), (1,2), (2,3), ..., (9,10)]
print([(x,x+1) for x in range(10)])

# 1 2 3 
# 4 5 6
# 7 8 9
# [[1,2,3], [4,5,6], [7,8,9]]


# HOMEWORK
# n is a square (i.e n = x**2 for some x)
# i want an x by x matrix with values 1,2,3,4,...,n 

print([[]])