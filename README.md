# AutoPocTest
AutoPocTest是一个由x1uq1n9开源的漏洞检测框架，使用Python3开发，自动调用网络空间安全搜索引擎，目前只支持fofa，其他引擎有待开发。

基本兼容网上绝大部分poc与exp；使用协程，轻量化，可满足在大多数场景下使用

## 安装
- 从Git上获取最新版本的AutoPocTest代码
- 自行搭建Python3环境
- 安装Python包


    $ cd AutoPocTest
    
    $ pip install -r requirements.txt
    
## 配置
- 如果没有FoFaApi的，可以将自己的fofa账号Cookie放入`user/COOKIES`文件中，免费爬取前五页内容；
- 如果有FoFaApi的，在`main.py`中设置`USE_FofaApi`为`True`，然后填写自己的相关信息即可
- 把POC或者EXP脚本放入`plugins`文件夹中，把脚本添加一个接收URL的参数
- 配置`main.py`中的`query`值为需要在`fofa`中搜索的漏洞指纹; 在`FUNCTION`变量中调用exp/poc

## 运行
    $ python3 AutoPocTest.py