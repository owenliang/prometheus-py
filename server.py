# -*- coding: utf-8 -*-

from prometheus_client import Counter, Gauge, Histogram, Summary, start_http_server, Histogram
import time
import random

# 定义4种metrics例子
c = Counter('cc', 'A counter')
g = Gauge('gg', 'A gauge')
h = Histogram('hh', 'A histogram', buckets=(-5, 0, 5))
s = Summary('ss', 'A summary', ['label1', 'label2'])  # metrics名字, metrics说明, metrics支持的label

# 在线程中启动http服务, 供metrics抓取
start_http_server(8000)

#
while True:
    # counter:  只增不减
    c.inc()

    # gauge: 任意值
    g.set(random.random())

    # histogram: 任意值, 会给符合条件的bucket增加1次计数
    h.observe(random.randint(-10, 10))

    # summary：任意值, python client不支持summary的百分位统计, 其他语言的client也许支持, 但一般不建议用, 性能和场景都有局限
    s.labels('a', 'b').observe(17)

    time.sleep(1)
