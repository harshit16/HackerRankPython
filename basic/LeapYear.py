# LinkToProblem
# https://www.hackerrank.com/challenges/write-a-function/problem


def is_leap(year):

    leap = False

    if (year % 4 == 0) & (year % 100 != 0 )|( year % 400 == 0):
        leap = True

    return leap


print("Enter the year")
year = int( input())
print(is_leap(year))
