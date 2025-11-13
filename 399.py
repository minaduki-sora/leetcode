from typing import List

class UnionFindSet:
    def __init__(self, datas=None):
        self.fa = {}
        self.rank = {}
        if datas:
            for node in datas:
                self.add(node)
    
    def add(self, node):
        """动态添加节点"""
        if node not in self.fa:
            self.fa[node] = node
            self.rank[node] = 0
    
    def find(self, node):
        """查找根节点，带路径压缩"""
        if node not in self.fa:
            self.add(node)
            
        if self.fa[node] != node:
            self.fa[node] = self.find(self.fa[node])  # 路径压缩
        return self.fa[node]
    
    def is_same_set(self, nodea, nodeb):
        """判断两个节点是否属于同一集合"""
        if nodea not in self.fa or nodeb not in self.fa:
            return False
        return self.find(nodea) == self.find(nodeb)
    
    def union(self, nodea, nodeb):
        """合并两个节点所在的集合"""
        if nodea is None or nodeb is None:
            return
            
        # 确保节点存在
        if nodea not in self.fa:
            self.add(nodea)
        if nodeb not in self.fa:
            self.add(nodeb)
            
        afa = self.find(nodea)
        bfa = self.find(nodeb)
        
        if afa == bfa:
            return  # 已经在同一集合
            
        # 按秩合并
        if self.rank[afa] < self.rank[bfa]:
            self.fa[afa] = bfa
        elif self.rank[afa] > self.rank[bfa]:
            self.fa[bfa] = afa
        else:
            self.fa[bfa] = afa
            self.rank[afa] += 1


class Solution:
    def calcEquation(self, equations: List[List[str]], values: List[float], queries: List[List[str]]) -> List[float]:
        pass