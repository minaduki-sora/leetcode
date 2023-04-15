#include <bits/stdc++.h>
using namespace std;

// 双向链表
class DLNode
{
public:
    int key, value;
    DLNode *prev, *next;

    DLNode() : key(0), value(0), prev(nullptr), next(nullptr){};
    DLNode(int k, int v) : key(k), value(v), prev(nullptr), next(nullptr){};
    ~DLNode(){};
};

class LRUCache
{
private:
    int capacity;
    int size;
    DLNode *head, *tail;
    unordered_map<int, DLNode *> maps;

public:
    LRUCache(int _capacity);
    int get(int key);
    void put(int key, int value);
    void move(DLNode *node);
    void add(DLNode *node);
    void drop();
};

LRUCache::LRUCache(int _capacity)
{
    this->capacity = _capacity;
    size = 0;
    // head,tail为假头部尾部
    head = new DLNode();
    tail = new DLNode();
    head->next = tail;
    tail->prev = head;
}

int LRUCache::get(int key)
{
    auto f = maps.find(key);
    if (f == maps.end())
        return -1;
    auto node = (*f).second;
    move(node);
    return node->value;
}

void LRUCache::put(int key, int value)
{
    auto f = maps.find(key);
    if (f == maps.end())
    {
        auto node = new DLNode(key, value);
        add(node);
        maps[key] = node;
        size++;
        if (size > capacity)
        {
            drop();
        }
    }
    else
    {
        (*f).second->value = value;
        move((*f).second);
    }
}

void LRUCache::move(DLNode *node)
{
    if (node->prev == head)
        return;
    node->prev->next = node->next;
    node->next->prev = node->prev;
    auto n = head->next;
    head->next = node;
    n->prev = node;
    node->prev = head;
    node->next = n;
}

void LRUCache::add(DLNode *node)
{
    auto n = head->next;
    head->next = node;
    n->prev = node;
    node->prev = head;
    node->next = n;
}

void LRUCache::drop()
{
    size--;
    auto node = tail->prev;
    auto p = node->prev;
    p->next = tail;
    tail->prev = p;
    maps.erase(node->key);
    delete node;
}

int main()
{
    LRUCache lRUCache(2);
    lRUCache.put(1, 1);              // 缓存是 {1=1}
    lRUCache.put(2, 2);              // 缓存是 {1=1, 2=2}
    cout << lRUCache.get(1) << endl; // 返回 1
    lRUCache.put(3, 3);              // 该操作会使得关键字 2 作废，缓存是 {1=1, 3=3}
    cout << lRUCache.get(2) << endl; // 返回 -1 (未找到)
    lRUCache.put(4, 4);              // 该操作会使得关键字 1 作废，缓存是 {4=4, 3=3}
    cout << lRUCache.get(1) << endl; // 返回 -1 (未找到)
    cout << lRUCache.get(3) << endl; // 返回 3
    cout << lRUCache.get(4) << endl; // 返回 4
    return 0;
}