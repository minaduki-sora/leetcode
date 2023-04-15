#include <bits/stdc++.h>
using namespace std;

// hash思想，如果利用1 10做相加，会溢出，
// 但可以利用质数相乘/字母计数相连做字符串/字符排序

/**
class Solution {
public:
    vector<vector<string>> groupAnagrams(vector<string>& strs) {
        unordered_map<string,vector<string>> hashmap;
        for(auto s : strs)
        {
            auto key = s;
            sort(key.begin(),key.end());
            hashmap[key].emplace_back(s);
        }
        vector<vector<string>> ans;
        for(auto it : hashmap)
        {
            ans.emplace_back(it.second);
        }
        return ans;
    }
};
**/

class Solution
{
public:
    vector<vector<string>> groupAnagrams(vector<string> &strs)
    {
        unordered_map<long long, vector<string>> hashmap;

        for (auto s : strs)
        {
            long long key = 1;
            for (auto const &n : s)
            {
                key *= ha(n);
                key = key%(100001611);//不完备，但可以记住此质数
            }
            hashmap[key].emplace_back(s);
        }
        vector<vector<string>> ans;
        for (auto it : hashmap)
        {
            ans.emplace_back(it.second);
        }
        return ans;
    }
    inline int ha(const char &c)
    {
        switch (c)
        {
        case 'a':
            return 2;
            break;
        case 'b':
            return 3;
            break;
        case 'c':
            return 5;
            break;
        case 'd':
            return 7;
            break;
        case 'e':
            return 11;
            break;
        case 'f':
            return 13;
            break;
        case 'g':
            return 17;
            break;
        case 'h':
            return 19;
            break;
        case 'i':
            return 23;
            break;
        case 'j':
            return 29;
            break;
        case 'k':
            return 31;
            break;
        case 'l':
            return 37;
            break;
        case 'm':
            return 41;
            break;
        case 'n':
            return 43;
            break;
        case 'o':
            return 47;
            break;
        case 'p':
            return 53;
            break;
        case 'q':
            return 59;
            break;
        case 'r':
            return 61;
            break;
        case 's':
            return 67;
            break;
        case 't':
            return 71;
            break;
        case 'u':
            return 73;
            break;
        case 'v':
            return 79;
            break;
        case 'w':
            return 83;
            break;
        case 'x':
            return 89;
            break;
        case 'y':
            return 97;
            break;
        case 'z':
            return 101;
            break;
        default:
            return 101;
            break;
        }
    }
};

int main()
{
    return 0;
}