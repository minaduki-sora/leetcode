#include <bits/stdc++.h>
using namespace std;

class Solution
{
public:
    int coinChange(vector<int> &coins, int amount)
    {
        vector<int> dp(amount + 1, -1);
        sort(coins.begin(),coins.end());
        dp[0] = 0;
        int t;
        for (int i = 0; i < amount + 1; ++i)
        {
            t = numeric_limits<int>::max();
            for (auto coin : coins)
            {
                if(i - coin < 0)break;
                if (dp[i-coin] >= 0)
                {
                    t = min(t, dp[i - coin] + 1);
                }
            }
            if(t != numeric_limits<int>::max())
            {
                dp[i] = t;
            }
        }
        return dp[amount];
    }
};

int main()
{
    return 0;
}