#include <bits/stdc++.h>
using namespace std;

class Solution
{
public:
    int orangesRotting(vector<vector<int>> &grid)
    {
        deque<pair<int, int>> cur[2];
        int m = grid.size();
        int n = grid[0].size();
        vector<vector<bool>> visit(m, vector<bool>(n, false));
        int num=0;
        int rot = 0;
        for (int i = 0; i < m; ++i)
        {
            for (int j = 0; j < n; ++j)
            {
                if (grid[i][j] == 2)
                {
                    cur[0].push_back(make_pair(i, j));
                    visit[i][j] = true;
                    rot++;
                }
                else if(grid[i][j]==1)
                {
                    num++;
                }
            }
        }
        if(num == 0 && rot == 0)return 0;
        int i, j,flag,negflag;
        flag = 0;
        negflag = 1;
        int cnt = 0;
        while (!cur[0].empty() || !cur[1].empty())
        {
            while (!cur[flag].empty())
            {
                auto loca = cur[flag].front();
                cur[flag].pop_front();
                i = loca.first;
                j = loca.second;
                if(i>0 && grid[i-1][j] == 1 && visit[i-1][j] == false)
                {
                    num--;
                    visit[i-1][j] = true;
                    cur[negflag].push_back(make_pair(i-1,j));
                }
                if(j>0 && grid[i][j-1] == 1 && visit[i][j-1] == false)
                {
                    num--;
                    visit[i][j-1] = true;
                    cur[negflag].push_back(make_pair(i,j-1));
                }
                if(i<m-1 && grid[i+1][j] == 1 && visit[i+1][j] == false)
                {
                    num--;
                    visit[i+1][j] = true;
                    cur[negflag].push_back(make_pair(i+1,j));
                }
                if(j<n-1 && grid[i][j+1] == 1 && visit[i][j+1] == false)
                {
                    num--;
                    visit[i][j+1] = true;
                    cur[negflag].push_back(make_pair(i,j+1));
                }
            }
            cnt++;
            negflag = flag;
            flag = (flag + 1) & 1;
        }
        if(num != 0)return -1;
        return cnt-1;
    }
};

int main()
{
    Solution test;
    vector<vector<int>> grid({{0}});
    cout<<test.orangesRotting(grid)<<endl;
    return 0;
}