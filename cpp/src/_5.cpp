#include <bits/stdc++.h>
using namespace std;

class Solution
{
public:
    string longestPalindrome(string s)
    {
        int len = s.size();
        vector<vector<bool>> dp(len, vector<bool>(len, false));
        int left = 0, _max = 1;
        for (int i = 0; i < len; i++) {
            dp[i][i] = true;
        }
        for(int span = 2;span <= len;++span)
        {
            //i as left
            for(int i = 0;i<len;++i)
            {
                int j = span+i-1;
                if(j>=len)break;
                if(s[i] == s[j])
                {
                    if(span < 3)
                    {
                        dp[i][j] = true;
                    }
                    else
                    {
                        dp[i][j] = dp[i+1][j-1];
                    }
                }
                if(dp[i][j] && _max < span)
                {
                    left = i;
                    _max = span;
                }
            }
        }
        return s.substr(left, _max);
    }
};

int main()
{
    Solution test;
    auto b = test.longestPalindrome("aa");
    cout << b << endl;
    return 0;
}