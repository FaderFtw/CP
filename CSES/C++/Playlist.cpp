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
    vector<int> songs(n);
    for (int i = 0; i < n; i++)
    {
        cin >> songs[i];
    }
    map<int, int> mp;
    int ans = 0;
    for (int i = 0, j = i; i < n; i++)
    {
        while (j < n && mp[songs[j]] < 1)
        {
            mp[songs[j]]++;
            j++;
        }
        ans = max(ans, j - i);
        mp[songs[i]]--;
    }
    cout << ans << endl;
    return 0;
}