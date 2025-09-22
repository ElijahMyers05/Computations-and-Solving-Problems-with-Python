# Create a lambda function 
add = lambda x, y: x + y
# Implement subtraction, multiplication, and division
# Check the division by zero
divide = lambda x, y: x / y if y !=0 else "Error: Divison by zero!"

# Test the lambda function
# Create a list of tuples
inputs = [(10,5), (8,0), (14,6)]
for x, y in inputs:
    print(f"Inputs: (x), (y)")
    print(f"Addition: {add(x, y)}")
    print(f"Division: {divide(x, y)}")
    print()

