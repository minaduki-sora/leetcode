#include <bits/stdc++.h>
using namespace std;

//classical algorithm + improve
/**
class Solution
{
public:
    int maxArea(vector<int> &height)
    {
        int len = height.size();
        int high = 0;//improve
        int max_capacity = 0;
        for (int i = 0; i < len; ++i)
        {
            int left = height[i];
            if(left <= high) continue;
            else high = left;
            for (int j = i + 1; j < len; ++j)
            {
                int capacity = min(height[j], left) * (j - i);
                max_capacity = max(max_capacity, capacity);
            }
        }
        return max_capacity;
    }
};
 */

//double pointer
class Solution
{
public:
    int maxArea(vector<int> &height)
    {
        int i = 0,j = height.size() -1;
        int capacity,max_capacity=0;
        int left,right;
        while(i<j)
        {
            left = height[i];
            right = height[j];
            if(left < right)
            {
                capacity = left*(j-i);
                max_capacity = max(capacity,max_capacity);
                ++i;
            }
            else
            {
                capacity = right*(j-i);
                max_capacity = max(capacity,max_capacity);
                --j;
            }
        }
        return max_capacity;
    }
};

int main()
{
    return 0;
}