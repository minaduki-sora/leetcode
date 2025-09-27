#include <bits/stdc++.h>
using namespace std;

class Solution
{
public:
    int len;
    int firstMissingPositive(vector<int> &nums)
    {
        len = nums.size();
        int ans = -1;
        for (int i = 0; i < len; ++i)
        {
            rectify(nums, i);
        }
        for (int i = 0; i < len; ++i)
        {
            if(nums[i] != i+1)
            {
                return i+1;
            }
        }
        return len+1;
    }
    inline void rectify(vector<int> &nums, int i)
    {
        int next;
        int cur = nums[i];
        while (cur <= len && cur > 0 && nums[cur-1] != cur)
        {
            next = nums[cur];
            nums[cur] = cur;
            cur = next;
        }
    }
};

int main()
{
    return 0;
}