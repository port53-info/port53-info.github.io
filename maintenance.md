# 本文档用于说明如何维护该网站项目

本文档版本更新历史：
- 2023-12-19：by xw
---
# 项目说明
1. 本项目采用的是`HUGO`方案，采用了[hugoblox](https://hugoblox.com/templates/)中的`Research Group`模板，并进行一定程度的改动。更多具体使用可参考官方文档或在线搜索
2. 本项目部署在Github

# 维护方式
1. 从Github下载最新项目文件
2. 本地修改并使用`Hugo`进行测试
3. 没问题后git commit 并 push（public目录可以ignore）
4. Github部署了自动化执行，会自动生成并更新，整个过程约几分钟

# 目录结构及维护
1. src: 包含了用于将数据生成静态HTML内容的代码，该部分不是网站生成原生项目
   1. csv2html.py：用于将RFC列表的CSV内容转化成HTML表单；生成的内容自动替换目标HTML网页
      
      该文件用于更新RFC列表页面内容，在飞书将最新的数据，去除无用列，下载保存为CSV格式并按照src/data_template.csv的格式进行规整，随后运行该Python脚本会自动完成RFC列表页面的数据内容更新。
   2. status.ipynb：用于转化`Open Encrypted DNS Servers`页面内图标所需数据的代码
      
      将原始数据相关的json文件放置于同目录下，依次执行cell；相关输出用于直接替换data/Open encrypted DNS Servers/index.md中的数据；输出的内容为`变量名:数据内容`的格式，将输出的数据替换掉data/Open encrypted DNS Servers/index.md中对应变量名的数据内容即可完成更新；同时需要将提供下载的文件放在files/目录下，并修改data/Open encrypted DNS Servers/index.md最后markdown表格中的文件名与链接指向。

2. public：Hugo生成后的文件夹，即静态网站文件目录
3. imags：存放图片文件（目前没用到）
4. **conten**：网页源代码目录
      - 该目录下每个文件夹对应后续一个生成的网站路径，例如，源文件夹为`./content/test/`则使用Hugo编译后生成的目录即为http://xxxx/test
      - 每个子目录内（例如test）如果有一个名为`index.md`的文件，则该文件会被自动识别为该网页
      - 如果子目录内的文件名为`_index.md`，则该文件会被自动识别为该网页的文件，并为一个索引目录，该子文件夹内继续放置子文件夹用于编写具体页面。（e.g. data目录）
      - 网页源代码支持md以及html，且文件前几行为固定格式，用于识别该文件的一些信息，具体参考`./content/rfcs/index.md`以及官方本模板[官方使用手册](https://docs.hugoblox.com/)
5. config: 用于修改一些默认配置，例如网站title，具体参考[官方使用手册](https://docs.hugoblox.com/)
6. assets：存放一些静态资源，例如css，js等，用于自定义web页面样式、图标等；
    - 其中scss文件夹存放具体CSS代码，需要自定义的网页样式写在custom.scss文件中
    - 上述文件级别仅次于网页源文件中DOM的直接样式定义
    - 具体编写方式参考scss规范或者参考目前已有内容
    - 想要修改的id;class等可使用浏览器管理者视图进行确认
