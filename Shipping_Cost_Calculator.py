# Shipping Cost Calculator

## Input package weight and shipping rate
weight = float(input("Enter the package weight in kilograms: "))
rate = float(input("Enter the shopping rate per kilogram: "))

## Calculate shopping cost
shopping_cost = weight * rate

## Display the result
print(f"Shipping Cost: {shopping_cost} USD")
