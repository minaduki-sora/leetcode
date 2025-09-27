#include <bits/stdc++.h>
using namespace std;

class MinStack
{
private:
    stack<pair<int,int>> s;
    int _min;
public:
    MinStack()
    {
        _min = INT_MAX;
    }

    void push(int val)
    {
        _min = min(val,_min);
        s.push(make_pair(val,_min));
    }

    void pop()
    {
        s.pop();
        if(s.empty())
        {
            _min = INT_MAX;
        }
        else
        {
            _min = s.top().second;
        }
    }

    int top()
    {
        return s.top().first;
    }

    int getMin()
    {
        return s.top().second;
    }
};

int main()
{
    return 0;
}