import sys

def solve():
    # 入力を一度に読み込んで空白または改行区切りでリスト化
    input_data = sys.stdin.read().split()
    
    # 入力が空の対策
    if not input_data:
        return

    # a を受け取る
    a = int(input_data[0])
    # b, c を受け取る
    b = int(input_data[1])
    c = int(input_data[2])
    # s を受け取る
    s = input_data[3]
    
    # 計算結果と文字列をスペース区切りで出力する
    print(f"{a + b + c} {s}")

if __name__ == "__main__":
    solve()
