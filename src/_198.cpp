#include <bits/stdc++.h>
using namespace std;

/*
//空间复杂度O(n) 时间复杂度O(n)
class Solution
{
public:
    int rob(vector<int> &nums)
    {
        int len = nums.size();
        // dp[i][j] j=0 不偷i j=1 偷i
        vector<vector<int>> dp(len + 1, vector<int>(2, 0));
        for (int i = 1; i < len + 1; i++)
        {
            dp[i][0] = max(dp[i - 1][1], dp[i - 1][0]);
            dp[i][1] = dp[i - 1][0] + nums[i - 1];
        }
        return max(dp[len][0], dp[len][1]);
    }
};
*/

// 空间复杂度O(1) 时间复杂度O(n)但常数大
class Solution
{
public:
    int rob(vector<int> &nums)
    {
        int len = nums.size();
        // 0 不偷i 1 偷i
        int cur_0, cur_1;
        int pre_0 = 0, pre_1 = 0;
        for (int i = 1; i < len + 1; i++)
        {
            cur_0 = max(pre_1, pre_0);
            cur_1 = pre_0 + nums[i - 1];
            pre_0 = cur_0;
            pre_1 = cur_1;
        }
        return max(cur_0, cur_1);
    }
};

/**
 * 然而实际上，只需要一维dp数组，因为当出现dp[i-1]不偷i-1时,
 * dp[i-1] = dp[i-2],
 * 因而dp[i] = max(dp[i-2]+nums[i],dp[i-1])可以解决这种情况
 */

int main()
{
    return 0;
}