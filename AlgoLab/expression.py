from stack import ArrayQueue

def eval_post(exp:str) -> tuple((str, int)):
    tokens = exp.strip().split()
    operators = ["+", "-", "*", "/"]
    q = ArrayQueue()
    for token in tokens:
        if token not in operators:
            q.enqueue(token)
        else:
            a = q.dequeue()
            b = q.dequeue()
            c = "".join([a, token, b])
            q.enqueue(c)
    new_exp = q.dequeue()
    res = eval(new_exp)
    if not isinstance(res, int) and not isinstance(res, float):
        raise ValueError("Invalid Expression:", exp)
    return new_exp, res

print(eval_post("1 2 3 / - 1 5 / 4 - *"))