# prometheus-py
prometheus python client demo

## 重要理解

```
关于range-vector和instant-vector
1, 只有很少一部分functions作用在range-vector，在https://prometheus.io/docs/prometheus/latest/querying/functions/ 搜索range-vector可以看出来，range-vector主要是为了基于一批数据求个斜率之类的，场景很有限.
2，大部分functions作用在instant-vector，比如sum、avg，乍一看感觉应该用在range-vector，实际上它们是对多个不同name或者不同label的instant-vector做聚合用的

关于绘制graph：
1，画图用的都是instant-vector，而不是想当然的认为一个range-vector来表达多个点，记住：range-vector存在的目的基本就是为了计算某种instant-vector，它自身没法直接用
2，prometheus画图的时候，会按一定的间隔后退时间，在每个时间点上执行query得到若干不同name和label的instant-vector，最终把同样name+label的instant-vector数据放到一组画出一条线.

关于向量运算operator：
1，只有instant-vector之间可以加减乘除运算，这和sum,avg的原理一样，是用于不同name or label的instant-vector之间的运算
2，vector之间做运算，分成2个步骤：先匹配，后运算。
两个name不同label不同的instant-vector做运算，必须先经过on/ignoring实现label的统一，这样就完成了"匹配"。
运算则需要考虑，左侧vector和右侧vector，在记录数量上谁多谁少，如果左侧多那么就要group_left(相当于left join, n:1关系)，否则就用group_right(相当于right join, 1:n关系)，如果你不指定，那么应该会因为无法1:1 join而报错。
```
