#include <bits/stdc++.h>
using namespace std;

/*
//dp
//思路与爬楼梯一致，只不过加法换min()
class Solution {
public:
    int jump(vector<int>& nums) {
        int len = nums.size();
        vector<int> dp(len,INT_MAX);
        dp[0] = 0;
        for(int i = 0; i < len; ++i)
        {
            for(int j = min(nums[i],len-i-1); j > 0; --j)
            {
                dp[i+j] = min(dp[i+j],dp[i]+1);
            }
        }
        return dp[len - 1];
    }
};
*/

//阶梯式前进
class Solution
{
public:
    int jump(vector<int> &nums)
    {
        int _begin, _end;
        _begin = _end = 0;
        int cnt = 0;
        int len = nums.size();
        int i,next = INT_MIN;
        while (_end < len - 1)
        {
            for (i = _begin; i <= _end; ++i)
            {
                next = max(next,i+nums[i]);
            }
            _begin = _end + 1;
            _end = next;
            cnt++;
        }
        return cnt;
    }
};

int main()
{
    return 0;
}