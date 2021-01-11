# 缩短二进制
# 来源：https://www.nowcoder.com/practice/4ffcc9f206b949ddb057ee0099b34d51?tpId=107&tqId=33282&rp=1&ru=%2Fta%2Fbeginner-programmers&qru=%2Fta%2Fbeginner-programmers%2Fquestion-ranking
# 输出描述：十进制整数1234对应的八进制和十六进制（字母大写），用空格分开，并且要求，在八进制前显示前导0，在十六进制数前显示前导0X。
# 使用进制转化函数：
#   二进制：bin()
#   八进制：oct()
#   十六进制:hex()


# 当前十进制的数字：1234
dec=1234
oct=oct(dec).replace("o","")    # 删除八进制转化代入的0x
hex=hex(dec).upper()
print(oct,hex)

#print("0"+"%o" % 1234)
#print("0"+"%X" % 1234)