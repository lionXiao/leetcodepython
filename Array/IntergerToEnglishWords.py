class InterToEnglistWords(object):
    def num2str(self, num):
        ge = ("", "One", "Two", "Three", "Four", "Five", "Six", "Seven", "Eight", "Nine", "Ten", "Eleven", "Twelve",
                  "Thirteen", "Fourteen", "Fifteen", "Sixteen", "Seventeen", "Eighteen", "Nineteen") # 不超过19的正整数表达
        shi = ("", "", "Twenty", "Thirty", "Forty", "Fifty", "Sixty", "Seventy", "Eighty", "Ninety") # 十位不小于2的表达
        ans = ""
        gewei, shiwei, baiwei = num % 10, (num//10) % 10, num // 100 # # 把数分成个位, 十位, 百位
        pre = 0 # 先前是否有非0数的标记
        if baiwei != 0:
            pre = 1
            ans = ans + ge[baiwei] + "hundred"
        if shiwei > 1: # 十位数大于1, 单独表达
            if pre:
                ans = ans + " " # 先前已有非零数, 添加空格
            pre = 1
            ans = ans + shi[shiwei]
        if shiwei == 1 or gewei != 0: # 十位和个位数小于20的正整数是, 一起表达
            if shiwei == 1:
                gewei = gewei + 10
            if pre:
                ans = ans + " " # 先前已有非0数, 添加空格
            ans = ans + ge[gewei]
        return ans

    def number2words(self, num):
        if num == 0:
            return "zero"
        rear = ["", "Thousand", "Million", "Billion"]
        nums = []
        for i in range(4):
            nums.append(num % 1000)
            num = num // 1000
        ans = ""
        pre = 0
        count = len(nums) - 1
        print(nums)
        while count >= 0:
            if not nums[count]:
                count -= 1
                continue
            if pre:
                ans = ans + " "
            print(ans)
            print(count)
            pre = 1
            ans = ans + self.num2str(nums[count]) + rear[count]
            count -= 1
        return ans

if __name__ == "__main__":
    inter2words = InterToEnglistWords()
    print(inter2words.number2words(987))

