def sort_by_age(lst):
    # Sort the list of tuples by the second element (age) in each tuple
    # The 'key' argument specifies a function to extract the sorting key from each tuple
    # The lambda function takes a tuple 'x' and returns the second element (age) for sorting
    return sorted(lst, key=lambda x: x[1])
# an implementation of the sort function to extract the sorting key from each tuple
# Create a list of tuples with names and ages
people = [("Peshy", 22), ("John", 32), ("Liam", 1)]

# Apply the sort_by_age function to sort by age
sorted_people = sort_by_age(people)

# Print the sorted list of tuples
print(sorted_people)  
