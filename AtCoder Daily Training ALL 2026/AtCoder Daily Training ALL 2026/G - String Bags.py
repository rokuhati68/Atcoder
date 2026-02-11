T = input().strip()
N = int(input())
_lenT = len(T)

# dp[j] : Tのj文字目まで作るのに必要な最小コスト
# 非常に大きい値（101など）で初期化
INF = float('inf')
dp = [INF] * (_lenT + 1)
dp[0] = 0

for _ in range(N):
    line = input().split()
    # 最初の a はこの問題では使わない（袋iの番号や個数などのため）
    # 実際には A_i (個数) が line[0] に相当
    S_list = line[1:]
    
    # 次の状態を保存する一時的な配列（この袋を「使う」か「使わない」か）
    next_dp = dp[:]
    
    for s in S_list:
        _lenS = len(s)
        for j in range(_lenT - _lenS + 1):
            # 現在 j 文字目まで完成していて、かつそこから s が T と一致するか
            if dp[j] != INF and T[j:j + _lenS] == s:
                next_dp[j + _lenS] = min(next_dp[j + _lenS], dp[j] + 1)
    
    dp = next_dp

# 最終的な答え
ans = dp[_lenT]
print(ans if ans != INF else -1)