#include <bits/stdc++.h>
using namespace std;

class Solution
{
public:
    string decodeString(string s)
    {
        stack<string> S;
        stack<int> times;
        string time;
        string str("");
        for (char c : s)
        {
            if (isdigit(c))
            {
                time += c;
            }
            else if (c == '[')
            {
                times.push(atoi(time.c_str()));
                time = "";
                S.push(str);
                str = "";
            }
            else if (c == ']')
            {  
                int t = times.top();//当前层对应的times,于上一层进入[时进栈
                times.pop();
                string st = S.top();//上一层[]内的str
                S.pop();
                //返回上一层,处理内层[]
                for(int i = 0; i<t;i++)
                {
                    st += str;
                }
                str = st;//已返回上一层,str继续读取字符
            }
            else
            {
                str += c;
            }
        }
        return str;
    }
};

int main()
{
    Solution test;
    auto a = test.decodeString("3[1[ab]3[c]]2[d]");
    cout << a << endl;
    return 0;
}