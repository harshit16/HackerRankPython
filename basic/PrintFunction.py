"""Problem statement"""

# https://www.hackerrank.com/challenges/python-print/problem


def print_number(n):
    if n <= 0:
        print("Incorrect Input!")
    elif n == 1:
        print(n)
    else:
        i = 1
        while i <= n:
            print(i, end='')
            i += 1


if __name__ == '__main__':
    print("Enter the number: ")
    n = int(input())
    print_number(n)
