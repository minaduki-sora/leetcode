#include <bits/stdc++.h>
using namespace std;

class Solution
{
public:
    bool isvalid(string str)
    {
        int cnt = 0;
        for (auto c : str)
        {
            if (c == '(')
                cnt++;
            else if (c == ')')
                cnt--;
            if (cnt < 0)
                return false;
        }
        if (cnt != 0)
            return false;
        return true;
    }

    vector<string> removeInvalidParentheses(string s)
    {
        auto rm = isvalid(s);
        vector<string> ans;
        unordered_set<string> cur, next;
        cur.insert(s);
        if(!rm)
        {
            while (true)
            {
                for (auto str : cur)
                {
                    // 枚举删除的位置
                    for (int i = 0; i < str.length(); i++)
                    {
                        // 重复的跳过
                        if (i > 0 && str[i] == str[i - 1])
                            continue;
                        next.insert(str.substr(0, i) + str.substr(i + 1));
                    }
                }
                cur = next;
                for (auto str : next)
                {
                    if (isvalid(str))
                        ans.emplace_back(str);
                }
                if (ans.size() > 0)
                    return ans;
                next.clear();
            }
        }
        else
        {
            ans.emplace_back(s);
        }
        return ans;
    }
};

int main()
{

    return 0;
}