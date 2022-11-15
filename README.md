# FFxivTrpgDice
 一个最终幻想14与海豹掷骰核心的中转器，让trpg骰娘直接为游戏提供掷骰服务

大陆内版本readme，有图片
https://kdocs.cn/l/clxpwKUeG532

![](https://raw.githubusercontent.com/kagangtuya-star/picgo1/main/FFxivTrpgDice20221115131726.png)

![](https://raw.githubusercontent.com/kagangtuya-star/picgo1/main/FFxivTrpgDice20221115131739.png)



### 依赖

本工具依赖于以下程序

发送消息的鲶鱼精邮差

[Natsukage/PostNamazu: 鲶鱼精邮差，最终幻想14 触发器拓展 (github.com)](https://github.com/Natsukage/PostNamazu)

接受消息的高级触发器插件，挂载于CafeACT或呆萌ACT

[[ACT\][持续更新] Advanced Combat Tracker 国服整合版 | 第一时间适配国服更新 | 按需安装，自动更新 [CafeACT] NGA玩家社区](https://bbs.nga.cn/read.php?tid=17412506)

[[萌新科技\][ACT] ACT.呆萌.[国服|国际服]非绿色化整合 [持续更新] / 第一时间赶到现场适配国服&国际服客户端 NGA玩家社区](https://bbs.nga.cn/read.php?tid=19019884)

处理骰点数据的海豹骰子核心

[SealDice - 海豹TRPG骰点核心 (weizaima.com)](https://dice.weizaima.com/)

### 原理

![](https://raw.githubusercontent.com/kagangtuya-star/picgo1/main/FFxivTrpgDice%E7%8B%92%E7%8B%92%E9%AA%B0%E5%AD%90.png)

若程序监听17777端口，鲶鱼精邮差监听2020端口则有如下三个api可用，程序实现原理为互相内部调用

详见

[FFxivTrpgDice接口文档](https://blog.kagangtuya.top/other_html/FFxivTrpgDice接口文档.html?target_id=001)

### Python运行

安装python和git

`git clone https://github.com/kagangtuya-star/FFxivTrpgDice.git`

`cd FFxivTrpgDice`

`pip install -r requirements.txt -i  https://pypi.tuna.tsinghua.edu.cn/simple`

`python main.py`

### windows平台运行

**此exe程序可在win10以上系统运行，win7可能不一定能运行，32位系统肯定不能运行。**

点此 [Releases ](https://github.com/kagangtuya-star/FFxivTrpgDice/releases)或 [百度云盘](https://pan.baidu.com/s/1XOszQGIIXiSyKfyzJNkSfw?pwd=ecr9) 下载压缩包解压后双击exe即可，**如果闪退就是你没解压完，exe文件同文件夹下需有config.json 配置文件才能运行**

![](https://raw.githubusercontent.com/kagangtuya-star/picgo1/main/FFxivTrpgDice20221115132902.png)

此外，你需要

**向act的高级触发器导入骰子转发的触发器**

点 [掷骰指令发送器.xml](https://github.com/kagangtuya-star/FFxivTrpgDice/releases/download/FFxivTrpgDice1.0/default.xml) 或者从上一步的压缩包里 下载，导入方法（以CafeAct为例子，呆萌act同理）

![](https://raw.githubusercontent.com/kagangtuya-star/picgo1/main/FFxivTrpgDice20221115133052.png)

![](https://raw.githubusercontent.com/kagangtuya-star/picgo1/main/FFxivTrpgDice20221115133157.png)

![](https://raw.githubusercontent.com/kagangtuya-star/picgo1/main/FFxivTrpgDice20221115133234.png)



**安装鲶鱼精邮差，并在2020端口启动**

win10可用，其他没测

点击这里下载 [鲶鱼精邮差](https://github.com/Natsukage/PostNamazu/releases) 解压，将其中的dll文件放在妥善的地方，每一次act启动都会从那里加载

![](https://raw.githubusercontent.com/kagangtuya-star/picgo1/main/FFxivTrpgDice20221115133413.png)

![](https://raw.githubusercontent.com/kagangtuya-star/picgo1/main/FFxivTrpgDice20221115133632.png)

![](https://raw.githubusercontent.com/kagangtuya-star/picgo1/main/FFxivTrpgDice20221115133654.png)

![](https://raw.githubusercontent.com/kagangtuya-star/picgo1/main/FFxivTrpgDice20221115133753.png)

如此，就可以在游戏内使用掷骰功能了，它可以自动匹配每一个频道的。或.前缀的指令，并回复，你可以在act的触发器里自行选择一些频道是否启用。

### 有时候接收到消息但不回复怎么办？

因为海豹api的token过期了，而且它每秒只能触发1次，请考虑自行搭建并抓取api，抓一次如果海豹不关闭的话能用很长时间！

**注意，海豹的回复语得是 <玩家名> 骰出了xx的才可以，我是根据<和>来把将海豹核心的掷骰结果与狒狒的玩家名拼起来的，如果不是就可能报错（但默认的都是，如果你没改成什么{$t玩家_RAW}的话）**

抓api是这样的，打开海豹webui，怎么安装海豹看海豹官网

基本设置添加master UI:1001 保存

![image-20221115134547319](C:\Users\chenzihan\AppData\Roaming\Typora\typora-user-images\image-20221115134547319.png)

进入指令测试界面

![image-20221115134621286](C:\Users\chenzihan\AppData\Roaming\Typora\typora-user-images\image-20221115134621286.png)

按f12进入开发者模式，我用的是win10自带的edge浏览器

![image-20221115134912243](C:\Users\chenzihan\AppData\Roaming\Typora\typora-user-images\image-20221115134912243.png)

![](https://raw.githubusercontent.com/kagangtuya-star/picgo1/main/FFxivTrpgDice20221115135343.png)

打开exe文件目录下的config.json

![image-20221115135617462](C:\Users\chenzihan\AppData\Roaming\Typora\typora-user-images\image-20221115135617462.png)

如此完成

### 我想记录跑团log！

[[幻想科技\] [补档]ACT聊天记录加载器 178](https://nga.178.com/read.php?tid=31940289&rand=201)

[FFX|V 日志查看器 (orz.tools)](https://ffxivlog.orz.tools/)

[MadYeling/Logs_Chat_Record_Extractor: ACT聊天记录加载器 (github.com)](https://github.com/MadYeling/Logs_Chat_Record_Extractor)

随便找一个就行，就是不能染色，毕竟狒狒嘛

### 我想让狒狒跑团体验更好！

[dream2.0 画质补丁](https://www.bilibili.com/video/BV1bF411J7QQ/)

玩家间的聊天气泡 卫月框架（[注入器](https://bbs.tggfl.com/topic/32/dalamud-%E5%8D%AB%E6%9C%88%E6%A1%86%E6%9E%B6) 或者好用的第三方登录器[XIVLauncherCN](https://ottercorp.github.io/) ）国服库的 ChatBubbles 插件

![](https://raw.githubusercontent.com/kagangtuya-star/picgo1/main/FFxivTrpgDice20221115140544.png)
