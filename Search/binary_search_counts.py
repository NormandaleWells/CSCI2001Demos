
import binary_search as bs

def main():
    n = int(input("Array size: "))
    a = list(range(n))
    cc = []
    for i in range(-1, n+1):
        result = bs.index_cc(a, i)
        cc.append(result[1])
    print(max(cc))


if __name__ == "__main__":
    main()
