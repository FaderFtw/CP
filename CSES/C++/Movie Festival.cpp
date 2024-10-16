#include <bits/stdc++.h>
#include <iostream>
#include <vector>
#include <set>
#include <algorithm>
using namespace std;
#define ll long long
int main()
{
    int n;
    cin >> n;
    vector<pair<int, int>> a;
    for (int i = 0; i < n; i++)
    {
        int x, y;
        cin >> x >> y;
        a.push_back(make_pair(x, y));
    }
    sort(a.begin(), a.end(), [](const pair<int, int> &x, const pair<int, int> &y)
         { return x.second < y.second; });
    int ans = 0;
    int last = 0;
    for (const auto &movie : a)
    {
        if (movie.first >= last)
        {
            ans++;
            last = movie.second;
        }
    }
    cout << ans << endl;
    return 0;
}