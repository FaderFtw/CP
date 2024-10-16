#include <bits/stdc++.h>
#include <iostream>
#include <vector>
#include <set>
#include <algorithm>
using namespace std;
#define ll long long
int main()
{
    vector<int> numbers;
    int n, m;
    cin >> n >> m;
    for (int i = 0; i < n; i++)
    {
        int num;
        cin >> num;
        numbers.push_back(num);
    }
    vector<int> positions(n, 0);
    for (int i = 0; i < n; i++)
    {
        positions[numbers[i] - 1] = i;
    }
    int ans = 1;
    for (int i = 1; i < n; i++)
    {
        if (positions[i] < positions[i - 1])
        {
            ans += 1;
        }
    }
    for (int i = 0; i < m; i++)
    {
        int a, b;
        cin >> a >> b;
        set<pair<int, int>> updatedPairs;
        if (numbers[a - 1] + 1 <= n)
        {
            updatedPairs.insert({numbers[a - 1], numbers[a - 1] + 1});
        }
        if (numbers[a - 1] - 1 >= 1)
        {
            updatedPairs.insert({numbers[a - 1] - 1, numbers[a - 1]});
        }
        if (numbers[b - 1] + 1 <= n)
        {
            updatedPairs.insert({numbers[b - 1], numbers[b - 1] + 1});
        }
        if (numbers[b - 1] - 1 >= 1)
        {
            updatedPairs.insert({numbers[b - 1] - 1, numbers[b - 1]});
        }
        for (auto swapped : updatedPairs)
        {
            if (positions[swapped.first - 1] > positions[swapped.second - 1])
            {
                ans -= 1;
            }
        }
        swap(numbers[a - 1], numbers[b - 1]);
        positions[numbers[b - 1] - 1] = b - 1;
        positions[numbers[a - 1] - 1] = a - 1;
        for (auto swapped : updatedPairs)
        {
            if (positions[swapped.first - 1] > positions[swapped.second - 1])
            {
                ans += 1;
            }
        }
        cout << ans << endl;
        updatedPairs.clear();
    }
    return 0;
}