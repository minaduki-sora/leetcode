#include <bits/stdc++.h>
using namespace std;

/*
//classical algorithm
class Solution {
public:
    int subarraySum(vector<int>& nums, int k) {
        int len = nums.size();
        vector<int> sum(len+1,0);
        for(int i = 1;i<len+1;++i)
        {
            sum[i] = sum[i-1] + nums[i-1];
        }
        int ans = 0;
        for(int i = 0; i < len ; ++i)
        {
            for(int j = i + 1; j < len + 1; ++j)
            {
                if(sum[j] - sum[i] == k){
                    ans++;
                }
            }
        }
        return ans;
    }
};
*/
//prefix sum + hashmap//前缀和差移项
class Solution
{
public:
    int subarraySum(vector<int> &nums, int k)
    {
        int len = nums.size();
        unordered_map<int, int> maps;
        int ans = 0;
        int pre = 0;
        maps[0] = 1;
        for (const int &i : nums)
        {
            pre += i;
            if(maps.find(pre-k) != maps.end())
            {
                ans += maps[pre-k];
            }
            maps[pre]++;
        }
        return ans;
    }
};

int main()
{
    return 0;
}