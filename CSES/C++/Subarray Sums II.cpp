#include <bits/stdc++.h>
using namespace std;
#define ln '\n'
typedef long long ll;
const int mxN = 2e5;
int main()
{
    ll n, target;
    cin >> n >> target;
    ll ans = 0;
    ll sum = 0;
    map<ll, int> mp;
    mp[0]++;
    vector<ll> numbers(n);
    for (int i = 0; i < n; i++)
    {
        cin >> numbers[i];
        sum += numbers[i];
        ans += mp[sum - target];
        mp[sum]++;
    }
    cout << ans << endl;
    return 0;
}