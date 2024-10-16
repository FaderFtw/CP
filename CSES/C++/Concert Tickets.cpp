#include <iostream>
#include <vector>
#include <set>
#include <algorithm>
using namespace std;
#define ll long long
int main()
{
    ll n, m;
    cin >> n >> m;
    multiset<ll, greater<ll>> tickets;
    for (ll i = 0; i < n; i++)
    {
        ll t;
        cin >> t;
        tickets.insert(t);
    }
    for (ll i = 0; i < m; i++)
    {
        ll customerPrice;
        cin >> customerPrice;
        auto it = tickets.lower_bound(customerPrice);
        if (it == tickets.end())
        {
            cout << -1 << endl;
            continue;
        }
        ll ans = *it;
        cout << ans << endl;
        tickets.erase(it);
    }
    return 0;
}