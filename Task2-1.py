# Create a class named Cypher. The purpose of that class is to receive an input string of characters and convert it to another cypher string. Use a constructor to receive the input. You can also read the input from user, But don't use input() inside the constructor.
# The class must have a class method to do the string conversion. And an instance method to invoke the classmethod from within it.
# Use the below conversion logic:
# • Iterate over each character in the string, and if the character is a digit increment it by one (0->1, 1- >2,9 should be replaced with 0)
# if the character is an alphabet then shift the character by 2 positions (use chr() and ord() built-ins for this) (a->c, b->d,...y->a, z->b) If the character is in upper case convert it to lower and vice versa The returned string must be of same length as the input.
# No need to implement the reversing algorithm but will be a plus if avallable.
# 1) create an object for the Cypher class with the string.


class Cypher:
    def __init__(self, input_string):
        self.input_string = input_string
    
    @classmethod
    def convert_string(cls, input_str):
        result = ""
        for char in input_str:
            if char.isdigit():
                result += str((int(char) + 1) % 10)
            elif char.isalpha():
                shift = 2
                if char.islower():
                    result += chr((ord(char) - ord('a' if char.islower() else 'A') + shift) % 26 + ord('a'))
                else:
                    result += chr((ord(char) - ord('A') + shift) % 26 + ord('A')).lower()
            else:
                result += char
        return result

    def invoke_conversion(self):
        return self.convert_string(self.input_string)

# Example usage
input_string = "Beinex.com123"
cypher_instance = Cypher(input_string)
result = cypher_instance.invoke_conversion()
print(f"Original String: {input_string}")
print(f"Cypher String: {result}")
