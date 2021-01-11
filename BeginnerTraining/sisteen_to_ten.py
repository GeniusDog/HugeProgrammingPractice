# 十六进制转十进制
# 来源：https://www.nowcoder.com/practice/33e148570d5c4e728116e2f861638c9c?tpId=107&tqId=33282&rp=1&ru=%2Fta%2Fbeginner-programmers&qru=%2Fta%2Fbeginner-programmers%2Fquestion-ranking
# 描述：BoBo写了一个十六进制整数ABCDEF，他问KiKi对应的十进制整数是多少。
# 输出：十六进制整数ABCDEF对应的十进制整数，所占域宽为15。

dec=int("ABCDEF",16)
print("%15d" % dec)