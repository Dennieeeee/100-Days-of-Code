# 🚨 Don't change the code below 👇
student_heights = input("Input a list of student heights ").split()
for n in range(0, len(student_heights)):
  student_heights[n] = int(student_heights[n])
# 🚨 Don't change the code above 👆


#Write your code below this row 👇
'''total = 0
for i in student_heights:
    total += i
print(f'The average height is {round(total/len(student_heights),2)}')
'''
'''without using the len() function'''
total = 0
for i in student_heights:
    total += i

count = 0
for i in student_heights:
    count += 1
avg = round(total/count)
print(f'The average height is {avg}.')
