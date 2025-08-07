# 抓包分析

![image-20250807174219556](./assets/image-20250807174219556.png)

抓包分析一下

感觉没啥值得关注的

直接转python代码发包

![image-20250807175536326](./assets/image-20250807175536326.png)

这里我选择的是翻页逻辑

他的数据是直接返回html的，我测试发现cookies如果注释就拿不到了；所以需要处理cookies

![image-20250807175939047](./assets/image-20250807175939047.png)

测试发现sessionid不重要，主要是上面两个



清掉cookies重新抓包



# cookies处理

