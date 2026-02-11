#include<iostream>
using namespace std;

int main()
{
    int N;
    cin >> N;
    int ans = 10000;
    for(int i = 0; i < N; i++)
    {
        int a;
        cin >> a;
        int cnt = 0;

        while(a % 2 == 0)
        {
            a /= 2;
            cnt ++;
        }
        ans = min(ans,cnt);
    
    }
    cout << ans << endl;



}