#include <bits/stdc++.h>
using namespace std;

/*
//hashmap 版本
class Solution
{
public:
    string minWindow(string s, string t)
    {
        int cnt = t.size();
        int len = s.size();
        unordered_map<char, int> hashmap;
        for (auto i : t)
        {
            if (hashmap.find(i) == hashmap.end())
                hashmap[i] = 1;
            else
                hashmap[i]++;
        }
        char de = 0;
        int min_ = 0;
        int left = 0, right;
        //auto hashmap = hashmap;
        for (int i = 0; i < len; ++i)
        {
            if (hashmap.find(s[i]) == hashmap.end())
            {
                continue;
            }
            else
            {
                hashmap[s[i]]--;
                if(hashmap[s[i]] < 0)
                {
                    continue;
                }
                cnt--;
                if (cnt == 0)
                {
                    right = i;
                    min_ = right + 1;
                    break;
                }
            }
        }
        if (min_ == 0)
        {
            return "";
        }
        int j = right;
        for (int i = 0; i < len; ++i)
        {
            while (hashmap.find(s[i]) == hashmap.end() || hashmap[s[i]] < 0)
            {
                // move left pointer
                if(hashmap.find(s[i]) != hashmap.end())
                {
                    //decrease excessive char
                    hashmap[s[i]]++;
                }
                ++i;
                if (i >= len)
                {
                    return s.substr(left, min_);
                }
            }
            if (de != 0)
            {
                // find integral char from right
                ++j;
                while (j < len)
                {
                    if (s[j] == de)
                    {
                        hashmap[de]--;
                        de = 0;
                        break;
                    }
                    else if(hashmap.find(s[j]) != hashmap.end())
                    {
                        //find excessive char
                        hashmap[s[j]]--;
                    }
                    ++j;
                }
                if (j == len)
                {
                    break;
                }
            }
            if (min_ > j - i + 1)
            {
                min_ = j - i + 1;
                left = i;
                right = j;
            }
            // next target
            de = s[i];
            hashmap[de]++;
            if(hashmap[de] <= 0)
            {
                de = 0;
            }
        }
        return s.substr(left, min_);
    }
};
*/

//need window版本:核心利用need中非负数一定是未加入窗口的或者已经满足需求的
//负数可以是多余的需求，也可以是单纯的多余，但对不需求的字符，始终都是非正数
//特别的，在移动左指针时，移动的数是为0的，则一定是满足需求且不多余的字符
//因此需要count++
class Solution {
public:
    string minWindow(string s, string t) {
        vector<int> need(128,0);
        int count = 0;  
        for(char c : t)
        {
            need[c]++;
        }
        count = t.length();
        int l=0, r=0, start=0, size = INT_MAX;
        while(r<s.length())
        {
            char c = s[r];
            if(need[c]>0)
                count--;
            need[c]--;  //先把右边的字符加入窗口
            if(count==0)    //窗口中已经包含所需的全部字符
            {
                while(l<r && need[s[l]]<0) //缩减窗口
                {
                    need[s[l++]]++;
                }   //此时窗口符合要求
                if(r-l+1 < size)    //更新答案
                {
                    size = r-l+1;
                    start = l;
                }
                need[s[l]]++;   //左边界右移之前需要释放need[s[l]]
                l++;
                count++;
            }
            r++;
        }
        return size==INT_MAX ? "" : s.substr(start, size);
    }
};

int main()
{
    Solution test;
    auto c = test.minWindow("ADOBECODEBANC","ABC");
    cout<<c<<endl;
    return 0;
}