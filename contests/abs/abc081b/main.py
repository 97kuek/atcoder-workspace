# 入力
n = int(input())
a = list(map(int, input().split()))

# 初期化
ans = 0

# 全ての要素が偶数である限りループ
while all(i % 2 == 0 for i in a):
    # 全ての要素を2で割る
    a = [i // 2 for i in a]
    # カウントを1増やす
    ans += 1

print(ans)