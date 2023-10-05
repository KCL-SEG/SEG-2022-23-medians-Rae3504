"""Median calculator."""
"""ENTER YOUR SOLUTION HERE! Test"""

while True:
    try:
        print("Enter a list of numbers separated by commas: ")
        numbers = sorted([float(value) for value in input().split(",")])
    except ValueError:
        print("Some input could not be converted to a number!")
    else:
        break

lenhalf = len(numbers)/2
midindex = int(lenhalf) + (lenhalf % 1 > 0)
if len(numbers) % 2 == 0:
	print((numbers[midindex] + numbers[midindex - 1]) / 2)
else:
	print(numbers[midindex - 1])
