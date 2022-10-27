
# 1. Split in Half
# Given a string. Split it into two equal parts. Swap these parts and return the result.
# If the string has odd characters, the first part should be one character greater than the second part.
# Example: string = 'bbbbbcaaaaa'. Result = ‘aaaaabbbbbc’.


string = "bbbbbcaaaaa"
print("The original string is : " + string)

first_parts = string[:len(string)//2 + 1]
print(first_parts)

second_parts = string[:len(string)//2: - 1]
print(second_parts)

new_string = second_parts + first_parts
print(new_string)



# 2. Unique Characters in String
# Given a string, determine if it consists of all unique characters.
# For example, the string 'abcde' has all unique characters and should return True.
# The string 'aabcde' contains duplicate characters and should return False.


def check_unique(string):
  for i in range(len(string)):
    for j in range(i + 1, len(string)):
      if(string[i] == string[j]):
        return False
    return True


string = 'aabcde'
print(check_unique(string))
string = 'abcde'
print(check_unique(string))