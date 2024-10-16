#include <bits/stdc++.h>
using namespace std;
#define ln '\n'
typedef long long ll;
const int mxN = 2e5;
int main()
{
    int n, t;
    cin >> n >> t;
    vector<int> numbers(n);
    for (int i = 0; i < n; i++)
    {
        cin >> numbers[i];
    }
    unordered_map<int, array<int, 2>> mp;
    mp.reserve(1 >> 20);
    for (int i = 0; i < n; i++)
    {
        for (int j = i + 1; j < n; j++)
        {
            if (mp.find(t - numbers[i] - numbers[j]) != mp.end())
            {
                auto p = mp[t - numbers[i] - numbers[j]];
                cout << p[0] + 1 << " " << p[1] + 1 << " " << i + 1 << " " << j + 1 << ln;
                return 0;
            }
        }
        for (int j = 0; j < i; j++)
            mp[numbers[i] + numbers[j]] = {i, j};
    }
    cout << "IMPOSSIBLE" << ln;
    return 0;
}