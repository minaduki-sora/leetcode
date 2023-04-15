#include <bits/stdc++.h>
using namespace std;

/**
 * classical algorithm
class Solution {
public:
    vector<int> twoSum(vector<int>& nums, int target) {
        for(int i = 0; i < nums.size(); i++)
        {
            for(int j = 0; j< nums.size();j++)
            {
                if(i!=j && nums[i] + nums[j] == target)
                {
                    return {i,j};
                }
            }
        }
        return {0,0};
    }
};
*/

class Solution
{
public:
    vector<int> twoSum(vector<int> &nums, int target)
    {
        unordered_map<int, int> h;
        int n = nums.size();
        for (int i = 0; i < n; ++i)
        {
            int t = target - nums[i];
            auto it = h.find(t);
            if(it != h.end())
            {
                return {it->second,i};
            }
            h[nums[i]] = i;
        }
        return {};
    }
};

int main()
{
    Solution test;
    vector<int> a({5, 75, 25});
    auto ans = test.twoSum(a, 100);
    cout << ans[0] << " " << ans[1] << endl;
    return 0;
}