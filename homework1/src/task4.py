#Duck typing is the functionality of a language where "if it looks like a duck and quacks like a duck,
#you might as well treat it like a duck." This is quite common in interpreted languages. Create a
#new file named task4.py that calculates the final price of a product after applying a given discount
#percentage inside of a function named calculate_discount. The function should accept any numeric
#type for price and discount.

def calculate_discount(price, discount):
    try:
        final_price = price * (1 - discount / 100)
        return final_price
    except TypeError:
        print("Error: Price and discount must be numeric types.")
        return None
