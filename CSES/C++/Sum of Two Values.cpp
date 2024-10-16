#include <bits/stdc++.h>
#include <iostream>
#include <vector>
#include <set>
#include <algorithm>
using namespace std;
#define ll long long
int main()
{
    int n, x;
    cin >> n >> x;
    map<int, int> mp;
    for (int i = 0; i < n; i++)
    {
        int a;
        cin >> a;
        if (mp.find(x - a) != mp.end())
        {
            cout << mp[x - a] + 1 << " " << i + 1 << endl;
            return 0;
        }
        mp[a] = i;
    }
    cout << "IMPOSSIBLE" << endl;
    return 0;
}