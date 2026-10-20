# Electricity Bill Calculator
RATE = 12.90

# Validate name input

while True:
    name = input("Enter customer name: ")
    
    if name.strip() != "":
        if name.isdigit():
            print("There's a name that's all numbers? Enter a VALID name.")
        else:
            break 
    else:
        print("There is no one in this world without a name. Please enter one.")

# Validate previous rate
while True:
    try:
        previous = float(input("Enter previous meter reading: "))
        
        if previous < 0:
            print("Please enter a NON-NEGATIVE rate. At least zero.")
        else:
            break
    except:
        print("Not even a valid one.")

# Validate current rate

while True:
    try:
        current = float(input("Enter current meter reading: "))
        
        if current <= previous:
            print("Please enter a rate higher or equal to the previous rate.")
        else:
            break
    except:
        print("Not even a valid one.")

consumption = current - previous

total_bill = consumption * RATE

print("\nCustomer:", name)
print("Electricity Consumption:", consumption, "kWh")
print("Total Bill: PHP", round(total_bill, 2))

# Validation rules
# 1. Customer name -- Must not be empty
# 2. Previous reading -- Number at least 0
# 3. Current reading -- Number at least the previous reading
