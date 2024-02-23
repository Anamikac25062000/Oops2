# 2)call the instance method, which should internally call the classmethod you prepared for the conversion, pass the string data to classmethod and do the conversion.
# No need to consider special characters for now.
# Expected output for the string "ABCD1293Z" is "cdEf23046"


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
                    result += chr((ord(char) - ord('a') + shift) % 26 + ord('a'))
                else:
                    result += chr((ord(char) - ord('A') + shift) % 26 + ord('A')).lower()
            else:
                result += char
        return result

    def invoke_conversion(self):
        return self.convert_string(self.input_string)

# Example usage
input_string = "Beinex1234"
cypher_instance = Cypher(input_string)
result = cypher_instance.invoke_conversion()
print(f"Original String: {input_string}")
print(f"Cypher String: {result}")
