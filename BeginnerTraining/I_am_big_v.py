# 我是大V
# 来源：https://www.nowcoder.com/practice/5c329570ba034871a96299df21e80e51?tpId=107&tqId=33282&rp=1&ru=%2Fta%2Fbeginner-programmers&qru=%2Fta%2Fbeginner-programmers%2Fquestion-ranking
# 描述：要求输出由小写字母v组成的大V。
# v   v
#  v v
#   v

# 矩阵的行、列
row=3
cow=5
mid=cow/2

# 循环输出:3*5的矩阵
for i in range(row):
    for j in range(cow):
        if j<=mid:
            # 矩阵的左半部分
            if j-i==0:
                print("v",end="")
            else:
                print(" ",end="")
        else:
            # 矩阵的右半部分
            if cow-j-1==i:
                print("v",end="")
            else:
                print(" ",end="")
    print() # 一行结束

