# 表达式：由变量，常量和运算符组成的式子

'''
算数运算符
+ - * / %(取余) **(幂) //(取整)

算数运算表达式
1+1 2*3 a/3
功能：进行相关符号的数学运算，不会改变变量的值
值：相关数学运算结果
'''
num1 = 5
num2 = 3
print(num1 + num2)
print(num1 - num2)
print(num1 * num2)
print(num1 / num2)
print(num1 % num2)
print(num1 ** num2)
print(num1 // num2)

'''
赋值运算符和赋值运算表达式
赋值运算符 =
赋值运算表达式
格式：变量 = 表达式
功能：计算等号右侧表达式的值，并赋值给等号左侧变量
值：赋值结束后变量的值
'''
num3 = 10
num4 = num3 + 20


'''
符合运算符
+= a+=b a=a+b
-=
*=
/=
%=
**=
//=
'''

'''
if语句
if 表达式:
    语句

当程序执行到if语句时，首先计算表达式的值。
如果为真，执行if下的语句
如果为假，则跳过if语句

假：0, 0.0, '', None, False
'''

num5 = 10
num6 = 20
if num5==num6:
    num5 = 100
print("num5:",num5)