def merge_dicts(dict1, dict2):
    # Create a new dictionary to store the merged result
    merged_dict = dict1.copy()  # Start with a copy of the first dictionary
    
    # Update the new dictionary with items from the second dictionary
    for key, value in dict2.items():
        if key in merged_dict:
            # Sum the values if the key is already in the merged dictionary
            merged_dict[key] += value
        else:
            # Otherwise, add the key-value pair from the second dictionary
            merged_dict[key] = value
    
    return merged_dict

#  an Example of merging
dict1 = {'a': 10, 'b': 20, 'c': 30}
dict2 = {'b': 45, 'c': 55, 'd': 40}
merged = merge_dicts(dict1, dict2)
print(merged)  
