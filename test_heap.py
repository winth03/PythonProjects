def heapify(node, A):
    if node >= len(A) // 2:
        return
    max = node
    left = 2 * node + 1  # left = 2*i + 1
    right = 2 * node + 2  # right = 2*i + 2
    if left < len(A) and A[left] > A[max]:
        max = left
    if right < len(A) and A[right] > A[max]:
        max = right
    if max != node:
        A[max], A[node] = A[node], A[max]
        heapify(max, A)

def build_max_heap(A, i=0):
    last_non_leaf = len(A) // 2 - 1
    for i in range(last_non_leaf, -1, -1):
        heapify(i, A)

A = [3, 9, 2, 1, 4, 5]
build_max_heap(A)
print(A)

# def heap_sort_asc(A):
#     build_max_heap(A)
#     print(A)
#     # Sorting
#     for i in range(len(A) - 1, 0, -1):
#         A[i], A[0] = A[0], A[i]
#         node = 0
#         max = node
#         left = 2 * node + 1  # left = 2*i + 1
#         right = 2 * node + 2  # right = 2*i + 2
#         while True:
#             if left < i and A[left] > A[max]:
#                 max = left
#             if right < i and A[right] > A[max]:
#                 max = right
#             if max != node:
#                 A[max], A[node] = A[node], A[max]
#                 node = max
#                 left = 2 * node + 1
#                 right = 2 * node + 2
#                 continue
#             break
#         print(A)
    
# A = [3, 9, 2, 1, 4, 5]
# heap_sort_asc(A)