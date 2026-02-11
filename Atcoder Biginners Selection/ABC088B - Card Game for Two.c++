#include<iostream>
#include <bits/stdc++.h>
using namespace std;
#define rep(i, n) for (int i = 0; i < (int)(n); i++)

int N,A[101];

int main()
{
    cin >> N;
    rep(i,0,N) cin>>A[i];
    sort(A,A+N,greater<int>());

    int v[2] = {0,0};
    rep(i,0,N) v[i%2] += A[i];

    int ans = v[0] - v[1];
    cout << ans << endl;

}