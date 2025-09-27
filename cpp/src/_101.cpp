#include <bits/stdc++.h>
using namespace std;

struct TreeNode
{
    int val;
    TreeNode *left;
    TreeNode *right;
    TreeNode() : val(0), left(nullptr), right(nullptr) {}
    TreeNode(int x) : val(x), left(nullptr), right(nullptr) {}
    TreeNode(int x, TreeNode *left, TreeNode *right) : val(x), left(left), right(right) {}
};

/*
//quene
class Solution
{
public:
    bool isSymmetric(TreeNode *root)
    {
        if (root->left == nullptr && root->right == nullptr)
            return true;
        else if (root->left == nullptr || root->right == nullptr)
            return false;
        deque<TreeNode *> q1, q2;
        q1.push_back(root->left);
        q2.push_back(root->right);
        bool ans = true;
        while (!q1.empty() && ans)
        {
            auto ln = q1.front();
            auto rn = q2.front();
            q1.pop_front();
            q2.pop_front();
            if (ln == nullptr && rn == nullptr);//nop
            else if (ln == nullptr || rn == nullptr)
            {
                return false;
            }
            else
            {
                ans = ans && ln->val == rn->val;
                q1.push_back(ln->left);
                q2.push_back(rn->right);
                q1.push_back(ln->right);
                q2.push_back(rn->left);
            }
        }
        return ans;
    }
};
*/
//reverse
class Solution
{
public:
    bool isSymmetric(TreeNode *root)
    {
        if (root->left == nullptr && root->right == nullptr)
            return true;
        else if (root->left == nullptr || root->right == nullptr)
            return false;
        return syme(root->left,root->right);
    }
    bool syme(TreeNode *lp, TreeNode *rp)
    {
        if(lp->val != rp->val)return false;
        TreeNode * ln = lp->left;
        TreeNode * rn = rp->right;
        bool rb,lb;
        rb = lb = true;
        if (ln == nullptr && rn == nullptr); // nop
        else if (ln == nullptr || rn == nullptr)
        {
            return false;
        }
        else
        {
            rb = syme(lp->left,rp->right);
        }
        ln = rp->left;
        rn = lp->right;
        if (ln == nullptr && rn == nullptr);
        else if (ln == nullptr || rn == nullptr)
        {
            return false;
        }
        else{
            lb = syme(rp->left,lp->right);
        }
        return rb && lb;
    }
};

int main()
{
    return 0;
}