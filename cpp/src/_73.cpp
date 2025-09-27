#include <bits/stdc++.h>
using namespace std;

class Solution {
public:
    void setZeroes(vector<vector<int>>& matrix) {
        int first_row = 0;
        int first_column = 0;
        int M = matrix.size();
        int N = matrix[0].size();
        for(int i = 0;i<M;++i)
        {
            if(matrix[i][0] == 0)
            {
                first_column = 1;
                break;
            }
        }
        for(int i = 0;i<N;++i)
        {
            if(matrix[0][i] == 0)
            {
                first_row = 1;
                break;
            }
        }
        for(int i = 1;i<M;++i)
        {
            for(int j = 1;j<N;++j)
            {
                if(matrix[i][j] == 0)
                {
                    matrix[i][0] = matrix[0][j] = 0;
                }
            }
        }
        for(int i = 1;i<M;++i)
        {
            if(matrix[i][0] == 0)row_zero(matrix,i);
        }
        for(int j = 1;j<N;++j)
        {
            if(matrix[0][j] == 0)column_zero(matrix,j);
        }
        if(first_row)row_zero(matrix,0);
        if(first_column)column_zero(matrix,0);
    }
    inline void row_zero(vector<vector<int>>& matrix,int r)
    {
        for(int & i: matrix[r])
        {
            i = 0;
        }
    }
    inline void column_zero(vector<vector<int>>& matrix,int c)
    {
        int M = matrix.size();
        for(int i = 0;i<M;++i)
        {
            matrix[i][c] = 0;
        }
    }
};

int main()
{
    return 0;
}