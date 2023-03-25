import time
menu = ["Sushi","Fish fry","Chillie Chicken","Sweet corn soup","Baby Corn Munchuria","Tandoori","Dum Biryani","Hydrabadi Biryani"]
print("Sir, Please choose a item from this menu shown below:")
for i in range(len(menu)):
    print(f"{i+1}. {menu[i]}")
order = int(input("Your order Please : "))
print(f"Your {menu[order-1]} will be ready, with in few seconds")
time.sleep(4)
print("")
print(f"You order {menu[order-1]} is here\nEnjoy the food sir")
