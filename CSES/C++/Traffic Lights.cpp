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
    cin >> x >> n;
    set<int> positions;
    map<int, int> lengths;
    positions.insert(0);
    positions.insert(x);
    lengths[x] = 1;
    for (int i = 0; i < n; i++)
    {
        int tl;
        cin >> tl;
        auto it = positions.upper_bound(tl);
        int r = *it;
        it--;
        int l = *it;
        lengths[r - l]--;
        if (lengths[r - l] == 0)
        {
            lengths.erase(r - l);
        }
        lengths[r - tl]++;
        lengths[tl - l]++;
        positions.insert(tl);
        cout << (--lengths.end())->first << " ";
    }
    return 0;
}