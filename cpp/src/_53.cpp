#include <bits/stdc++.h>
using namespace std;

/*
//O(n)
class Solution
{
public:
    int maxSubArray(vector<int> &nums)
    {
        int ans = 0, left, right;
        int len = nums.size();
        int temp, i = 0, j = 0;
        int m = nums[0];
        while (1)
        {
            while (i < len && nums[i] < 0)
            {
                i++;
                //为了解决数组仅有负数
                if (i >= len)
                    break;
                m = max(m, nums[i]);
            }
            if (m < 0)
                return m;
            j = i;
            temp = 0;
            while (temp >= 0 && j < len)
            {
                temp += nums[j++];
                if (temp > ans)
                {
                    ans = temp;
                    left = i;
                    right = j;
                }
            }
            if (j != len)
            {
                i = j;
            }
            else
                break;
        }
        return ans;
    }
};
*/

//分治法
class Solution
{
public:
    int maxSubArray(vector<int> &nums)
    {
        return maxsub(nums, 0, nums.size() - 1);
    }
    int maxsub(const vector<int> &nums, int i, int j)
    {
        if (i == j)
            return nums[i];
        int mid = (i + j) / 2;
        int left_v = maxsub(nums, i, mid);
        int right_v = maxsub(nums, mid + 1, j);
        // find cross max
        int mid_v = 0;
        int t = 0;
        int left_sum = numeric_limits<int>::min(), right_sum = INT_MIN;
        for (int left = mid; left >= i; --left)
        {
            t += nums[left];
            left_sum = max(left_sum, t);
        }
        t = 0;
        for (int right = mid + 1; right <= j; ++right)
        {
            t += nums[right];
            right_sum = max(right_sum, t);
        }
        mid_v = left_sum + right_sum;
        return max(max(left_v, right_v), mid_v);
    }
};

int main()
{
    return 0;
}