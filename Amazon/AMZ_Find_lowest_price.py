"""
An Amazon seller is celebrating ten years in business! They are having a sale to honor their privileged members, those who have purchased from them in the past five years. These members receive the best discounts indicated by any discount tags attached to the product. Determine the minimum cost to purchase all products listed. As each potential price is calculated, round it to the nearest integer before adding it to the total. Return the cost to purchase all items as an integer.
There are three types of discount tags:
Type O: discounted price, the item is sold for a given price.
Type 1: percentage discount, the customer is given a fixed percentage discount from the retail price.
Type 2: fixed discount, the customer is given a fixed amount off from the retail price.

Example
products = [['10', 'd0', 'd1'], ['15', 'EMPTY', 'EMPTYI', ['20', 'd1',
'EMPTY'I]
discounts = [I'dO','1',27'], ['d1' '21', '5']]

The products array elements are in the form ['price', 'tag 1', 'tag 2', ..., 'tag m-1']. There may be zero or more discount codes associated with a product. Discount tags in the products array may be 'EMPTY' which is the same as a null value. The discounts array elements are in the form ['tag', type', amount].

If a privileged member buys product 1 listed at a price of 10 with two discounts available:
-> Under discount do of type 1, the discounted price is 10 - 10 * 0.27 = 7.30, round to 7.
-> Under discount d1 of type 2, the discounted price is 10 - 5 = 5.
-> The price to purchase the product 1 is the lowest of the two, or 5 in this case
The second product is priced at 15 because there are no discounts available
The third product is priced at 20. Using discount tag d1 of type 2, the discounted price is 20 - 5 = 15
The total price to purchase the three items is 5 + 15 + 15 = 35.

Notes: Not all items will have the maximum number of tags. Empty tags may just not exist in input, or they may be filled with the string EMPTY. These are equivalent as demonstrated in the example above.
Function Description
Complete the function findLowestPrice in the editor below.
findLowestPrice has the following parameter(s):
[string] products[nilm]: a 2D array of product descriptors as
strings: price followed by up to m-7 discount tags
[string] discounts{di[3]: a 2D array of tag descriptors as strings:
tag, type, amount
Returns:
int: the total amount paid for all listed products, discounted to privileged members' pricing

Constraints
• 1 = n. m. d=1000
"""


class Discount():
    def __init__(self, d_type, amount):
        self.d_type = d_type
        self.amount = amount

def minProfit(products, discounts):
    hash_map = {}
    for discount in discounts:
        hash_map[discount[0]] = Discount(int(discount[1]), int(discount[2]))
    total = 0
    for product in products:
        for i in range(1, len(product)):
            if product[i] != None and product[i] != 'EMPTY' and product[i] in hash_map:
                # Calculate the price
                total += min(int(product[0]), calculate_price(int(product[0]), hash_map[product[i]]))
    return total 

def calculate_price(price, discount_obj):
    discounted_price = 0
    if discount_obj.d_type == 0:
        discounted_price = discount_obj.amount
    elif discount_obj.d_type == 1:
        discounted_price = round((100 - discount_obj.amount) * price / 100)
    elif discount_obj.d_type == 2:
        discounted_price = price - discount_obj.amount
    else:
        print("Err")
    return discounted_price

prod=[['10','sale','january-sale'],['200','sale','EMPTY']]
disc=[['sale','0','10'],['january-sale','1','10']]
print(minProfit(prod,disc))
