import sys

def solve():
    input_data = sys.stdin.read().split()
    if not input_data:
        return

    # 入力を受け取る
    a = int(input_data[0])
    b = int(input_data[1])
    ans = a * b
    if ans % 2 == 0:
        print("Even")
    else:
        print("Odd")

if __name__ == "__main__":
    solve()