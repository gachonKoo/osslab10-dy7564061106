import sys

if __name__ == "__main__":
    n = int(sys.argv[1])
    for i in range(1, n + 1):
        if n % i == 0:
            print(i, end=" ")

