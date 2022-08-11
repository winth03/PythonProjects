# def test(func):
#     return func("Hello World")

# test(
#     lambda x: (
#         print(x),
#         print("TESTTEST")
#         )
#     )

arr = [1,2,3]
arr2, arr3 = arr, arr.copy()
arr2[1] = 69
arr3[1] = 420
print(arr, arr2, arr3)
