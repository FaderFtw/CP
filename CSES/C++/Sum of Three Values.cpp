#include <bits/stdc++.h>
using namespace std;
#define ln '\n'
typedef long long ll;
const int mxN = 2e5;
int main()
{
    int n, t;
    cin >> n >> t;
    vector<pair<int, int>> numbers(n);
    for (int i = 0; i < n; i++)
    {
        ll t;
        cin >> t;
        numbers[i] = make_pair(t, i);
    }
    sort(numbers.begin(), numbers.end());
    for (int i = 0; i < n; i++)
    {
        int t2 = t - numbers[i].first;
        for (int j = i + 1, k = n - 1; j < k; j++)
        {
            while (j < k && numbers[j].first + numbers[k].first > t2)
                k--;
            if (j < k && numbers[j].first + numbers[k].first == t2)
            {
                cout << numbers[i].second + 1 << " " << numbers[j].second + 1 << " " << numbers[k].second + 1 << ln;
                return 0;
            }
        }
    }
    cout << "IMPOSSIBLE" << ln;
    return 0;
}