#include <bits/stdc++.h>
using namespace std;
#define ln '\n'
typedef long long ll;
const int mxN = 2e5;
int main()
{
    int n, m;
    cin >> n >> m;
    vector<int> machines(n);
    for (int i = 0; i < n; i++)
        cin >> machines[i];
    ll lb = 0, rb = 1e18;
    while (lb < rb)
    {
        ll mb = (lb + rb) / 2, products = 0;
        for (int i = 0; i < n; i++)
        {
            products += min(mb / machines[i], (ll)1e9);
            if (products >= m)
                break;
        }
        if (m > products)
            lb = mb + 1;
        else
            rb = mb;
    }
    cout << lb << ln;
    return 0;
}