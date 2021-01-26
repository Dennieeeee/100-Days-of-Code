# Problem 1
'''Check even or odd number'''
# 🚨 Don't change the code below 👇
#number = int(input("Which number do you want to check? "))
number = 90
# 🚨 Don't change the code above 👆

#Write your code below this line 👇
if number % 2 == 0:
    print("It's an even number.")
else:
    print("It's an odd number.")

##########################################################################
##########################################################################
# Problem 2
'''
venn diagram: 
https://viewer.diagrams.net/?highlight=0000ff&edit=_blank&layers=1&nav=1&title=Rollercoaster%202#Uhttps%3A%2F%2Fdrive.google.com%2Fuc%3Fid%3D1J7_rw1flGeF0hmc_zrMzPX7t6xkbcsiX%26export%3Ddownload
'''
'''Rollercoaster Admission Ticket'''
print("Welcome to the rollercoaster!")
height = int(input("What is your height in cm? "))
bill = 0

if height >= 120:
    print("You can ride the rollercoaster!")
    age = int(input("What is your age? "))
    if age < 12:
        bill = 5
        print("Child tickets are $5.")
    elif age <= 18:
        bill = 7
        print("Youth tickets are $7.")
    elif age >= 45 and age <= 55:
        print("Everything is going to be ok. Have a free ride on us!")
    else:
        bill = 12
        print("Adult tickets are $12.")

    wants_photo = input("Do you want a photo taken? Y or N. ")
    if wants_photo == "Y":
        bill += 3

    print(f"Your final bill is ${bill}")

else:
    print("Sorry, you have to grow taller before you can ride.")
