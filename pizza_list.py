# the code below:
toppings = ["pepperoni", "pineapple", "cheese", "sausage", "olives", "anchovies", "mushrooms"]
prices = [2, 6, 1, 3, 2, 7, 2]

num_two_dollar_slices = prices.count(2)
#length of toppings
num_pizzas = len(toppings)

#new 2D list
pizza_and_prices = [
  [2, "pepperoni"],
  [6, "pineapple"],
  [1, "cheese"],
  [3, "sausage"],
  [2, "olives"],
  [7, "anchovies"],
  [2, "mushrooms"]
]

#sort the elements
pizza_and_prices.sort()
# cheapest price
cheapest_pizza = pizza_and_prices[0]
# highest price
priciest_pizza = pizza_and_prices[-1]
# remove the last element
pizza_and_prices.pop(-1)
# add new element
pizza_and_prices.insert(2, "peppers")
#
three_cheapest = pizza_and_prices[:3]

print(three_cheapest)
#print("We sell " + str(num_pizzas) + " different kind of pizza!")
