#include <bits/stdc++.h>
using namespace std;

class Solution
{
public:
    vector<int> findAnagrams(string s, string p)
    {
        int left, right;
        int len = s.size();
        int lenp = p.size();
        unordered_map<char,int> hashmap;
        unordered_map<char,int> ha;
        vector<int> ans;
        for (const char &c : p)
        {
            if(hashmap.find(c) == hashmap.end())
            {
                hashmap[c] = 1;
            }
            else
            {
                ++hashmap[c];
            }
            ha[c] = 0;
        }
        int cnt = 0;
        for (left = right = 0; left < len - lenp + 1; ++left)
        {
            if (hashmap.count(s[left]) == 0)
            {
                right = left + 1;
                continue;
            }
            while (right < len && hashmap.count(s[right]) > 0 && ha[s[right]] < hashmap[s[right]])
            {
                ++cnt;
                ++ha[s[right]];
                ++right;
                if (cnt == lenp)
                {
                    ans.emplace_back(left);
                    break;
                }
            }
            --cnt;
            --ha[s[left]]; // left pointer move
        }
        return ans;
    }
};

int main()
{
    Solution test;
    auto a = test.findAnagrams("baa", "aa");
    for (auto i : a)
    {
        cout << i << endl;
    }
    return 0;
}