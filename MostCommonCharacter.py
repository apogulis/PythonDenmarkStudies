# This program checks what is the most common character
# used in the string

def main():
    # Imported Module
    import collections
    # User enters string
    user_string = input('Enter a string:')
    # Using the Counter from imported module to count characters
    print(collections.Counter(user_string).most_common(1)[0])


# Calling the main function
main()
