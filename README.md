# E-Bike

## 概述

校园电动车服务微信小程序后端，基于Django实现。

## 快速开始

克隆项目

```shell
git clone https://github.com/tangjzh/EBike.git

cd EBike
```

创建环境并装依赖

```shell
conda create -n ebike python=3.10
conda activate ebike
pip install -r requirements.txt
```

创建数据库和索引

```shell
python manage.py makemigrations
python manage.py migrate
python manage.py rebuild_index
```

创建超级用户（可选）

```shell
python manage.py createsuperuser
```

运行后端服务

```shell
python manage.py runserver
```

## API文档

运行后端后，你将在控制台看到：

```shell
Starting ASGI/Channels version 3.0.4 development server at http://127.0.0.1:8000/
```

打开网址 `http://127.0.0.1:8000/doc` 查看 api 文档。

该文档并不全面，因为由Swagger生成的文档可能无法捕捉手写的处理函数。

你可以查看 `test/` 目录中的测试样例来进一步了解这些 API。

## 其它

注意，后端配置了 JWT 认证，这意味着所有请求都需要附带一个 authToken。

要使用 VSCode 运行 .http 文件进行测试，请先安装 REST Client 插件。