#include <bits/stdc++.h>
using namespace std;

class Solution
{
public:
    int findKthLargest(vector<int> &nums, int k)
    {
        return reverse_findk(nums,0,nums.size() - 1,k);
    }
    int reverse_findk(vector<int> &nums, int left, int right, int k)
    {
        int i, j;
        i = j = left;
        int pivot = nums[right];
        while (j < right)
        {
            if(nums[j] < pivot)
            {
                swap(nums[i],nums[j]);
                ++i;
            }
            ++j;
        }
        swap(nums[i],nums[right]);
        if(right - i + 1 == k)
        {
            return nums[i];
        }
        else if(right - i + 1 > k)
        {
            return reverse_findk(nums,i+1,right,k);
        }
        else
        {
            return reverse_findk(nums,left,i-1,k - right + i -1);
        }
    }
    inline void swap(int & a,int & b)
    {
        int temp = b;
        b = a;
        a = temp;
    }
};

int main()
{
    Solution test;
    vector<int> a = {3,2,1,5,6,4};
    cout<<test.findKthLargest(a,2)<<endl;
    return 0;
}