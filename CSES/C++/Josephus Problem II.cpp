#include <bits/stdc++.h>
#include <iostream>
#include <vector>
#include <ext/pb_ds/assoc_container.hpp>
#include <ext/pb_ds/tree_policy.hpp>
using namespace std;
using namespace __gnu_pbds;
#define ll long long
int main()
{
    int n, k;
    cin >> n >> k;
    typedef tree<int, null_type, less<int>, rb_tree_tag, tree_order_statistics_node_update> ordered_set;
    ordered_set s;
    for (int i = 1; i <= n; i++)
        s.insert(i);
    int start = 0;
    while (!s.empty())
    {
        start %= s.size();
        int posToRem = (start + k) % s.size();
        start = posToRem;
        auto t = s.find_by_order(posToRem);
        cout << *t << endl;
        s.erase(t);
    }
    return 0;
}