# 小飞机
# 来源：https://www.nowcoder.com/practice/5cd9598f28f74521805d2069ce4a108a?tpId=107&tqId=33282&rp=1&ru=%2Fta%2Fbeginner-programmers&qru=%2Fta%2Fbeginner-programmers%2Fquestion-ranking
# 描述：按格式输出*的飞机

# 矩阵：6*12
for i in range(6):
    for j in range(12):
        if i==0 or i==1:
            if j==5 or j==6:
                print("*",end="")
            else:
                print(" ",end="")
        if i == 2 or i == 3:
            print("*", end="")
        if i==4 or i==5:
            if j==4 or j==7:
                print("*",end="")
            else:
                print(" ",end="")
    print() # 换行