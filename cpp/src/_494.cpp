#include <bits/stdc++.h>
using namespace std;

class Solution
{
public:
    int findTargetSumWays(vector<int> &nums, int target)
    {
        int sum = -target;
        for (auto i : nums)
        {
            sum += i;
        }
        if (sum < 0 || sum & 0x1 == 1)
            return 0; // summary-target是非负偶数
        sum /=2;
        int n = nums.size();
        vector<vector<int>> dp(n + 1, vector<int>(sum + 1));
        for (int j = 1; j < sum + 1; j++)
            dp[0][j] = 0;
        dp[0][0] = 1;
        for (int i = 1; i < n + 1; i++)
        {
            for (int j = 0; j < sum + 1; j++)
            {
                dp[i][j] = (j < nums[i-1]) ? dp[i - 1][j] : (dp[i - 1][j - nums[i-1]] + dp[i - 1][j]);
            }
        }
        return dp[n][sum];
    }
};

int main()
{
    Solution test;
    vector<int> a({1, 1, 1, 1, 1});
    cout << test.findTargetSumWays(a, 3) << endl;
    return 0;
}