n = int(input()) if __name__ == "__main__" else 0

# 하지만 autograding은 명령줄 인자(sys.argv)를 사용하므로 수정
import sys

if __name__ == "__main__":
    n = int(sys.argv[1])
    result = []
    for i in range(1, n + 1):
        if n % i == 0:
            result.append(str(i))
    print(" ".join(result))

