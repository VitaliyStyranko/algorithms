
# 1. Compute the sum of digits in all numbers from 1 to n. When a function gets a number n,
# find the sum of digits in all numbers from 1 to n.

def sum_of_digits(n):
    result = 0
    for i in range(1, n + 1):
        result += i
    return result

n = 5
result = sum_of_digits(n)
print(f"Result = {result}")


# 2. Find max number from 3 values.

a = 5
b = 45
c = 68

if a > b and a > c:
    max_number = a
elif b > c:
    max_number = b
else:
    max_number = c

print(f"Result = {max_number}")


#  3. Count odd and even digits of the whole number.

def count_odd_even_numbers(num):
  if type(num) == int:
    arr = str(num)

    result = {
      'odd': 0,
      'even': 0
    }

    for number in arr:
      if int(number) % 2 == 0:
        result['even'] += 1
      else:
        result['odd'] += 1

    print(result)
  else
    print(False)

count_odd_even_numbers(94777678123)
