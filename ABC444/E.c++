#include <iostream>
#include <vector>
#include <set>
#include <deque>

using namespace std;


int main() {
    
    ios::sync_with_stdio(false);
    cin.tie(nullptr);

    long long N, D;
    if (!(cin >> N >> D)) return 0;

    vector<long long> A(N);
    for (int i = 0; i < N; ++i) {
        cin >> A[i];
    }

    set<long long> s;
    const long long INF = 2e18; 
    s.insert(-INF);
    s.insert(INF);

    deque<long long> q;
    long long ans = 0;
    long long cnt = 0;

    for (long long a : A) {
        while (true) {
    
            auto it = s.lower_bound(a);
            
            
            
            if (a - *prev(it) >= D && *it - a >= D) {
                break;
            }

            
            if (!q.empty()) {
                long long pre = q.front();
                q.pop_front();
                s.erase(pre);
                cnt--;
            }
        }

        
        cnt++;
        ans += cnt;
        
        
        q.push_back(a);
        s.insert(a);
    }

    cout << ans << endl;

    return 0;
}