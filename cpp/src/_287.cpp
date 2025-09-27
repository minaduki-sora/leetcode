#include <bits/stdc++.h>
using namespace std;

class Solution {
public:
    int findDuplicate(vector<int>& nums) {
        int len = nums.size();
        int fast,slow;
        fast = slow = 0;
        do{
            fast = nums[nums[fast]];
            slow = nums[slow];
        }
        while(fast != slow);
        fast = 0;
        while(fast != slow)
        {
            fast = nums[fast];
            slow = nums[slow];
        }
        return fast;
    }
};

int main()
{
    Solution test;
    vector<int> a({1,3,4,2,2});
    cout<<test.findDuplicate(a)<<endl;
    return 0;
}