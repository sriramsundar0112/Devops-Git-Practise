# Discount - Check - Python script

print("D-Mart Super Market - Bill")
print("Let's Check if you are applicable for a discount")
total_bill=int(input("Enter the total value of the bill :"))
if(total_bill>1000):
    print("You are applicable for a 10% Discount on the total Bill")
    print(f"Discounted Amount is {total_bill*0.10}")
    print(f"Final Bill post discount is {total_bill-(total_bill*0.1)}")
else:
    print("No discount")