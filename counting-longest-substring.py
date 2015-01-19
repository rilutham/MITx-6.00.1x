# Counting the longest substring of a string.
#
# Riky Lutfi Hamzah
# rilutham@gmail.com
# http://rikylutfihamzah.com 
#

# Array of characters.
s = 'pneumonoultramicroscopicsilicovolcanoconiosis'

# Assign the first character of s to temp and result list.
temp = s[0]
result = s[0]

# Count the longest substring of s
for i in range(1, len(s)):
    if s[i] >= temp[-1]:
        temp += s[i]
        if len(temp) > len(result):
            result = temp
    else:
        temp = s[i]

# Print the longest substring of s
print 'Longest substring in alphabetical order is:', result