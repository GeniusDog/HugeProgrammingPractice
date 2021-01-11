# 成绩输入输出
# 来源：https://www.nowcoder.com/practice/eb49750ef0de47168c21761de086d97c?tpId=107&tqId=33282&rp=1&ru=%2Fta%2Fbeginner-programmers&qru=%2Fta%2Fbeginner-programmers%2Fquestion-ranking
# 描述：输入3科成绩，然后把三科成绩输出，成绩为整数形式。
# 输入：一行，3科成绩，用空格分隔，范围（0~100）
# 输出：一行，把3科成绩显示出来，输出格式详见输出样例。
# 如：score1=60,score2=80,score3=90

score=input().split(" ")
for i in range(len(score)):
    if i<2:
        print("score%d=%d," % (i+1,int(score[i])),end="")
    else:
        print("score%d=%d" % (i+1,int(score[i])),end="")
print()