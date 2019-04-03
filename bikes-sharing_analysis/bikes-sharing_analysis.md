# 探索美国共享单车数据

## 自行车共享数据

在过去十年内，自行车共享系统的数量不断增多，并且在全球多个城市内越来越受欢迎。自行车共享系统使用户能够按照一定的金额在短时间内租赁自行车。用户可以在 A 处借自行车，并在 B 处还车，或者他们只是想骑一下，也可以在同一地点还车。每辆自行车每天可以供多位用户使用。

由于信息技术的迅猛发展，共享系统的用户可以轻松地访问系统中的基座并解锁或还回自行车。这些技术还提供了大量数据，使我们能够探索这些自行车共享系统的使用情况。

在此项目中，你将使用 [Motivate](https://www.motivateco.com/) 提供的数据探索自行车共享使用模式，Motivate 是一家入驻美国很多大型城市的自行车共享系统。你将比较以下三座城市的系统使用情况：芝加哥、纽约市和华盛顿特区。

## 数据集

数据包括美国三座城市（芝加哥，纽约和华盛顿） 2017 年上半年的数据。

三个数据文件都包含相同的核心**六 (6)** 列：

- 起始时间 Start Time（例如 2017-01-01 00:07:57）
- 结束时间 End Time（例如 2017-01-01 00:20:53）
- 骑行时长 Trip Duration（例如 776 秒）
- 起始车站 Start Station（例如百老汇街和巴里大道）
- 结束车站 End Station（例如塞奇威克街和北大道）
- 用户类型 User Type（订阅者 Subscriber/Registered 或客户Customer/Casual）

芝加哥和纽约市文件还包含以下两列（数据格式可以查看下面的图片）：

- 性别 Gender
- 出生年份 Birth Year

原始文件（访问地址：([芝加哥](https://www.divvybikes.com/system-data)、[纽约市](https://www.citibikenyc.com/system-data)、[华盛顿特区](https://www.capitalbikeshare.com/system-data)）有很多列，并且在很多方面格式不一样。我们执行了一些[数据整理](https://en.wikipedia.org/wiki/Data_wrangling)操作，使这些文件压缩成上述核心六大列，以便于更直接地使用 Python 技能进行评估和分析。

![img](https://s3.cn-north-1.amazonaws.com.cn/u-img/015d05eb-ec77-4adb-a0c1-20494f1fa169)

## 问题

你将编写代码并回答以下关于自行车共享数据的问题：

[代码在这里](src/bikeshare.py)

这里选用**芝加哥城市数据**进行分析，月份和工作日全部包括，输出结果如下：

```shell
Hello! Let's explore some US bikeshare data!

Please input the city you want to analyza: chicago

Please input the month you want to analyza: all

Please input the day you want to analyza: all
----------------------------------------

Calculating The Most Frequent Times of Travel...

The most common month:  June
The most common day of week:  Tuesday
The most common start hour:  17

This took 0.23366641998291016 seconds.
----------------------------------------

Calculating The Most Popular Stations and Trip...

The most commonly used start station:  Streeter Dr & Grand Ave
The most commonly used end station:  Streeter Dr & Grand Ave
The most commonly frequent combination of start station and end station trip:  Lake Shore Dr & Monroe StStreeter Dr & Grand Ave

This took 0.1433701515197754 seconds.
----------------------------------------

Calculating Trip Duration...

Display total travel time:  280871787
Display maen travel time:  936.23929

This took 0.003118276596069336 seconds.
----------------------------------------

Calculating User Stats...

Display counts of user types:
 Subscriber    238889
Customer       61110
Dependent          1
Name: User Type, dtype: int64
Display counts of gender:
 Male      181190
Female     57758
Name: Gender, dtype: int64
Display earliest, most recent, and most common year of birth: 1899.0 2016.0 1989.0

This took 0.12210416793823242 seconds.
----------------------------------------
```

下面的问题可以被回答为：

1. 起始时间（Start Time 列）中哪个月份最常见？

   June，六月

2. 起始时间中，一周的哪一天（比如 Monday, Tuesday）最常见？ 提示：可以使用 `datetime.weekday()` （点击[查看文档](https://docs.python.org/3/library/datetime.html#datetime.date.weekday)）

   Tuesday，星期二

3. 起始时间中，一天当中哪个小时最常见？

   17时。

4. 总骑行时长（Trip Duration）是多久，平均骑行时长是多久？

   总时长：280871787s，平均时长：936.23929s。

5. 哪个起始车站（Start Station）最热门，哪个结束车站（End Station）最热门？

   最热门起始车站：Streeter Dr & Grand Ave， 最热门结束车站： Streeter Dr & Grand Ave

6. 哪一趟行程最热门（即，哪一个起始站点与结束站点的组合最热门）？

   最热门行程：Lake Shore Dr & Monroe 至 StStreeter Dr & Grand Ave

7. 每种用户类型有多少人？

   Subscriber    238889
   Customer       61110
   Dependent          1

8. 每种性别有多少人？

   Male      181190
   Female     57758

9. 出生年份最早的是哪一年、最晚的是哪一年，最常见的是哪一年？

   出生年份最早是1899.0，最晚是2016.0，最常见是1989.0
