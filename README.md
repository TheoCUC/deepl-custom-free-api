# deepl-custom-free-api

该项目借鉴于 [reycn/deepl-custom-server-for-bob](https://github.com/reycn/deepl-custom-server-for-bob) , 由于原项目没跑通, 刚好在学爬虫和Docker, 就试着换了selenium库来做一下. 

Docker部分写的不是很好, 由于刚学了一点点皮毛, 还不会容器里的通信什么的, 所以只能比较粗糙的做一下.

## 使用方法

1. clone本仓库
2. 构建镜像, 由于构建过程需要联网, 因此使用host网络
```
docker build -t test/deeplapi . --network host
```
3. 运行容器, 这里也使用host网络好了, 端口默认是是6888, 好像可以通过ARG传入参数, 以后再研究研究
```
docker run -itd --network=host test/seleniumpy
```
4. 在Bob插件中配置API地址为 `IP:6888` 即可
