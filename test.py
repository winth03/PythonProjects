a = """"""
b = """"""

# Check if the two strings are equal
def check(a, b):
    test1 = a.strip().split('\n')
    test2 = b.strip().split('\n')
    for i in range(len(test1)):
        try:
            if test1[i] != test2[i]:
                print(f"Line {i} is different")
                print(f"{test1[i]}\n{test2[i]}")
                # print the difference
                for j in range(len(test1[i])):
                    if test1[i][j] != test2[i][j]:
                        print(f"{test1[i][j]} != {test2[i][j]}")
                        break
                return False
        except IndexError:
            print(f"Line {i} is different")
            print(f"{test1[i]}\n{test2[i]}")
            return False
    return True

print(check(a, b))