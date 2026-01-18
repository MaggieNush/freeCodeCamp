# if __name__ == '__main__':
#     n = int(input().strip())

# if n % 2 != 0:
#     print('Weird')
# if n % 2 == 0 and n in range(2, 5+1):
#     print('Not Weird')
# if n % 2 == 0 and n in range(6, 20+1):
#     print('Weird')
# if n % 2 == 0 and n > 20:
#     print('Not Weird') 

# if __name__ == '__main__':
#     a = int(input())
#     b = int(input())
#     print(a+b)
#     print(a-b)
#     print(a*b)

# """Task
# The provided code stub reads an integer, n , from STDIN. For all non-negative integers i < n, print i^2 .

# Example
# n = 3
# The list of non-negative integers that are less than n = 3 is [0,1,2] . Print the square of each number on a separate line.
# 0
# 1
# 4"""
# if __name__ == '__main__':
#     n = int(input())
#     for i in range(n):
#         print(i * i)

# def is_leap(year):
#     if year % 400 == 0:
#         return True
#     elif year % 100 == 0:
#         return False
#     elif year % 4 == 0:
#         return True
#     else:
#         return False

# year = int(input())
# print(is_leap(year))

if __name__ == '__main__':
    n = int(input())
    print(''.join(str(i) for i in range(1, n+1)))

