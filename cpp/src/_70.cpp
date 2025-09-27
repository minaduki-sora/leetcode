#include <bits/stdc++.h>
using namespace std;

/*
class Solution {
public:
    int climbStairs(int n) {
        vector<int> dp(n+1,0);
        dp[1] = 1;
        dp[0] = 1;
        for(int i = 2;i<n+1;++i)
        {
            dp[i] = dp[i-1] + dp[i-2];
        }
        return dp[n];
    }
};
*/
class Solution {
public:
    int climbStairs(int n) {
        
        int dp_1 = 1;
        int dp_0 = 1;
        int dp;
        while(--n)
        {
            dp = dp_1 + dp_0;
            dp_0 = dp_1;
            dp_1 = dp;
        }
        return dp;
    }
};

int main()
{
    return 0;
}