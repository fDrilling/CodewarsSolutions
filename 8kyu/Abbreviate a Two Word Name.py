# Write a function to convert a name into initials. 
# This kata strictly takes two words with one space in between them.

# The output should be two capital letters with a dot separating them.

# It should look like this:

# Sam Harris => S.H

# patrick feeney => P.F



# My solution

def abbrev_name(name):
    list = name.rsplit()
    print(list)
    return str.upper(list[0][0])+'.'+str.upper(list[1][0])