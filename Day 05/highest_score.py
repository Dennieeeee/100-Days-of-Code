# 🚨 Don't change the code below 👇
student_scores = input("Input a list of student scores ").split()
# this will convert the input numbers into integer
for n in range(0, len(student_scores)):
  student_scores[n] = int(student_scores[n])
print(student_scores)
# 🚨 Don't change the code above 👆

#Write your code below this row 👇
highest = 0
for i in student_scores:
    if i > highest:
        highest = i
print(f'The highest score is {highest}.')
