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
    vector<int> cubes(n);
    for (int i = 0; i < n; i++)
    {
        cin >> cubes[i];
    }
    multiset<int> towers;
    for (int i = 0; i < n; i++)
    {
        if (towers.size() == 0)
        {
            towers.insert(cubes[i]);
        }
        else
        {
            auto it = towers.upper_bound(cubes[i]);
            if (it == towers.end())
            {
                towers.insert(cubes[i]);
            }
            else
            {
                towers.erase(it);
                towers.insert(cubes[i]);
            }
        }
    }
    cout << towers.size() << endl;
    return 0;
}