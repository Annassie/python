### Task_2_5

# Create a list containing product prices (10-20 products). Exmaple [45.3, 9.4, 97, 103,5]

# Display these prices as line/string, separated by common
# The price should be displayed as <euros> euros <cents> (fro example 9 euros 40 cents)
# Think about how to get euros and cents from the price, how to add zero, if for example it turned out 5 cents or 0 cents
# (it should be 05 cents or 00 centes)
# Display prices sorted in ascending order, do not create a new list
# Create a new list containing the same prices, but sorted in descending order
# Display prices of the five most expensive items.
# Is it possible to display the prices of these products in ascending order with a minimum of code


# Creating a list

prices = [57.8, 46.51, 97, 103.56, 9.7, 10.1, 21.99, 150.6, 88.5, 35.6, 83.2]
print(prices, id(prices))

# A. Display these prices as line/string, separated by common
all_prices = []

for element in prices:
    formatted_prices = "{:,.2f}".format(element)
    del_dot = formatted_prices.replace('.', ' euros ')
    all_prices.append(str(del_dot) + ' cents')
    all_products = ', '.join(all_prices)
print(all_products)


# B. Display prices sorted in ascending order, do not create a new list
prices.sort()
print(prices, id(prices))

# C. Create a new list containing the same prices, but sorted in descending order

new_prices = sorted(prices, reverse=True)
print(new_prices, id(new_prices))

# D. Display prices of the five most expensive items.
# Is it possible to display the prices of these products in ascending order with a minimum of code

print(sorted(new_prices[:5]))
