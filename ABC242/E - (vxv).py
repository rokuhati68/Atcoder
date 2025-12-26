T = int(input())
MOD = 998244353
for _ in range(T):
    N = int(input())
    S = input()
    _len = (N + 1) // 2
    dp = [0] * (_len + 1)
    for i in range(_len):
        num = ord(S[i]) - ord("A")
        dp[i + 1] += dp[i] + (num * pow(26,_len - i - 1,MOD))
        dp[i + 1] %= MOD
    ans = dp[-1]
    if N % 2 == 1:
        s = S[:_len - 1]
        s +=S[_len - 1] + s[::-1]
    else:
        s = S[:_len]
        s += s[::-1]
    
    if s <= S:
        ans += 1
    print(ans % MOD)
    