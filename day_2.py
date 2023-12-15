print ("Please enter the current weather conditions")
print ("Enter the temperature")
temperature=int(input ())
print ("Is it raining (yes or no)")
rain=input()
if temperature <50:
    print("You should wear a coat, hat, scarf, and gloves")
elif temperature >=50 and temperature<70 and rain=="yes":
    print ("You should wear a rain jacket and boots")
elif temperature >=50 and temperature<70 and rain=="no":
    print("You should wear a sweater or light jacket")
elif temperature > 70 and rain=="yes":
    print ("You should wear a light jacket and rain boots")
elif temperature >70 and rain=="no":
    print("You should wear a t-shirt and shorts")   
else: print("invalid input")

