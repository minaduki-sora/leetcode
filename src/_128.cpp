#include <bits/stdc++.h>
using namespace std;

//classical algorithm 遍历一遍，仅在开头时做查询，最坏O(n^2)
/**
 class Solution {
public:
    int longestConsecutive(vector<int>& nums) {
        unordered_set<int> hashset;
        for(const int& i : nums)
        {
            hashset.insert(i);
        }
        int ans = 0;
        for(const int & i : hashset)
        {
            if(hashset.count(i-1) == 0)
            {
                int len = 1;
                int j = i;
                while(hashset.count(j + 1))
                {
                    len++;
                    j++;
                }
                ans = max(ans,len);
            }
        }
        return ans;
    }
};
 */
/*
class Solution {
public:
    int longestConsecutive(vector<int>& nums) {
        unordered_set<int> hashset;
        unordered_map<int,int> hashmap;
        for(const int& i : nums)
        {
            hashset.insert(i);
        }
        int ans = 0;
        for(const auto & i : hashset)
        {
            int left = GetOrDefault(hashmap,i-1);
            int right = GetOrDefault(hashmap,i+1);
            int mid = left + right + 1;
            ans = max(mid,ans);
            hashmap[i-left] = mid;
            hashmap[i+right] = mid;
        } 
        return ans;
    }
    inline int GetOrDefault(const unordered_map<int,int>& hashmap,const int& key,int Default = 0)
    {
        auto f = hashmap.find(key);
        if(f == hashmap.end()) return Default;
        else return (*f).second;
    }
};
*/
/*
//针对时间空间复杂度进行改进
class Solution {
public:
    int longestConsecutive(vector<int>& nums) {
        unordered_map<int,int> hashmap;
        int ans = 0;
        for(const auto & i : nums)
        {
            if(hashmap.find(i) == hashmap.end())
            {
                int left = GetOrDefault(hashmap,i-1);
                int right = GetOrDefault(hashmap,i+1);
                int mid = left + right + 1;
                ans = max(mid,ans);
                hashmap[i] = mid;//此时为必需，因重复数值不重复执行的原理是find == end
                hashmap[i-left] = mid;
                hashmap[i+right] = mid;
            }
        } 
        return ans;
    }
    inline int GetOrDefault(const unordered_map<int,int>& hashmap,const int& key,int Default = 0)
    {
        auto f = hashmap.find(key);
        if(f == hashmap.end()) return Default;
        else return (*f).second;
    }
};
*/

//搜索思想,一维状态的搜索，向邻近扩散，维护一个visited数组用于判断是否已经被搜索
//复杂度O(n)
class Solution
{
public:
    int longestConsecutive(vector<int> &nums)
    {
        unordered_map<int, bool> maps;
        for (auto i : nums)
        {
            maps[i] = false;
        }
        int left, right, _max = 0;
        for (auto i : nums)
        {
            if (maps[i])
                continue;
            maps[i] = true;
            for (left = i - 1; maps.find(left) != maps.end(); --left)
            {
                maps[left] = true;
            }
            for (right = i + 1; maps.find(right) != maps.end(); ++right)
            {
                maps[right] = true;
            }
            _max = max(_max, right - left - 1);
        }
        return _max;
    }
};


int main()
{
    Solution test;
    vector<int> a ({100,4,200,1,3,2});
    cout<<test.longestConsecutive(a)<<endl;
    return 0;
}