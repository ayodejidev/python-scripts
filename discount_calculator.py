#Discount Calculator

discount_percentage = float(input("Enter the discount percentage %: \n"))
original_price = float(input("Enter original price of product N: \n"))

discounted_value = (original_price*discount_percentage) / (100)
discounted_price = original_price - discounted_value

print(f"Discounted Price is N{discounted_price}")