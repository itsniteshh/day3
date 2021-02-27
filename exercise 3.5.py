# 🚨 Don't change the code below 👇
print("Welcome to the Love Calculator!")
name1 = input("What is your name? \n").lower()
name2 = input("What is their name? \n").lower()
# 🚨 Don't change the code above 👆

#Write your code below this line 👇

names = name1 + name2

t = names.count("t")
r = names.count("r")
u = names.count("u")
e = names.count("e")
compatibility1 = t+r+u+e

l = names.count("l")
o = names.count("o")
v = names.count("v")
e = names.count("e")
compatibility2 = l+o+v+e

print(str(compatibility1) + str(compatibility2))