def fibonacci_sequence(fibonacci_start, fibonacci_next, fibonacci_nth):
# This is a function of the sequence where fibonacci_start is the initial value of the sequence, fibonacci_next is
# the next number to be added to fibonacci_start, and fibonacci_nth determines how many values in the sequence will
# be printed.
    
    fibonacci_even_values = [] # Creates an empty list to store all even values under 4000000.
    
    for i in range(fibonacci_nth): # Prints nth number of values in the fibonacci sequence determined by fibonacci_nth.
        
        fibonacci_num = fibonacci_start + fibonacci_next # fibonacci_num is the value to be printed.
        
        if((fibonacci_num < 4000000) & ((fibonacci_num%2) == 0)): # If the value is < 4000000 and even.
            fibonacci_even_values.append(fibonacci_num) # Adds value to the end of the list.
            
        fibonacci_start = fibonacci_next # Reassigns the new initital value as the previous "next" value to be added in the next iteration.
        fibonacci_next = fibonacci_num # The "next" value to be added in the next iteration becomes the previous fibonacci value.
    
    print("All even values under 4,000,000 of the fibonacci sequence are: " + str(fibonacci_even_values)) # Prints the list of even numbers.
    print("\nThe sum of all even values under 4,000,000 is equal to: " + str(sum(fibonacci_even_values))) # Prints the sum of all values in the list. 
    
fibonacci_sequence(0, 1, 100)
# fibonacci_start MUST be 0 because it will be added with fibonacci_next to print the first fibonacci value, 1.
# fibonacci_next MUST be 1 because (fibonacci_nth = 0) + 1 = first value =  1. 
# These values change in the function.
# fibonacci_nth is an arbitrary value.
