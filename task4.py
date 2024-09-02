def count_vowels(text):
    # Vowels to check against (both lowercase and uppercase)
    vowels = "aeiouAEIOU"
    
    # Counter for vowels
    count = 0
    
    # Loop through each character in the text
    for char in text:
        # If the character is a vowel, increase the count
        if char in vowels:
            count += 1
    
    # Return the final count of vowels
    return count
