# points                   Recursion           Iteration     

# Space efficient             No                   Yes               No stack memory is required 
# Time efficient              No                   Yes               In case of recurson system needs more time for pop and push operations
#Easy to code?                Yes                  No                Problem can be divided into similar subproblems

# def powerOftwo(n):
#     if n==0:
#         return 1
#     else:
#        power = powerOftwo(n-1)
#        return power * 2
    
# print(powerOftwo(4))


# def factorial(num):
#     if num<=1:
#         return 1
#     else:
#         return num * factorial(num-1)
# print(factorial(5))

# def isPalindrome(strng):
#     if len(strng) == 0:
#         return True
#     else:
#         if strng[0]==strng[len(strng)-1]:
#             return False
#         return isPalindrome(strng[1:-1])
    
# print(isPalindrome("malayalam"))

# def power(base,exponent):
#     if exponent==0:
#         return 1
#     return base * power(base,exponent-1)
# print(power(2,0))
# print(power(2,4))
# print(power(2,2))

# def capitalizeFirst(arr):
#     result = []
#     if len(arr) == 0:
#         return result
    
#     result.append(arr[0][0].upper() + arr[0][1:])
#     return result + capitalizeFirst(arr[1:])

# print(capitalizeFirst(["car","taco","banana"]))    

# def productOfArray(arr):
#     if len(arr) == 0:
#         return 1
#     return arr[0] * productOfArray(arr[1:])

# print(productOfArray([1,2,3]))
# print(productOfArray([1,2,3,10]))


def fib(num):
    if (num < 2) :
        return num
    return fib(num - 1) + fib(num - 2)
print(fib(4))