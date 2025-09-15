# Function that creates a message 
def create_message(prefix, *args):
    s = str(prefix) + ': '
    for arg in args:
        s += str(arg) + ' '
    print(s)

def create_message(*args, **kwargs):
    # Find the key in kwargs 
    separator = kwargs.get("separator", " ")
    s = ' '
    for arg in args:
        s += str(arg) + separator 

    return s[:-1]

# Create a function 
create_message("Status", "Temp", 25, "Degree")
create_message("Alert", "System","is" "Online")

create_message("a", "b", separator = '-')