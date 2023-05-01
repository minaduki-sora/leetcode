#include <bits/stdc++.h>
using namespace std;

/*
// back forward
class Solution {
public:
    vector<int> temp;
    vector<vector<int>> ans;
    vector<vector<int>> subsets(vector<int>& nums) {
        subset(nums,0);
        return ans;
    }
    void subset(vector<int>&nums,int k)
    {
        if(k == nums.size() - 1)
        {
            ans.push_back(temp);
            temp.push_back(nums[k]);
            ans.push_back(temp);
            temp.pop_back();
            return;
        }
        subset(nums,k+1);
        temp.push_back(nums[k]);
        subset(nums,k+1);
        temp.pop_back();//forward
    }
};
*/

//二进制模式串
class Solution {
public:
    vector<vector<int>> subsets(vector<int>& nums) {
        int s = 0;
        int len = nums.size();
        int i = pow(2,len);
        vector<vector<int>> ans;
        while(i-->0)
        {
            bitset<10> bi(i);
            ans.emplace_back(btov(bi.to_string(),len,nums));
        }
        return ans;
    }
    inline vector<int>& btov(string bi,int len,vector<int>& nums)
    {
        vector<int> _ans;
        for(int i = 10-len;i<10;++i)
        {
            if(bi[i] == '1')_ans.emplace_back(nums[i-10+len]);
        }
        return _ans;
    }
};

int main()
{
    Solution test;
    vector<int> nums({1,2,3});
    auto a = test.subsets(nums);
    for(auto i : a)
    {
        for(auto j : i)
        {
            cout<<j<<" ";
        }
        cout<<endl;
    }
    return 0;
}