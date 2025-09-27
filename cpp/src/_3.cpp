#include <bits/stdc++.h>
using namespace std;

/*
//classical algorithm
class Solution
{
public:
    int lengthOfLongestSubstring(string s)
    {
        unordered_map<char, int> pi;
        int len = s.length();
        int max_len  = 0;
        for (int i = 0; i < len; ++i)
        {
            if(pi.find(s[i]) == pi.end())
            {
                pi[s[i]] = i;
            }
            else
            {
                max_len = max((int)pi.size(),max_len);
                i = pi[s[i]];
                pi.clear();
            }
        }
        max_len = max((int)pi.size(),max_len);
        return max_len;
    }
};
*/

class Solution
{
public:
    int lengthOfLongestSubstring(string s)
    {
        unordered_set<char> pi;
        int len = s.length();
        int max_len  = 0;
        int right = 0;
        for (int i = 0; i < len; ++i)
        {
            while(right < len && pi.find(s[right]) == pi.end())
            {
                pi.emplace(s[right]);
                ++right;
            }
            max_len = max(max_len,(int)(pi.size()));
            pi.erase(s[i]);
        }
        return max_len;
    }
};


int main()
{
    return 0;
}