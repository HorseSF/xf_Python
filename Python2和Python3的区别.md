# Python2和Python3的区别

***

## 八进制区别

+ Python2里，0o开始的数字是八进制，以0开始的数字也是八进制
+ Python3里不能以0开始表示八进制

***

## 除法运算符的区别

+ Python2里，两个整数相除的结果是一个整数
+ Python3里，两个整数相除的结果是一个浮点数

***

## 比较运算符

+ Python3里，不在支持<>比较运算符

***

## 字符串的表示方式

+ Python2里可以使用反引号表示原生字符
+ Python3里不再支持

***

## 新式类和经典类

+ 经典类：不继承自object的类，称之为经典类
+ 新式类：继承自object的类
+ Python3不再支持经典类，一个类不指定父类的话，默认都是继承自object

***

## 中文的支持

+ Python2默认不支持中文，需要写注释

```Python2
# -*- coding:utf-8 -*-
```
+ Python3支持中文

***

## print 语句的区别

+ Python2里支持以下写法

```Python2
print 'hello'
```
+ Python3里不再支持以上写法

***

## input语句的区别

+ Python2里的input会把用户的输入当做代码。根据输入内容确定变量类型。
+ Python3直接接受用户的输入。所有的输入内容都是String类型。
+ Python2里的raw_input和Python3里的input功能一致。