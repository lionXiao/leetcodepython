class PerfectSquares(object):

    def numSquares(self, n):
        """
        :type n: int
        :rtype: int
        """
        if n == 0:
            return 0
        output = [0x7fffffff] * (n + 1)
        output[0] = 0
        output[1] = 1
        for i in range(2, n + 1):
            j = 1
            while (j * j <= i):
                output[i] = min(output[i], output[i - j * j] + 1)
                j = j + 1
        return output[n]

    def numSquares2(self, n):
        if n == 0:
            return 0
        output = [0x7fffffff] * (n + 1)
        loop_1 = 0
        while loop_1 * loop_1 <= n:
            output[loop_1 * loop_1] = 1
            loop_1 += 1
        for i in range(1, n + 1):
            loop_j = 1
            while i + loop_j * loop_j <= n:
                output[i + loop_j * loop_j] = min(output[i] + 1, output[i + loop_j * loop_j])
                loop_j += 1
                print(output)
        # print(output)

if __name__ == '__main__':
    sulotion = PerfectSquares()
    print(sulotion.numSquares2(19))
