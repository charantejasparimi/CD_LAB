class InfixToPostfix:
    def __init__(self):
        self.precedence = {'+':1, '-':1, '*':2, '/':2, '^':3}
    
    def is_operator(self, char):
        return char in self.precedence
    
    def infix_to_postfix(self, expression):
        stack = []
        postfix = []
        
        for char in expression:
            if char.isalnum():
                postfix.append(char)
            elif char == '(':
                stack.append(char)
            elif char == ')':
                while stack and stack[-1] != '(':
                    postfix.append(stack.pop())
                stack.pop()
            elif self.is_operator(char):
                while stack and stack[-1] != '(' and self.precedence[stack[-1]] >= self.precedence[char]:
                    postfix.append(stack.pop())
                stack.append(char)
        
        while stack:
            postfix.append(stack.pop())
        
        return ''.join(postfix)

class InfixToPrefix(InfixToPostfix):
    def infix_to_prefix(self, expression):
        reversed_expression = expression[::-1]
        postfix_expression = self.infix_to_postfix(reversed_expression)
        return postfix_expression[::-1]

class InfixToThreeAddressCode(InfixToPostfix):
    def __init__(self):
        super().__init__()
        self.temp_count = 1
    
    def generate_temp_variable(self):
        temp_variable = f"t{self.temp_count}"
        self.temp_count += 1
        return temp_variable
    
    def infix_to_three_address_code(self, expression):
        stack = []
        three_address_code = []
        
        for char in expression:
            if char.isalnum():
                stack.append(char)
            elif char == '(':
                stack.append(char)
            elif char == ')':
                while stack and stack[-1] != '(':
                    operand2 = stack.pop()
                    operator = stack.pop()
                    operand1 = stack.pop()
                    temp_variable = self.generate_temp_variable()
                    three_address_code.append(f"{temp_variable} = {operand1} {operator} {operand2}")
                    stack.append(temp_variable)
                stack.pop()
            elif self.is_operator(char):
                while stack and stack[-1] != '(' and self.precedence[stack[-1]] >= self.precedence[char]:
                    operand2 = stack.pop()
                    operator = stack.pop()
                    operand1 = stack.pop()
                    temp_variable = self.generate_temp_variable()
                    three_address_code.append(f"{temp_variable} = {operand1} {operator} {operand2}")
                    stack.append(temp_variable)
                stack.append(char)
        
        while stack:
            operand2 = stack.pop()
            operator = stack.pop()
            operand1 = stack.pop()
            temp_variable = self.generate_temp_variable()
            three_address_code.append(f"{temp_variable} = {operand1} {operator} {operand2}")
            stack.append(temp_variable)
        
        return three_address_code

if __name__ == '__main__':
    infix_expression = "a+b*(c-d)"
    
    postfix_converter = InfixToPostfix()
    postfix_expression = postfix_converter.infix_to_postfix(infix_expression)
    
    prefix_converter = InfixToPrefix()
    prefix_expression = prefix_converter.infix_to_prefix(infix_expression)
    
    three_address_code_converter = InfixToThreeAddressCode()
    three_address_code = three_address_code_converter.infix_to_three_address_code(infix_expression)
    
    print(f"Infix Expression: {infix_expression}")
    print(f"Postfix Expression: {postfix_expression}")
    print(f"Prefix Expression: {prefix_expression}")
    print("Three Address Code:")
    for code in three_address_code:
        print(code)
