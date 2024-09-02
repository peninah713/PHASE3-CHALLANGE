def decorator_func(func):
    # Define the decorator function
    def wrapper(*args, **kwargs):
        # Print message before calling the original function
        print("Decorator Applied")
        # Call the original function with its arguments
        return func(*args, **kwargs)
    return wrapper

def apply_decorator(func):
    # Apply the decorator to the function
    return decorator_func(func)
# an example for the implementation of the decorator
@apply_decorator
def say_greetings(name):
    print(f"Hello, {name}!")

# Call the decorated function
say_greetings("peshys")
