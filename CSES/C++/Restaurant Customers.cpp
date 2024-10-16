#include <bits/stdc++.h>
#include <iostream>
#include <vector>
#include <set>
#include <algorithm>
using namespace std;
#define ll long long
int main()
{
    ll n;
    cin >> n;
    set<array<ll, 2>> s;
    for (int i = 0; i < n; i++)
    {
        ll a, b;
        cin >> a >> b;
        s.insert({a, 1});
        s.insert({b, -1});
    }
    int ans = 0, c = 0;
    for (array<ll, 2> a : s)
    {
        c += a[1];
        ans = max(ans, c);
    }
    cout << ans;
    return 0;
}