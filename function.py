QUESTION 1
def calculate_discount(price, discount_percent):
#check if the discount is 20% or more
    if discount_percent >= 20:
        #calculate the discount amount
        discount_amount = price * (discount_percent / 100)
        #calculate the final price after discount
        final_price = price - discount_amount
        return final_price
    else:
        #if the discount is less than 20%, return the original price
        return price
    
    Question 2
    #Prompt the user for the price and discount percentage
price = float(input("Enter the price of the item: "))
discount_percent = float(input("Enter the discount percentage: "))
#Call the function to calculate the final price
final_price = calculate_discount(price, discount_percent)
#Print the final price or the original price if no discount is applied
if final_price == price:
    print(f"No discount applied. The price is: ${price:.2f}")
else:
    print(f"The final price after discount is: ${final_price:.2f}")
#End of code 
