# Counting number of times the string 'bob' program.
#
# Riky Lutfi Hamzah
# rilutham@gmail.com
# http://rikylutfihamzah.com 
#

# Array of characters.
s = 'bobazcbobobobegghakl'

# Initialize number of times the string 'bob' occurs in s.
num_of_bobs = 0

# Count the number of times the string 'bob' occurs in s.
for i in range(1, len(s) - 1):
    if s[i-1 : i+2] == 'bob':
        num_of_bobs += 1

# Print the number of times the string 'bob' occurs in s.
print 'Number of times bob occurs is: %d' % num_of_bobs