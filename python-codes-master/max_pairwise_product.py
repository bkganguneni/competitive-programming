# python3
def max_pairwise_product(n,a,b):
    # n is the number of inputs
    # a is the values of the inputs
    # b is the list for appending the products
    for i in range(0,n):
        for j in range (1,n):
            if a[i] != a[j]:
                k = a[i]*a[j]
                b.append(k)
            else:
                continue

        Product = max(b)

    return Product


if __name__ == '__main__':
    n = int(input())
    a = [int(x) for x in input().split()]
    b = list()
    print(max_pairwise_product(n,a,b))