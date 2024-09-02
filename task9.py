class Car:
    # Default values for the car attributes
    make = ""   # The make of the car (e.g., Toyota, Honda)
    model = ""  # The model of the car (e.g., Corolla, Civic)
    year = 0    # The manufacturing year of the car

    def display_info(self):
        # Print out the car's information
        print(f"Make: {self.make}")   # Display the make of the car
        print(f"Model: {self.model}") # Display the model of the car
        print(f"Year: {self.year}")   # Display the year of the car

