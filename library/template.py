import sys
import math
from collections import deque, defaultdict, Counter

# 再帰上限を増やす（深さ優先探索などで必要）
sys.setrecursionlimit(10**7)

# 入力処理の高速化
# 1文字または1行ずつ読む場合は sys.stdin.readline を使う
def ii(): return int(sys.stdin.readline())
def mi(): return map(int, sys.stdin.readline().split())
def li(): return list(map(int, sys.stdin.readline().split()))
def si(): return sys.stdin.readline().rstrip()

def solve():
    # 入力を一度に読み込む（高速化）
    # input_data = sys.stdin.read().split()
    
    pass

if __name__ == "__main__":
    solve()
