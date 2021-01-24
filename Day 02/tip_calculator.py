'''Calculate how much should each person pay of the total bill'''
'''
#If the bill was $150.00, split between 5 people, with 12% tip.
#Each person should pay (150.00 / 5) * 1.12 = 33.6
#Format the result to 2 decimal places = 33.60
#Tip: There are 2 ways to round a number. You might have to do some Googling to solve this.💪
#HINT 1: https://www.google.com/search?q=how+to+round+number+to+2+decimal+places+python&oq=how+to+round+number+to+2+decimal
#HINT 2: https://www.kite.com/python/answers/how-to-limit-a-float-to-two-decimal-places-in-python
'''
bill = float(input('What is the total amount of the bill?\n'))
tip = int(input('What is the tax (ex: 12% please enter 12)?\n'))
tip_decimal = tip / 100
people = int(input('How many people?\n'))
total_amount = bill + (bill * tip_decimal)
amount_per_person = total_amount / people
print(f'The amount each people needs to pay is ${amount_per_person}.')


