#include<iostream>
using namespace std;

int main()
{
    int A,B,C,X;
    cin >> A;
    cin >> B;
    cin >> C;
    cin >> X;

    int ans = 0;
    for(int i = 0; i < A + 1; i++)
    {
    for(int j = 0; j < B + 1;  j++)
    {
    for(int r = 0; r < C + 1;  r++)
    {
        if(500*i + 100*j + 50*r == X)
        {
            ans++;
        }
    }
    }
    }
    cout << ans << endl;
}