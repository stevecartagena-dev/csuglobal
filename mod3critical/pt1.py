
# Online Python - IDE, Editor, Compiler, Interpreter

print('I can calculate the total amount of your resturant bill')
print('Please input your food charge and I will take care of the rest')
food = float(input()) #added float to make sure decimals are included
tip = food * 0.18
tax = food * 0.07
total = food + tip + tax
print('Here is the total amount of your restaurant bill')
print('${:.2f} Food Charge'.format(food)) #used :.2f format for readability
print('${:.2f} Tip (18%)'.format(tip))
print('${:.2f} Tax (7%)'.format(tax))
print('${:.2f} Total Charge'.format(total))