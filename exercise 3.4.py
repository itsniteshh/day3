# 🚨 Don't change the code below 👇
print("Welcome to Python Pizza Deliveries!")
size = input("What size pizza do you want? S, M, or L:  ")
add_pepperoni = input("Do you want pepperoni? Y or N:  ")
extra_cheese = input("Do you want extra cheese? Y or N:  ")
# 🚨 Don't change the code above 👆

#Write your code below this line 👇

if size == "S":
  print("small pizza costs $15")

  want_pepperoni = input("Do you want pepperoni? Y or N: ")
  if want_pepperoni == "Y":
    want_cheese = input("Do you want cheese? Y or N: ")
    if want_cheese == "Y":
      print("your total bill amount is $18")
    else:
      print("your total bill amount is $17")
  else:
    print("your total bill amount is $15")

elif size == "M":
  print("medium pizza is $20")

  want_pepperoni = input("Do you want pepperoni? Y or N: ")
  if want_pepperoni == "Y":
    want_cheese = input("Do you want cheese? Y or N: ")
    if want_cheese == "Y":
      print("your total bill amount is $24")
    else:
      print("your total bill amount is $23")
  else:
    print("your total bill amount is $20")

else:
  print("large pizza is $25")

  want_pepperoni = input("Do you want pepperoni? Y or N: ")
  if want_pepperoni == "Y":
    want_cheese = input("Do you want cheese? Y or N: ")
    if want_cheese == "Y":
      print("your total bill amount is $29")
    else:
      print("your total bill amount is $28")
  else:
    print("your total bill amount is $25") 

print("We are happy to serve you")
