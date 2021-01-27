'''Pick a person at random'''
# Split string method
#names_string = input("Give me everybody's names, separated by a comma. ")

names_string = 'Tom, Jerry, Aple, Peach'
names = names_string.split(", ")
# 🚨 Don't change the code above 👆

#Write your code below this line 👇
import random
print(random.choice(names))

'''without using the choice(), use len() instead'''
name_length = len(names)
x = random.randint(0,name_length-1)
print(names[x])