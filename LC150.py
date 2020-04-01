'''

EVALUATE REVERSE POLISH NOTATION

Evaluate the value of an arithmetic expression in Reverse Polish Notation.
Valid operators are +, -, *, /. Each operand may be an integer or another expression.

Note:
* Division between two integers should truncate toward zero.
* The given RPN expression is always valid. 
  That means the expression would always evaluate to a result and there won't be any divide by zero operation.

'''

def evalRPN(self, tokens: List[str]) -> int:

    def operate(opr: str, op1: str, op2: str) -> int:
        a, b = int(op1), int(op2)
        if opr == "+":
            return a + b
        elif opr == "-":
            return a - b
        elif opr == "*":
            return a * b
        elif opr == "/":
            return int(operator.truediv(a, b))

    operators = ("+", "-", "*", "/")
    stack = []
    for t in tokens:
        if t not in operators:
            stack.append(t)
        else:
            b = stack.pop()
            a = stack.pop()
            res = operate(t, a, b)
            stack.append(res)
    return stack[-1] 
