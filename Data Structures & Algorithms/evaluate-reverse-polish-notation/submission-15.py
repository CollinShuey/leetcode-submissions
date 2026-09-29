class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        stack = []

        symbols = "+/-*"

        for token in tokens:
            
            if token not in symbols:
                stack.append(int(token))
            else:
                
                n1 = stack.pop()
                
                n2 = stack.pop()
                if token == "-":
                    stack.append(n2-n1)
                elif token == "+":
                    stack.append(n2+n1)
                elif token == "/":
                    stack.append(int(n2/n1)) 
                else:
                    stack.append(n2*n1)


        return stack.pop()