# 🚨 Don't change the code below 👇
print("Welcome to Python Pizza Deliveries!")
size = input("What size pizza do you want? S, M, or L:  ")
add_pepperoni = input("Do you want pepperoni? Y or N:  ")
extra_cheese = input("Do you want extra cheese? Y or N:  ")
# 🚨 Don't change the code above 👆

#Write your code below this line 👇

if size == "S":
  
  if add_pepperoni == "Y":
    if extra_cheese == "Y":
      print("your total bill amount is $18")
    else:
      print("your total bill amount is $17")
  else:
    print("\nyour total bill amount is $15")

elif size == "M":

  if add_pepperoni == "Y":
    if extra_cheese == "Y":
      print("your total bill amount is $24")
    else:
      print("your total bill amount is $23")
  else:
    print("\nyour total bill amount is $20")

else:

  if add_pepperoni == "Y":
    if extra_cheese == "Y":
      print("your total bill amount is $29")
    else:
      print("your total bill amount is $28")
  else:
    print("\nyour total bill amount is $25") 

print("We are happy to serve you")
