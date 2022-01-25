#include <iostream>
#include <algorithm>

#define int long long
using namespace std;
const int mxn = 5005;

int arr[mxn];
int dp[mxn][mxn];
void solve() {
    int n;
    cin >> n;
    for (int i = 0; i < n; i++) cin >> arr[i];
    sort(arr, arr + n);
    int ans = 1;
    for (int i = 0; i < n - 1; i++) {
        int pr = 0;
        int mx = -1;
        for (int j = n - 1; j > i; j--) {
            dp[i][j] = 2;
            while (pr < i && arr[i] - arr[pr] > arr[j] - arr[i]) {
                mx = max(mx, dp[pr][i] + 1);
                pr++;
            }
            dp[i][j] = max(dp[i][j], mx);
            ans = max(ans, dp[i][j]);
        }
    }
    cout << ans << "\n";
}
int32_t main() {
    ios::sync_with_stdio(false);
    cin.tie(nullptr);
    cout.tie(nullptr);
    int t;
    cin >> t;
    for (int t1 = 0; t1 < t; t1++) {
        solve();
    }
    return 0;
}