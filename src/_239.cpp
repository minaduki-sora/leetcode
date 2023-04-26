#include <bits/stdc++.h>
using namespace std;

/*
//思路：利用堆存当前最大值，如果不在窗口内就连续pop直到top在窗口内
class Solution
{
public:
    vector<int> maxSlidingWindow(vector<int> &nums, int k)
    {
        priority_queue<pair<int, int>> q;
        int len = nums.size();
        vector<int> ans;
        for (int i = 0; i < len && i<k; ++i)
        {
            q.push(make_pair(nums[i],i));
        }
        ans.emplace_back(q.top().first);
        for(int i = k; i < len; ++i)
        {
            q.push(make_pair(nums[i],i));
            while(q.top().second <= i - k)q.pop();
            ans.emplace_back(q.top().first);
        }
        return ans;
    }
};
*/

//单调队列:deque实现，cut & push
class Solution
{
public:
    vector<int> maxSlidingWindow(vector<int> &nums, int k)
    {
        deque<int> q;
        int len = nums.size();
        vector<int> ans;
        for (int i = 0; i < len && i < k; ++i)
        {
            PushAndCut(q,nums,i,i-k);
        }
        ans.emplace_back(nums[q.front()]);
        for (int i = k; i < len; ++i)
        {
            PushAndCut(q,nums,i,i-k);
            ans.emplace_back(nums[q.front()]);
        }
        return ans;
    }
    inline void PushAndCut(deque<int> &q, vector<int> &nums, int &a, int left)
    {
        push(q, nums, a);
        cut(q,left);
    }
    inline void push(deque<int> &q, vector<int> &nums, int a)
    {
        auto i = q.rbegin();
        while (i != q.rend() && nums[*i] <= nums[a])
        {
            q.pop_back();
            i++;
        }
        q.emplace_back(a);
    }
    inline void cut(deque<int> &q, int left)
    {
        auto i = q.begin();
        while(i != q.end() && (*i) <= left)
        {
            q.pop_front();
            i++;
        }
    }
};

int main()
{
    return 0;
}