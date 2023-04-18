#include <bits/stdc++.h>
using namespace std;

// classical algorithm TLE
/*
class Solution
{
public:
    vector<vector<int>> threeSum(vector<int> &nums)
    {
        unordered_map<int, vector<int>> hashmap;
        int len = nums.size();
        for (int i = 0; i < len; ++i)
        {
            hashmap[nums[i]].emplace_back(i);
        }
        set<vector<int>> ans;
        int right_value;
        for (int left = 0; left < len - 2; ++left)
        {
            for (int mid = left + 1; mid < len - 1; ++mid)
            {
                right_value = -nums[left] - nums[mid];
                auto f = hashmap.find(right_value);
                if (f == hashmap.end())
                    continue;
                for (auto right : (*f).second)
                {
                    if (right > mid)
                    {
                        auto i = (vector<int>){nums[left], nums[mid], nums[right]};
                        sort(i.begin(),i.end());
                        ans.insert(i);
                    }
                }
            }
        }
        vector<vector<int>> ans_vec;
        for(auto a : ans)
        {
            ans_vec.emplace_back(a);
        }
        return ans_vec;
    }
};
*/

class Solution
{
public:
    vector<vector<int>> threeSum(vector<int> &nums)
    {
        sort(nums.begin(), nums.end());
        int len = nums.size();
        vector<vector<int>> ans;
        int right_value, right_p;
        int left_v, mid_v;
        for (int left = 0; left < len - 2; ++left)
        {
            // the same as precede time
            if (nums[left] == left_v)
                continue;
            else
                left_v = nums[left];
            right_p = len - 1;
            for (int mid = left + 1; mid < len - 1; ++mid)
            {
                if (nums[mid] == mid_v)
                    continue;
                else
                    mid_v = nums[mid];
                right_value = -left_v - mid_v;
                while(right_p > mid && nums[right_p] > right_value)--right_p;
                if(right_p <= mid )break;
                if(nums[right_p] == right_value){
                    ans.emplace_back((vector<int>){left_v,mid_v,right_value});
                }
            }
        }
        return ans;
    }
};

int main()
{
    Solution test;
    vector<int> a({1,1,-2});
    for(auto i : test.threeSum(a))
        for(auto j : i)
            cout<<j<<endl;
    return 0;
}