total = 0
for i in range(0,101,2):
    total += i
print(f'The sum of even numbers is {total}.')

sum = 0
for i in range(0,101):
    if i%2 == 0:
        sum += i
print(f'The sum of even numbers is {sum}.')