#include <bits/stdc++.h>
using namespace std;

class Solution
{
public:
    bool wordBreak(string s, vector<string> &wordDict)
    {
        int len = s.length();
        unordered_set<string> sets;
        for (auto w : wordDict)
        {
            sets.emplace(w);
        }
        bool dp[300] = {false};
        for (int i = 0; i < len; ++i)
        {
            for (int j = 0; j < i; ++j)
            {
                if (dp[j] && sets.find(s.substr(j + 1, i - j)) != sets.end())
                {
                    // find
                    dp[i] = true;
                    break;
                }
            }
            if (sets.find(s.substr(0, i+1)) != sets.end())
                dp[i] = true;
        }
        return dp[len-1];
    }
};

int main()
{
    return 0;
}