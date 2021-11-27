'''
1、树有一个根结点
2、树的子集不相交，同父异父的子集都不相交。
3、n个结点，就必有n-1条边。
结点的度degree：结点的子树个数。
树的度：树的所有结点中最大的度数。
叶结点Leaf：度为0的结点。

路径长度：连接两个结点路径所包含边的长度。
根结点在第一层，以此类推。
树的深度depth：树中所有结点中最大层次是这棵树的深度。
深度：对于任意节点n,n的深度为从根到n的唯一路径长，根的深度为0；
高度：对于任意节点n,n的高度为从n到一片树叶的最长路径长，所有树叶的高度为0；


为了让树的关系更好表达，我们用链表来完成，
但是链表按照多个指针来表示连接结构的话，会严重浪费存储空间。
例如：
一个degree为3的树，为了保证结点的统一性，每个结点都有3个指针，
n个结点就有3n个指针，但是只有n-1条边，
也就是说只有n-1个指针非空，浪费了3n -（n-1）= 2n+1个指针。

'''

# 为了避免这样的空间浪费，可以用："儿子-兄弟表示法"
# 不论度为多少的树，
# 统统只设定两个指针--（˙指向第一个儿子、指向自己的兄弟）
# 这样的方法把复杂树的结构归一化表示，
# 这样浪费的指针总是： 2n-（n-1）=n+1 个，而与树的度无关了。
# 这样的 "儿子-兄弟表示法"，
# 总是可以将复杂的树表示为二叉树。二叉树的左边是儿子，右边是兄弟。