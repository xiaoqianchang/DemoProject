class Solution:
    """
    输入一个整数，输出该数二进制表示中1的个数。其中负数用补码表示。
    PS:该方式对负数有问题
    由源码分析可知，Python3 整数对象存储为无符号数加上符号位标志，所以不存在“负数”补码形式，因此，计算 “1” 的数量需要按去符号后的无符号数：cnt=bin(n).count('1')
    另外，Python3 无长整，整数长度原则上不限，所以不能以假定的 32 位处理。
    """
    def NumberOf1(self, n):
        # write code here
        cnt = 0
        if n < 0:
            n = n & 0xffffffff
        while n:
            cnt += 1
            n = (n - 1) & n
        return cnt

    # bin函数： bin返回一个整数的二进制字符串，以0b开头，
    # bin(10) '0b1010'  bin(-10)  '-0b1010'
    #
    # count函数 返回字符串当中非重叠的字符串的个数，可以传入start，end来表示对字符串切片的结果
    #
    # 如果一个数为负数，那么2**32 + n 然后再用bin返回的就是它的补码形式。 补码+源码=2**32
    def NumberOf1_strong1(self, n):
        if n >= 0:
            return bin(n).count('1')
        else:
            return bin(2**32 + n).count('1')


    def NumberOf1_strong2(self, n):
        """
        该方法对正数有效，负数无效
        :param n:
        :return:
        """
        count = 0
        while n:
            if n & 1 == 1:
                count += 1
            n >>= 1
        return count


if __name__ == '__main__':
    solution = Solution()
    n = 100
    # print(solution.NumberOf1(n))
    print(solution.NumberOf1_strong1(n))
    print(solution.NumberOf1_strong2(n))
    print(bin(n))
    # 上面的方法可以如下取得
    print(bin(n).count('1'))

