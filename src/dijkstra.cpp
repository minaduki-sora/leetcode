#include <bits/stdc++.h>
using namespace std;

int n, m, s, cnt;
int head[100005];
int dis[100005];
struct edge
{
    int to, dis, next;
};
edge e[200005];
bool vis[100005];
struct node
{
    int dis, pos;
    bool operator<(const node &x) const
    {
        return x.dis < dis;
    }
};
priority_queue<node> q;

inline void add_edge(int u, int v, int d)
{
    cnt++;
    e[cnt].to = v;
    e[cnt].dis = d;
    e[cnt].next = head[u];
    head[u] = cnt;
}

inline void dijkstra()
{
    dis[s] = 0;
    q.push((node){0, s});
    while (!q.empty())
    {
        node t = q.top();
        q.pop();
        int d = t.dis;
        int pos = t.pos;
        if (vis[pos])
            continue;
        vis[pos] = true;
        for (int i = head[pos]; i; i = e[i].next)
        {
            int y = e[i].to;
            if (!vis[y] && dis[y] > dis[pos] + e[i].dis)
            {
                dis[y] = dis[pos] + e[i].dis;
                q.push((node){dis[y], y});
            }
        }
    }
}

int main()
{
    cin >> n >> m >> s;
    for (int i = 1; i <= n; ++i)
    {
        dis[i] = 0x3fffffff;
    }
    for (int i = 0; i < m; ++i)
    {
        int u, v, w;
        cin>>u>>v>>w;
        add_edge(u, v, w);
    }
    dijkstra();
    for (int i = 1; i <= n; ++i)
    {
        cout << dis[i];
        if (i != n)
            cout << " ";
    }
    return 0;
}