# 关于本项目：

​		想必你已经受够了kikoeru网站自带的垃圾下载，创建本项目的初衷就是为了解决kikoeru下载的问题，但是本项目不提倡对于该网站的批量爬取

​		scrapy的异步携程的下载速度非常快，同时也会对于其网站的下载服务器造成较大压力（本来就是白嫖，就不要给人家搞出问题了，恼）（某次打开ua黑了，恼）

## 使用：

​		在[Release v1.1 · ChuangSR/KikoeruDownload (github.com)](https://github.com/ChuangSR/KikoeruDownload/releases/tag/v1.1) 中进行下载，本项目已使用pyinstaller打包为exe，无图形界面，仅仅支持命令运行，同时，本项目不支持将kikoeru.exe所在的目录配置到PATH中（本人对于pyinstaller并不熟悉，会出现bug），所有每次运行请在kikoeru.exe所在的位置打开cmd运行

### -u参数：

​		指定下载的音频

```
kikoeru.exe -u https://www.asmr.one/work/RJXXXXXXX
```

​		以上是最简单的下载方法

```
kikoeru.exe -u RJXXXXXXX
```

​		也可以仅仅是一个RJ号，但是请保证其存在于网站

### -p参数：

​		指定下载的路径

```
kikoeru.exe -u https://www.asmr.one/work/RJXXXXXXX -h D://xxx
```

### -l参数：

​		指定下载的语言偏好，此项并不准确，该网站部分返回情况下返回的数据可能存在错误，同时偏好还受到config.ini中配置的影响，但是此属性大于config.ini中的配置

```
kikoeru.exe -u https://www.asmr.one/work/RJXXXXXXX -h D://xxx -l JZ
```

#### 支持参数：

```
JZ 简中 FZ 繁中 JP 日语 EG 英语
```

#### 错误的参数：

​		如果输入了错误的参数，那么下载器将根据当前的RJ号进行下载

## config.ini:

​		这个是本项目的配置文件

```
[url]
URL=https://www.asmr.one/work/
[api]
WORK_INFO_API=https://api.asmr-200.com/api/workInfo/
TRACKS_API=https://api.asmr-200.com/api/tracks/
[proxy]
#请将使用xxx.xxx.xxx:port的形式
#或者你可以使用全局代理模式
IP=
[language]
#默认的下载语言
#注意此处的配置并不可靠
#该网站返回信息中可能会存在部分错误
#所以请尽量输入所需ASMR的url
#参数为:JZ简中 FZ繁中 JP日语 EG英语
#如果你输入了不属于配置中的语言类型，那么会默认下载当前url
LANGUAGE=JZ
[path]
#文件保存的路径
SAVE_PATH=
[user_agent]
USER_AGENT=User-Agent:Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36
```

​		url参数为网站的网址+/work，api中的参数为网站信息返回的接口（如果出现更换请自行提取）

### 文件默认存储路径：

​		请修改SAVE_PATH的值

## 关于代理：

​		配置文件中的代理参数未经过测试，预计会出现bug（我似乎并不想修），所以请使用代理类软件进行全局代理

## 关于网站拒绝连接：

​		请尝试更换USER_AGENT的值亦或者是你的IP地址（我本来不想写这一段的，恼）
