# 学生基本信息输入输出
# 来源：https://www.nowcoder.com/practice/58b6a69b4bf943b49d2cd3c15770b9fd?tpId=107&tqId=33282&rp=1&ru=%2Fta%2Fbeginner-programmers&qru=%2Fta%2Fbeginner-programmers%2Fquestion-ranking
# 输入：学号以及3科成绩，学号和成绩之间用英文分号隔开，成绩之间用英文逗号隔开。
# 输出：学号，3科成绩，输出格式详见输出样例。
# 如：
# input：   17140216;80.845,90.55,100.00
# output：  The each subject score of  No. 17140216 is 80.85, 90.55, 100.00.
# 注意个数输出四舍五入进位是个概率性事件

from decimal import Decimal

student_input=input().split(";")
student_id=student_input[0]
student_score=student_input[1].split(",")
a=Decimal(student_score[0]).quantize(Decimal('0.00'))
b=Decimal(student_score[1]).quantize(Decimal('0.00'))
c=Decimal(student_score[2]).quantize(Decimal('0.00'))



print("The each subject score of  No. %s is %s,%s,%s."
      % (student_id,a,b,c))