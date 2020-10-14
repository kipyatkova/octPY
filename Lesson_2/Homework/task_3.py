import math
import simpleeval

expression = input("Enter the expression: ")

result = simpleeval.simple_eval(expression, names={"pi": math.pi, "e": math.e})

print(f"Result is {result}")
