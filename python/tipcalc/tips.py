# Tips Calculator

bill = float(input ("Enter the total amount of the bill: \n"))
tip = float(input ("Enter the percentage of tip you would like to give: \n"))
import random
import math

totaltip = round((tip / 100) * bill,2)
totalbill = round(totaltip + bill,2)

print(f"The total tip amount is ${totaltip}, and the total bill is ${totalbill}")

decision = input(" Would you like to divide the bill with others? \n").lower()

if decision =="yes":
  people = int(input("How many people are in the group? \n"))
  billsplit = round(totalbill / people, 2)
  print(f"Each person should pay ${billsplit} ")

else:
  print("Have a nice day")
