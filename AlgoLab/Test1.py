def run(code:str):
    exec(compile(code.strip(), '', 'exec'))

code = """
x=6+9+6*9
print(f"{x=}")
"""

run(code)