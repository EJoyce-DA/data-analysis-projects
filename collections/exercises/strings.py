# ---- Exercise 2: Bracket Notation Basics ----

text = 'Strings_are_sequences_of_characters.'
word = 'tomato'

# 1. Print a slice of the first 12 characters from 'text'.
slice_1 = text[:12]
print(slice_1)

# 2. Print a slice of the last 12 characters from 'text'. You should NOT have to count the index values yourself!
slice_2 = text[-12:]
print(slice_2)

# 3. Print a slice of the middle 12 characters from 'text'.
slice_3 = text[12:24]
print(slice_3)


# ---- Exercise 3: Looping Through a String ----

# Use index values to loop backwards through 'word'.

# 1. Print 1 letter per line.
word_index = len(word)-1
for i in range(word_index, -1, -1):
    print(word[i])

# 2. Refactor the code to use the accumulator pattern to build up and print the reversed string. For example, if given 'good', print 'doog' on one line.
word_backwards = ''
for i in range(word_index, -1, -1):
    word_backwards += word[i]
print(word_backwards)

# 3. Refactor the code to print a combination of the original and reversed string. For example, given 'tomato', print 'tomatootamot'. (If you want to be fancy, print 'tomato | otamot').
word_combo = word + ' | ' + word_backwards
print(word_combo)