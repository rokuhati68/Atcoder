#include <bits/stdc++.h>
using namespace std;

int main() {
    ios::sync_with_stdio(false);
    cin.tie(nullptr);

    int N;
    cin >> N;
    vector<string> S(N);
    for (int i = 0; i < N; i++) cin >> S[i];

    const long long INF = (long long)1e18; 
    vector<long long> nowdp(N + 1, 0);

    for (int i = 0; i < N; i++) {
        vector<int> whiteCnt(N + 1, 0), blackCnt(N + 1, 0);

        // prefix sums
        for (int j = 0; j < N; j++) {
            whiteCnt[j + 1] = whiteCnt[j];
            blackCnt[j + 1] = blackCnt[j];
            if (S[i][j] == '.') whiteCnt[j + 1]++;
            else blackCnt[j + 1]++;
        }

        vector<long long> nxtdp(N + 1, INF);

        long long mn = nowdp[N]; 
        for (int j = N; j >= 0; j--) { 
            mn = min(mn, nowdp[j]);

            long long changeWhite = blackCnt[j];
            long long changeBlack = whiteCnt[N] - whiteCnt[j];

            nxtdp[j] = mn + changeWhite + changeBlack;
        }

        nowdp.swap(nxtdp);
    }

    cout << *min_element(nowdp.begin(), nowdp.end()) << "\n";
    return 0;
}