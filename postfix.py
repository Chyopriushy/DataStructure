class Stack:
    def __init__(self, capacity = 10):
        self.capacity = capacity
        self.arr = [None] * self.capacity
        self.top = -1

    def size(self):
        return self.top + 1

    def empty(self):
        return not self.size()

    def full(self):
        return self.capacity <= self.size()

    def push(self, data):
        if self.full():
            raise IndexError("this stack full")
        self.top += 1
        self.arr[self.top] = data

    def peek(self):
        if self.empty():
            raise IndexError("this stack empty")
        return self.arr[self.top]

    def pop(self):
        if self.empty():
            raise IndexError("this stack empty")
        ret = self.arr[self.top]
        self.top -= 1
        return ret


    def __str__(self):
        ret = []
        i = 0
        while i < self.size():
            ret.append(self.arr[i])
            i += 1
        ret = ", ".join(map(str, ret))
        return f"[{ret}]"

def infix_to_postfix(expr):
    OPS = {"+", "-", "*", "/", "^", "(", ")"}
    PREC = {"+": 1, "-": 1, "*": 2, "/": 2, "^": 3, None: 9}

    stack = Stack(len(expr))
    ret = []

    for tok in expr:
        if tok not in OPS:
            ret.append(tok)
        elif tok == "(":
            stack.push(tok)
        elif tok == ")":
            while stack.peek() != "(":
                ret.append(stack.peek())
                stack.pop()
            stack.pop()
        else:
            while not stack.empty() and PREC.get(tok, 0) <= PREC.get(stack.peek(), 0):
                ret.append(stack.peek())
                stack.pop()
            stack.push(tok)

    if not stack.empty():
        while not stack.empty():
            ret.append(stack.peek())
            stack.pop()

    return "".join(ret)

if __name__ == "__main__":
    expr = "a/b+c*d/e"
    postfix = infix_to_postfix(expr)
    print(f"{expr} => {postfix}")
    expr = "a*b/c*d/e*f/g"
    postfix = infix_to_postfix(expr)
    print(f"{expr} => {postfix}")
    expr = "a+b*c"
    postfix = infix_to_postfix(expr)
    print(f"{expr} => {postfix}")
    expr = "a*b+c"
    postfix = infix_to_postfix(expr)
    print(f"{expr} => {postfix}")
    expr = "a+(b*c+d)*e"
    postfix = infix_to_postfix(expr)
    print(f"{expr} => {postfix}")
    expr = "3+5*2/(7-2)"
    postfix = infix_to_postfix(expr)
    print(f"{expr} => {postfix}")