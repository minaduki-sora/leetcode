#include <bits/stdc++.h>
using namespace std;

class Solution
{
public:
    int numIslands(vector<vector<char>> &grid)
    {
        int len = grid.size();
        int width = grid[0].size();
        vector<vector<bool>> visted(len, vector<bool>(width, false));
        int cnt = 0;
        for (int i = 0; i < len; ++i)
        {
            for (int j = 0; j < width; ++j)
            {
                if (grid[i][j] != '0' && !visted[i][j])
                {
                    dfs(grid, visted, i, j);
                    cnt++;
                }
            }
        }
        return cnt;
    }
    void dfs(vector<vector<char>> &grid, vector<vector<bool>> &visted, int i, int j)
    {
        visted[i][j] = true;
        if (i > 0 && grid[i - 1][j] != '0' && !visted[i - 1][j])
            dfs(grid, visted, i - 1, j);
        if (i < grid.size() - 1 && grid[i + 1][j] != '0' && !visted[i + 1][j])
            dfs(grid, visted, i + 1, j);
        if (j > 0 && grid[i][j - 1] != '0' && !visted[i][j - 1])
            dfs(grid, visted, i, j - 1);
        if (j < grid[0].size() - 1 && grid[i][j + 1] != '0' && !visted[i][j + 1])
            dfs(grid, visted, i, j + 1);
    }
};

int main()
{
    return 0;
}