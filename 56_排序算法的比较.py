'''
排序方法比较：

    简单排序：
        1、选择排序
        2、冒泡排序
        3、插入排序
    复杂排序：
        1、希尔排序（插入排序改进）
        2、堆排序
        3、快速排序
        4、归并排序
        5、基数排序
'''
'''
一般跳着交换的就会不稳定。

        排序方法       平均时间复杂度  最坏情况时间复杂度  额外空间复杂度  稳定性             
    简单排序：
        1、选择排序      O(N^2)         O(N^2)          O(1)          不稳定
        2、冒泡排序      O(N^2)         O(N^2)          O(1)          稳定
        3、插入排序      O(N^2)         O(N^2)          O(1)          稳定
    复杂排序：
        1、希尔排序      O(N^d)         O(N^2)          O(1)          不稳定
        2、堆排序        O(NlogN)       O(NlogN)        O(1)          不稳定
        3、快速排序      O(NlogN)       O(N^2)          O(logN)       不稳定 
        4、归并排序      O(NlogN)       O(NlogN)        O(N)          稳定
        5、基数排序      O(P(N+B)       O(P(N+B)        O(N+B)        稳定
'''