#include <iostream>
#include <set>
using namespace std;
#define ll long long
int main()
{
    set<int> a;
    ll n;
    cin >> n;
    for (ll i = 0; i < n; i++)
    {
        ll x;
        cin >> x;
        a.insert(x);
    }
    cout << a.size();
    return 0;
}