# Counting vowels program.
#
# Riky Lutfi Hamzah
# rilutham@gmail.com
# http://rikylutfihamzah.com 
#

# List of valid vowels.
vowel = ['a','i','u','e','o']

# Array of characters.
string = 'Today is my mother\'s birthday'

# Convert string to lowercase
lower_string = string.lower()

# Initialize number of vowel.
num_of_vowel = 0

# Count the number of vowel.
for i in lower_string:
	if i in vowel:
		num_of_vowel +=1

# Print the number of vowel.
print 'Number of vowels: %d' % num_of_vowel