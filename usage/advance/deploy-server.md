---
order: 3
---
# 部署自定义同步服务器

PotatoVN 同步服务器是一个用于帮助PotatoVN跨电脑同步/备份数据的服务器，它提供了一个RESTful API用于客户端与服务器之间的通信。

它能同步什么：[请参考potatovn wiki](/usage/advance/data-exchange)

:::tip

手动部署服务器需要具有一定的服务器使用经验。建议没有特殊需求的用户使用[官方服务器](/usage/how-to-use/sync-games)~

:::

## 前置要求

要部署自定义PoatoVN同步服务器，你需要有以下东西：

* **兼容AWS S3的内容分发服务**（用来存储同步的图片、未来可能添加的游戏存储功能等）（如[MinIO](https://min.io/)、[Cloudflare R2](https://www.cloudflare.com/zh-cn/developer-platform/products/r2/)、[腾讯云对象存储](https://cloud.tencent.com/product/cos)、[七牛云](https://developer.qiniu.com/kodo/4086/aws-s3-compatible)等）（事实上基本上所有内容分发服务都兼容AWS S3 API）
* **一台7x24小时开机的电脑**（服务器）——先生，你也不希望忘记打开服务器而同步失败吧（bushi）
* **服务器要能够访问公网**（除非你在内网自建了内容分发服务器）

## 推荐部署方式：Docker (Compose)

1. 确保服务器上安装了docker
2. 在服务器任意位置创建一个文件夹，它将用来存放docker-compose.yml文件及数据库数据。**以下操作均在此文件夹内进行**。
3. 下载docker-compose.yml文件：

```shell
curl -O https://raw.githubusercontent.com/GoldenPotato137/PotatoVN/refs/heads/dev/GalgameManager.Server/docker-compose.yml
```

> 国内服务器在访问github时可能会遇到网络问题，可以使用代理解决这个问题，或者直接下载docker-compose.yml文件到本地，然后上传到服务器。

3. 修改docker-compose.yml里必填内容，该文件内包含详细注释，按照注释填写即可。

```shell
nano docker-compose.yml
```

4. 新建一个 `data`文件夹，并修改其权限，其用于存放数据库数据。

```shell
mkdir data
sudo chown -R 1001:1001 ./data
```

5. 测试性启动服务

```shell
sudo docker-compose up
```

检查是否正常启动，尝试用potatovn客户端链接服务器。如果你没有修改docker-compose.yml文件中的端口，
那么potatovn中应该输入的服务器地址为 `http://你的服务器地址:8080` （如： http://192.168.114.114:8080）。

6. 如果一切正常，按 `Ctrl+C`停止服务，然后使用以下命令正式启动服务：

```shell
sudo docker-compose down
sudo docker-compose up -d
```

7. （可选）使用https保护你的服务器，自行使用任何你喜欢的反向代理工具代理服务即可，如Nginx、Caddy等。

以下为一个简单的使用Caddy的配置文件示例：

```plaintext
your.domain.name {
    reverse_proxy localhost:8080
    encode zstd gzip
}
```

## 二进制部署

> 请注意，二进制部署需要你自行安装并配置PostgreSQL数据库，以及设置环境变量。

该部分文档TODO

## 在测试环境中运行

初始化用户密钥:

```shell
dotnet user-secrets init
```

设置各类环境变量：

```shell
dotnet user-secrets set "Key" "Value"
```

应该设置的环境变量有（Key）：

* `ConnectionStrings:DefaultConnection` 数据库连接字符串，**数据库必须是PostgreSQL**
* `AppSettings:JwtKey` JWT秘钥，**至少64位长**
* `AppSettings:Minio:EndPoint` 兼容AWS S3的OSS（对象存储）服务器地址与端口, 如: 114514.moe:1919
* `AppSettings:Minio:AccessKey` AWS S3 OSS用户识别码
* `AppSettings:Minio:SecretKey` AWS S3 OSS用户密钥

可以选填的环境变量有：

* `AppSettings:Minio:BucketName` AWS S3 OSS存储桶名称，默认为 `potatovn`，如果你创建的桶的名字不是 `potatovn`，你需要设置这个环境变量为你的桶的名字
* `AppSettings:Minio:UseSSL` 是否使用SSL，默认为 `false`，如果你的兼容AWS S3 OSS服务器配置了SSL，可以设置这个环境变量为 `true`
* `AppSettings:Bangumi:OAuth2Enable` 是否作为Bangumi OAuth2认证服务器，默认为 `false`，
  如果填写为 `true`则必须设置AppId和AppSecret
* `AppSettings:Bangumi:AppId` Bangumi第三方应用的AppId
* `AppSettings:Bangumi:AppSecret` Bangumi第三方应用的AppSecret
* `AppSettings:User:Default` 是否允许用户以用户名密码注册与登录，默认为 `true`
* `AppSettings:User:Bangumi` 是否允许用户使用Bangumi账号注册与登录，默认为 `false`
* `AppSettings:User:OssSize` OSS上每位用户的存储空间大小，单位为byte，默认为 `104857600`（100MB），此数值最大为2^63-1 (8388608TB)
