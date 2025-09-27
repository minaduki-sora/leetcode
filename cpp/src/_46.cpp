#include <bits/stdc++.h>
using namespace std;

bool used[6];
vector<vector<int>> ans;
vector<int> t;

class Solution
{
public:
    int len;
    vector<vector<int>> permute(vector<int> &nums)
    {
        memset(used, 0, sizeof(used));
        len = nums.size();
        t.clear();
        ans.clear();
        track(nums);
        return ans;
    }
    void track(vector<int> &nums)
    {
        if (t.size() == len)
        {
            ans.push_back(t);
            return;
        }
        for (int i = 0; i < len; ++i)
        {
            if (used[i])
                continue;
            used[i] = true;
            t.push_back(nums[i]);
            track(nums);
            t.pop_back();
            used[i] = false;
        }
    }
};

int main()
{
    return 0;
}