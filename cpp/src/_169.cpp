#include <bits/stdc++.h>
using namespace std;

class Solution
{
public:
    int majorityElement(vector<int> &nums)
    {
        int now = nums[0];
        int cnt = 1;
        int len = nums.size();
        for (int i = 1; i < len; ++i)
        {
            if (now == nums[i])
            {
                ++cnt;
            }
            else
            {
                --cnt;
                if (cnt == 0)
                {
                    now = nums[i];
                    ++cnt;
                }
            }
        }
        return now;
    }
};

int main()
{
    return 0;
}