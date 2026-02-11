#include<iostream>
using namespace std;

int main()
{
    int N,A,B;
    cin >> N>>A>>B;
    
    int ans = 0;
    for(int i = 1; i < N + 1; i++)
    {
        int n = i;
        int _sum = 0;
        while(n)
        {
            _sum += n%10;
            n /= 10;
        }
        if(A<=_sum && _sum<=B)
        {
            ans+= i;
        }
    }

    cout << ans <<endl;
    return 0;

}