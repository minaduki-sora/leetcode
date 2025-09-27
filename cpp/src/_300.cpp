#include <bits/stdc++.h>
using namespace std;

class Solution
{
public:
    int lengthOfLIS(vector<int> &nums)
    {
        int len = nums.size();
        vector<int> dp(len + 1, 0);
        int ans = 0;
        dp[len] = 0;
        int t, j, m;
        for (int i = len - 1; i >= 0; --i)
        {
            t = nums[i];
            for (j = i + 1, m = 0; j < len; ++j)
            {
                if (nums[j] > t)
                {
                    m = max(dp[j],m);
                }
            }
            dp[i] = m + 1;
            ans = max(ans, m+1);
        }
        return ans;
    }
};

int main()
{
    Solution test;
    vector<int> a = {0, 1, 0, 3, 2, 3};
    cout << test.lengthOfLIS(a) << endl;
    return 0;
}