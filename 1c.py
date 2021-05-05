# ask list from the user
import sys
numbers = [int(numbers) for numbers in input("list:").split(",")]

# using min(), max(), sum()
x = "minimum", min(numbers), "maximum", max(numbers), "mean", sum(numbers)/len(numbers)
sys.stdout.write(str(x))
