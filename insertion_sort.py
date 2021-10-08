import numpy as np

def insertion_sort(A):
    for j in range(0, len(A)):
        key = A[j]
        i = j - 1
        while i >= 0 and A[i] > key:
            A[i+1] = A[i]
            i -= 1
        A[i+1] = key
    return A

def display(rand_A, sort_A):
    print(f"Unsorted Array:\n{rand_A}")
    print(f"\nSorted Array:\n{sort_A}")

if __name__ == '__main__':
    rng = np.random.default_rng()
    rand_A = rng.integers(1,1000,size=100)
    display(rand_A, insertion_sort(rand_A.copy()))