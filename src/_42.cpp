#include <bits/stdc++.h>
using namespace std;

/*
class Solution
{
public:
    int trap(vector<int> &height)
    {
        int len = height.size();
        vector<int> left_max(len);
        vector<int> right_max(len);
        left_max[0] = height[0];
        right_max[len - 1] = height[len - 1];
        for (int i = 1; i < len; ++i)
        {
            left_max[i] = max(left_max[i - 1], height[i]);
        }
        for (int j = len - 2; j >= 0; --j)
        {
            right_max[j] = max(right_max[j + 1], height[j]);
        }
        int ans = 0;
        int h;
        for(int i = 0;i<len;i++)
        {
            h = min(left_max[i],right_max[i]);
            ans += h > height[i] ? h - height[i] : 0;
        }
        return ans;
    }
};
*/

/**
 * 利用双指针的原理：
 * 1 雨水量由两个数组中最小值决定，因此对于left和right走过的地方,
 * 已经更新对应的left_max和right_max
 * 2 同时left离开left_max的唯一可能是出现比left_max更高的右侧，right同理
 * 因此如果left需要移动，则已经保证了右侧有大于left_max的墙，
 * 而left_max为左侧最高的墙，因此此时对应的雨量为left_max - height[left]
 * right同理
 * 3 下面解释移动谁：
 * 当left_max<right_max时，移动left，因为此时left对应的雨量已经得到保证
 * 反之移动right
 * 而height[left]<height[right]蕴含着left_max<right_max，
 * 因为此时left要么为left_max的位置，要么已经移动过，前者显然，
 * 后者移动的原因已经在2解释
 *
class Solution
{
public:
    int trap(vector<int> &height)
    {
        int left = 0, right = height.size() - 1;
        int left_max = 0, right_max = 0;
        int ans = 0;
        while (left < right)
        {
            left_max = max(height[left], left_max);
            right_max = max(height[right], right_max);
            if(left_max < right_max)
            {
                ans += left_max - height[left++];
            }
            else
            {
                ans += right_max - height[right--];
            }
        }
        return ans;
    }
};
*/

//单调栈，本质上层层计算，考虑的是接水的结构为高低高，然后分层计算

class Solution
{
public:
    int trap(vector<int> &height)
    {
        stack<int> stk;
        int len = height.size();
        int ans = 0;
        for(int i = 0;i<len;++i)
        {
            while(!stk.empty() && height[stk.top()] < height[i])
            {
                int top = stk.top();
                stk.pop();
                if(stk.empty()) break;
                int left = stk.top();
                ans += (i - left - 1)*(min(height[i],height[left])-height[top]);
            }
            stk.push(i);
        }
        return ans;
    }
};

int main()
{
    return 0;
}