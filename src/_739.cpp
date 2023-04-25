#include <bits/stdc++.h>
using namespace std;

class Solution {
public:
    vector<int> dailyTemperatures(vector<int>& temperatures) {
        int len = temperatures.size();
        vector<int> ans(len,0);
        stack<int> s;
        for(int i = 0;i<len;++i)
        {
            if(s.empty() || temperatures[s.top()] >= temperatures[i])
            {
                s.push(i);
            }
            else
            {
                while(!s.empty() && temperatures[s.top()] < temperatures[i])
                {
                    ans[s.top()] = i - s.top();
                    s.pop();
                }
                s.push(i);
            }
        }
        return ans;
    }
};

int main()
{
    return 0;
}