#include <bits/stdc++.h>
using namespace std;

/*
//逆向思维
class Solution
{
public:
    bool canJump(vector<int> &nums)
    {
        bool dp[30000] = {false};
        int len = nums.size();
        dp[len - 1] = true;
        bool t;
        for (int i = len - 2; i >= 0; --i)
        {
            t = false;
            for(int j = min(nums[i],len-i-1); j>0 && !t;--j)
            {
                t = t||dp[i+j];
            }
            dp[i] = t;
        }
        return dp[0];
    }
};
*/

//正向思维
class Solution
{
public:
    bool canJump(vector<int> &nums)
    {
        int max_len = 0;
        int len = nums.size();
        for(int i = 0; i < len; ++i)
        {
            if(i>max_len)return false;
            max_len = max(max_len,i+nums[i]);
        }
        return true;
    }
};

int main()
{
    return 0;
}