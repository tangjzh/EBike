---
description: 后端接口定义文档用于定义后端服务的接口，包括接口的URL、请求方法（如GET、POST等）、请求参数、返回数据格式。
---

# 🔌 后端接口定义

## 1 概述

本文档是软件后端接口定义文档，遵循Swagger2.0协议，是对Swagger自动生成的API文档的详细标注。该文档主要起到如下作用：

* 对开发团队/第三方开发者
  * 前端可以根据本文档进行后端接口调用
  * 测试可以根据本文档进行接口测试
  * 后端可以参考该文档进行迭代开发
* 对用户
  * 用户可以了解后端系统的可用功能

本文档由 [唐锦洲](https://app.gitbook.com/u/eDuOQyxxq5RjDyaODgK5zwjGuh33 "mention") 负责编写。

## 2 用户模块

### 2.1 用户注册和登录

{% swagger src="https://raw.githubusercontent.com/tangjzh/EBike/master/swagger.yaml" path="/users/login/" method="post" %}
[https://raw.githubusercontent.com/tangjzh/EBike/master/swagger.yaml](https://raw.githubusercontent.com/tangjzh/EBike/master/swagger.yaml)
{% endswagger %}

{% swagger src="https://raw.githubusercontent.com/tangjzh/EBike/master/swagger.yaml" path="/users/register/" method="post" %}
[https://raw.githubusercontent.com/tangjzh/EBike/master/swagger.yaml](https://raw.githubusercontent.com/tangjzh/EBike/master/swagger.yaml)
{% endswagger %}

{% swagger src="https://raw.githubusercontent.com/tangjzh/EBike/master/swagger.yaml" path="/users/refresh/" method="post" %}
[https://raw.githubusercontent.com/tangjzh/EBike/master/swagger.yaml](https://raw.githubusercontent.com/tangjzh/EBike/master/swagger.yaml)
{% endswagger %}

### 2.2 用户个人信息

{% swagger src="https://raw.githubusercontent.com/tangjzh/EBike/master/swagger.yaml" path="/users/profile/" method="get" %}
[https://raw.githubusercontent.com/tangjzh/EBike/master/swagger.yaml](https://raw.githubusercontent.com/tangjzh/EBike/master/swagger.yaml)
{% endswagger %}

{% swagger src="https://raw.githubusercontent.com/tangjzh/EBike/master/swagger.yaml" path="/users/profile/{id}/" method="get" %}
[https://raw.githubusercontent.com/tangjzh/EBike/master/swagger.yaml](https://raw.githubusercontent.com/tangjzh/EBike/master/swagger.yaml)
{% endswagger %}

{% swagger src="https://raw.githubusercontent.com/tangjzh/EBike/master/swagger.yaml" path="/users/profile/{id}/" method="put" %}
[https://raw.githubusercontent.com/tangjzh/EBike/master/swagger.yaml](https://raw.githubusercontent.com/tangjzh/EBike/master/swagger.yaml)
{% endswagger %}

{% swagger src="https://raw.githubusercontent.com/tangjzh/EBike/master/swagger.yaml" path="/users/profile/{id}/" method="delete" %}
[https://raw.githubusercontent.com/tangjzh/EBike/master/swagger.yaml](https://raw.githubusercontent.com/tangjzh/EBike/master/swagger.yaml)
{% endswagger %}

{% swagger src="https://raw.githubusercontent.com/tangjzh/EBike/master/swagger.yaml" path="/users/profile/{id}/" method="patch" %}
[https://raw.githubusercontent.com/tangjzh/EBike/master/swagger.yaml](https://raw.githubusercontent.com/tangjzh/EBike/master/swagger.yaml)
{% endswagger %}

### 2.3 绑定电动车通行证

{% swagger src="https://raw.githubusercontent.com/tangjzh/EBike/master/swagger.yaml" path="/users/bind-permit/" method="post" %}
[https://raw.githubusercontent.com/tangjzh/EBike/master/swagger.yaml](https://raw.githubusercontent.com/tangjzh/EBike/master/swagger.yaml)
{% endswagger %}

{% swagger src="https://raw.githubusercontent.com/tangjzh/EBike/master/swagger.yaml" path="/users/unbind-permit/" method="delete" %}
[https://raw.githubusercontent.com/tangjzh/EBike/master/swagger.yaml](https://raw.githubusercontent.com/tangjzh/EBike/master/swagger.yaml)
{% endswagger %}

### 2.4 删除用户（需要管理员权限）

{% swagger src="https://raw.githubusercontent.com/tangjzh/EBike/master/swagger.yaml" path="/users/delete/{id}/" method="delete" %}
[https://raw.githubusercontent.com/tangjzh/EBike/master/swagger.yaml](https://raw.githubusercontent.com/tangjzh/EBike/master/swagger.yaml)
{% endswagger %}

## 3 电动车信息模块

### 3.1 电动车基本信息

{% swagger src="https://raw.githubusercontent.com/tangjzh/EBike/master/swagger.yaml" path="/bikes/" method="get" %}
[https://raw.githubusercontent.com/tangjzh/EBike/master/swagger.yaml](https://raw.githubusercontent.com/tangjzh/EBike/master/swagger.yaml)
{% endswagger %}

{% swagger src="https://raw.githubusercontent.com/tangjzh/EBike/master/swagger.yaml" path="/bikes/" method="post" %}
[https://raw.githubusercontent.com/tangjzh/EBike/master/swagger.yaml](https://raw.githubusercontent.com/tangjzh/EBike/master/swagger.yaml)
{% endswagger %}

{% swagger src="https://raw.githubusercontent.com/tangjzh/EBike/master/swagger.yaml" path="/bikes/id/" method="get" %}
[https://raw.githubusercontent.com/tangjzh/EBike/master/swagger.yaml](https://raw.githubusercontent.com/tangjzh/EBike/master/swagger.yaml)
{% endswagger %}

{% swagger src="https://raw.githubusercontent.com/tangjzh/EBike/master/swagger.yaml" path="/bikes/{id}/" method="get" %}
[https://raw.githubusercontent.com/tangjzh/EBike/master/swagger.yaml](https://raw.githubusercontent.com/tangjzh/EBike/master/swagger.yaml)
{% endswagger %}

{% swagger src="https://raw.githubusercontent.com/tangjzh/EBike/master/swagger.yaml" path="/bikes/{id}/" method="put" %}
[https://raw.githubusercontent.com/tangjzh/EBike/master/swagger.yaml](https://raw.githubusercontent.com/tangjzh/EBike/master/swagger.yaml)
{% endswagger %}

{% swagger src="https://raw.githubusercontent.com/tangjzh/EBike/master/swagger.yaml" path="/bikes/{id}/" method="delete" %}
[https://raw.githubusercontent.com/tangjzh/EBike/master/swagger.yaml](https://raw.githubusercontent.com/tangjzh/EBike/master/swagger.yaml)
{% endswagger %}

{% swagger src="https://raw.githubusercontent.com/tangjzh/EBike/master/swagger.yaml" path="/bikes/{id}/" method="patch" %}
[https://raw.githubusercontent.com/tangjzh/EBike/master/swagger.yaml](https://raw.githubusercontent.com/tangjzh/EBike/master/swagger.yaml)
{% endswagger %}

### 3.2 电动车图片

{% swagger src="https://raw.githubusercontent.com/tangjzh/EBike/master/swagger.yaml" path="/bikes/images/" method="post" %}
[https://raw.githubusercontent.com/tangjzh/EBike/master/swagger.yaml](https://raw.githubusercontent.com/tangjzh/EBike/master/swagger.yaml)
{% endswagger %}

{% swagger src="https://raw.githubusercontent.com/tangjzh/EBike/master/swagger.yaml" path="/bikes/images/{id}/" method="delete" %}
[https://raw.githubusercontent.com/tangjzh/EBike/master/swagger.yaml](https://raw.githubusercontent.com/tangjzh/EBike/master/swagger.yaml)
{% endswagger %}

### 3.3 电动车商家渠道

{% swagger src="https://raw.githubusercontent.com/tangjzh/EBike/master/swagger.yaml" path="/bikes/channel/" method="get" %}
[https://raw.githubusercontent.com/tangjzh/EBike/master/swagger.yaml](https://raw.githubusercontent.com/tangjzh/EBike/master/swagger.yaml)
{% endswagger %}

{% swagger src="https://raw.githubusercontent.com/tangjzh/EBike/master/swagger.yaml" path="/bikes/channel/" method="post" %}
[https://raw.githubusercontent.com/tangjzh/EBike/master/swagger.yaml](https://raw.githubusercontent.com/tangjzh/EBike/master/swagger.yaml)
{% endswagger %}

{% swagger src="https://raw.githubusercontent.com/tangjzh/EBike/master/swagger.yaml" path="/bikes/channel/id/" method="get" %}
[https://raw.githubusercontent.com/tangjzh/EBike/master/swagger.yaml](https://raw.githubusercontent.com/tangjzh/EBike/master/swagger.yaml)
{% endswagger %}

{% swagger src="https://raw.githubusercontent.com/tangjzh/EBike/master/swagger.yaml" path="/bikes/channel/{id}/" method="get" %}
[https://raw.githubusercontent.com/tangjzh/EBike/master/swagger.yaml](https://raw.githubusercontent.com/tangjzh/EBike/master/swagger.yaml)
{% endswagger %}

{% swagger src="https://raw.githubusercontent.com/tangjzh/EBike/master/swagger.yaml" path="/bikes/channel/{id}/" method="put" %}
[https://raw.githubusercontent.com/tangjzh/EBike/master/swagger.yaml](https://raw.githubusercontent.com/tangjzh/EBike/master/swagger.yaml)
{% endswagger %}

{% swagger src="https://raw.githubusercontent.com/tangjzh/EBike/master/swagger.yaml" path="/bikes/channel/{id}/" method="delete" %}
[https://raw.githubusercontent.com/tangjzh/EBike/master/swagger.yaml](https://raw.githubusercontent.com/tangjzh/EBike/master/swagger.yaml)
{% endswagger %}

{% swagger src="https://raw.githubusercontent.com/tangjzh/EBike/master/swagger.yaml" path="/bikes/channel/{id}/" method="patch" %}
[https://raw.githubusercontent.com/tangjzh/EBike/master/swagger.yaml](https://raw.githubusercontent.com/tangjzh/EBike/master/swagger.yaml)
{% endswagger %}

## 4 社交模块

### 4.1 车小圈帖子

{% swagger src="https://raw.githubusercontent.com/tangjzh/EBike/master/swagger.yaml" path="/social/post/" method="get" %}
[https://raw.githubusercontent.com/tangjzh/EBike/master/swagger.yaml](https://raw.githubusercontent.com/tangjzh/EBike/master/swagger.yaml)
{% endswagger %}

{% swagger src="https://raw.githubusercontent.com/tangjzh/EBike/master/swagger.yaml" path="/social/post/" method="post" %}
[https://raw.githubusercontent.com/tangjzh/EBike/master/swagger.yaml](https://raw.githubusercontent.com/tangjzh/EBike/master/swagger.yaml)
{% endswagger %}

{% swagger src="https://raw.githubusercontent.com/tangjzh/EBike/master/swagger.yaml" path="/social/post/mine/" method="get" %}
[https://raw.githubusercontent.com/tangjzh/EBike/master/swagger.yaml](https://raw.githubusercontent.com/tangjzh/EBike/master/swagger.yaml)
{% endswagger %}

{% swagger src="https://raw.githubusercontent.com/tangjzh/EBike/master/swagger.yaml" path="/social/post/{id}/" method="get" %}
[https://raw.githubusercontent.com/tangjzh/EBike/master/swagger.yaml](https://raw.githubusercontent.com/tangjzh/EBike/master/swagger.yaml)
{% endswagger %}

{% swagger src="https://raw.githubusercontent.com/tangjzh/EBike/master/swagger.yaml" path="/social/post/{id}/" method="put" %}
[https://raw.githubusercontent.com/tangjzh/EBike/master/swagger.yaml](https://raw.githubusercontent.com/tangjzh/EBike/master/swagger.yaml)
{% endswagger %}

{% swagger src="https://raw.githubusercontent.com/tangjzh/EBike/master/swagger.yaml" path="/social/post/{id}/" method="delete" %}
[https://raw.githubusercontent.com/tangjzh/EBike/master/swagger.yaml](https://raw.githubusercontent.com/tangjzh/EBike/master/swagger.yaml)
{% endswagger %}

{% swagger src="https://raw.githubusercontent.com/tangjzh/EBike/master/swagger.yaml" path="/social/post/{id}/" method="patch" %}
[https://raw.githubusercontent.com/tangjzh/EBike/master/swagger.yaml](https://raw.githubusercontent.com/tangjzh/EBike/master/swagger.yaml)
{% endswagger %}

### 4.2 车小圈帖子评论

{% swagger src="https://raw.githubusercontent.com/tangjzh/EBike/master/swagger.yaml" path="/social/comment/" method="get" %}
[https://raw.githubusercontent.com/tangjzh/EBike/master/swagger.yaml](https://raw.githubusercontent.com/tangjzh/EBike/master/swagger.yaml)
{% endswagger %}

{% swagger src="https://raw.githubusercontent.com/tangjzh/EBike/master/swagger.yaml" path="/social/comment/" method="post" %}
[https://raw.githubusercontent.com/tangjzh/EBike/master/swagger.yaml](https://raw.githubusercontent.com/tangjzh/EBike/master/swagger.yaml)
{% endswagger %}

{% swagger src="https://raw.githubusercontent.com/tangjzh/EBike/master/swagger.yaml" path="/social/comment/{id}/" method="get" %}
[https://raw.githubusercontent.com/tangjzh/EBike/master/swagger.yaml](https://raw.githubusercontent.com/tangjzh/EBike/master/swagger.yaml)
{% endswagger %}

{% swagger src="https://raw.githubusercontent.com/tangjzh/EBike/master/swagger.yaml" path="/social/comment/{id}/" method="put" %}
[https://raw.githubusercontent.com/tangjzh/EBike/master/swagger.yaml](https://raw.githubusercontent.com/tangjzh/EBike/master/swagger.yaml)
{% endswagger %}

{% swagger src="https://raw.githubusercontent.com/tangjzh/EBike/master/swagger.yaml" path="/social/comment/{id}/" method="delete" %}
[https://raw.githubusercontent.com/tangjzh/EBike/master/swagger.yaml](https://raw.githubusercontent.com/tangjzh/EBike/master/swagger.yaml)
{% endswagger %}

{% swagger src="https://raw.githubusercontent.com/tangjzh/EBike/master/swagger.yaml" path="/social/comment/{id}/" method="patch" %}
[https://raw.githubusercontent.com/tangjzh/EBike/master/swagger.yaml](https://raw.githubusercontent.com/tangjzh/EBike/master/swagger.yaml)
{% endswagger %}

### 4.3 车小圈用户互动

{% swagger src="https://raw.githubusercontent.com/tangjzh/EBike/master/swagger.yaml" path="/social/post/likes/" method="get" %}
[https://raw.githubusercontent.com/tangjzh/EBike/master/swagger.yaml](https://raw.githubusercontent.com/tangjzh/EBike/master/swagger.yaml)
{% endswagger %}

{% swagger src="https://raw.githubusercontent.com/tangjzh/EBike/master/swagger.yaml" path="/social/post/favorites/" method="get" %}
[https://raw.githubusercontent.com/tangjzh/EBike/master/swagger.yaml](https://raw.githubusercontent.com/tangjzh/EBike/master/swagger.yaml)
{% endswagger %}

{% swagger src="https://raw.githubusercontent.com/tangjzh/EBike/master/swagger.yaml" path="/social/post/interaction/toggle/" method="post" %}
[https://raw.githubusercontent.com/tangjzh/EBike/master/swagger.yaml](https://raw.githubusercontent.com/tangjzh/EBike/master/swagger.yaml)
{% endswagger %}

{% swagger src="https://raw.githubusercontent.com/tangjzh/EBike/master/swagger.yaml" path="/social/post/interaction/count/" method="post" %}
[https://raw.githubusercontent.com/tangjzh/EBike/master/swagger.yaml](https://raw.githubusercontent.com/tangjzh/EBike/master/swagger.yaml)
{% endswagger %}

{% swagger src="https://raw.githubusercontent.com/tangjzh/EBike/master/swagger.yaml" path="/social/follow/toggle/" method="post" %}
[https://raw.githubusercontent.com/tangjzh/EBike/master/swagger.yaml](https://raw.githubusercontent.com/tangjzh/EBike/master/swagger.yaml)
{% endswagger %}

### 4.4 车小圈首页

{% swagger src="https://raw.githubusercontent.com/tangjzh/EBike/master/swagger.yaml" path="/social/homepage/" method="get" %}
[https://raw.githubusercontent.com/tangjzh/EBike/master/swagger.yaml](https://raw.githubusercontent.com/tangjzh/EBike/master/swagger.yaml)
{% endswagger %}

## 5 二手交易模块

{% swagger src="https://raw.githubusercontent.com/tangjzh/EBike/master/swagger.yaml" path="/exchange/goods/" method="post" %}
[https://raw.githubusercontent.com/tangjzh/EBike/master/swagger.yaml](https://raw.githubusercontent.com/tangjzh/EBike/master/swagger.yaml)
{% endswagger %}

{% swagger src="https://raw.githubusercontent.com/tangjzh/EBike/master/swagger.yaml" path="/exchange/goods/mine/" method="get" %}
[https://raw.githubusercontent.com/tangjzh/EBike/master/swagger.yaml](https://raw.githubusercontent.com/tangjzh/EBike/master/swagger.yaml)
{% endswagger %}

{% swagger src="https://raw.githubusercontent.com/tangjzh/EBike/master/swagger.yaml" path="/exchange/goods/{hash}/" method="get" %}
[https://raw.githubusercontent.com/tangjzh/EBike/master/swagger.yaml](https://raw.githubusercontent.com/tangjzh/EBike/master/swagger.yaml)
{% endswagger %}

{% swagger src="https://raw.githubusercontent.com/tangjzh/EBike/master/swagger.yaml" path="/exchange/goods/{hash}/" method="put" %}
[https://raw.githubusercontent.com/tangjzh/EBike/master/swagger.yaml](https://raw.githubusercontent.com/tangjzh/EBike/master/swagger.yaml)
{% endswagger %}

{% swagger src="https://raw.githubusercontent.com/tangjzh/EBike/master/swagger.yaml" path="/exchange/goods/{hash}/" method="delete" %}
[https://raw.githubusercontent.com/tangjzh/EBike/master/swagger.yaml](https://raw.githubusercontent.com/tangjzh/EBike/master/swagger.yaml)
{% endswagger %}

{% swagger src="https://raw.githubusercontent.com/tangjzh/EBike/master/swagger.yaml" path="/exchange/goods/{hash}/" method="patch" %}
[https://raw.githubusercontent.com/tangjzh/EBike/master/swagger.yaml](https://raw.githubusercontent.com/tangjzh/EBike/master/swagger.yaml)
{% endswagger %}

## 6 维修模块

### 6.1 维修预约

{% swagger src="https://raw.githubusercontent.com/tangjzh/EBike/master/swagger.yaml" path="/maintenance/appointments/" method="get" %}
[https://raw.githubusercontent.com/tangjzh/EBike/master/swagger.yaml](https://raw.githubusercontent.com/tangjzh/EBike/master/swagger.yaml)
{% endswagger %}

{% swagger src="https://raw.githubusercontent.com/tangjzh/EBike/master/swagger.yaml" path="/maintenance/appointments/" method="post" %}
[https://raw.githubusercontent.com/tangjzh/EBike/master/swagger.yaml](https://raw.githubusercontent.com/tangjzh/EBike/master/swagger.yaml)
{% endswagger %}

{% swagger src="https://raw.githubusercontent.com/tangjzh/EBike/master/swagger.yaml" path="/maintenance/appointments/{id}/" method="get" %}
[https://raw.githubusercontent.com/tangjzh/EBike/master/swagger.yaml](https://raw.githubusercontent.com/tangjzh/EBike/master/swagger.yaml)
{% endswagger %}

{% swagger src="https://raw.githubusercontent.com/tangjzh/EBike/master/swagger.yaml" path="/maintenance/appointments/{id}/" method="put" %}
[https://raw.githubusercontent.com/tangjzh/EBike/master/swagger.yaml](https://raw.githubusercontent.com/tangjzh/EBike/master/swagger.yaml)
{% endswagger %}

{% swagger src="https://raw.githubusercontent.com/tangjzh/EBike/master/swagger.yaml" path="/maintenance/appointments/{id}/" method="delete" %}
[https://raw.githubusercontent.com/tangjzh/EBike/master/swagger.yaml](https://raw.githubusercontent.com/tangjzh/EBike/master/swagger.yaml)
{% endswagger %}

{% swagger src="https://raw.githubusercontent.com/tangjzh/EBike/master/swagger.yaml" path="/maintenance/appointments/{id}/" method="patch" %}
[https://raw.githubusercontent.com/tangjzh/EBike/master/swagger.yaml](https://raw.githubusercontent.com/tangjzh/EBike/master/swagger.yaml)
{% endswagger %}

### 6.2 维修商家

{% swagger src="https://raw.githubusercontent.com/tangjzh/EBike/master/swagger.yaml" path="/maintenance/shops/" method="get" %}
[https://raw.githubusercontent.com/tangjzh/EBike/master/swagger.yaml](https://raw.githubusercontent.com/tangjzh/EBike/master/swagger.yaml)
{% endswagger %}

{% swagger src="https://raw.githubusercontent.com/tangjzh/EBike/master/swagger.yaml" path="/maintenance/shops/" method="post" %}
[https://raw.githubusercontent.com/tangjzh/EBike/master/swagger.yaml](https://raw.githubusercontent.com/tangjzh/EBike/master/swagger.yaml)
{% endswagger %}

{% swagger src="https://raw.githubusercontent.com/tangjzh/EBike/master/swagger.yaml" path="/maintenance/shops/{id}/" method="get" %}
[https://raw.githubusercontent.com/tangjzh/EBike/master/swagger.yaml](https://raw.githubusercontent.com/tangjzh/EBike/master/swagger.yaml)
{% endswagger %}

{% swagger src="https://raw.githubusercontent.com/tangjzh/EBike/master/swagger.yaml" path="/maintenance/shops/{id}/" method="put" %}
[https://raw.githubusercontent.com/tangjzh/EBike/master/swagger.yaml](https://raw.githubusercontent.com/tangjzh/EBike/master/swagger.yaml)
{% endswagger %}

{% swagger src="https://raw.githubusercontent.com/tangjzh/EBike/master/swagger.yaml" path="/maintenance/shops/{id}/" method="delete" %}
[https://raw.githubusercontent.com/tangjzh/EBike/master/swagger.yaml](https://raw.githubusercontent.com/tangjzh/EBike/master/swagger.yaml)
{% endswagger %}

{% swagger src="https://raw.githubusercontent.com/tangjzh/EBike/master/swagger.yaml" path="/maintenance/shops/{id}/" method="patch" %}
[https://raw.githubusercontent.com/tangjzh/EBike/master/swagger.yaml](https://raw.githubusercontent.com/tangjzh/EBike/master/swagger.yaml)
{% endswagger %}

### 6.3 维修贴士

{% swagger src="https://raw.githubusercontent.com/tangjzh/EBike/master/swagger.yaml" path="/maintenance/tips/" method="get" %}
[https://raw.githubusercontent.com/tangjzh/EBike/master/swagger.yaml](https://raw.githubusercontent.com/tangjzh/EBike/master/swagger.yaml)
{% endswagger %}

{% swagger src="https://raw.githubusercontent.com/tangjzh/EBike/master/swagger.yaml" path="/maintenance/tips/" method="post" %}
[https://raw.githubusercontent.com/tangjzh/EBike/master/swagger.yaml](https://raw.githubusercontent.com/tangjzh/EBike/master/swagger.yaml)
{% endswagger %}

{% swagger src="https://raw.githubusercontent.com/tangjzh/EBike/master/swagger.yaml" path="/maintenance/tips/{id}/" method="get" %}
[https://raw.githubusercontent.com/tangjzh/EBike/master/swagger.yaml](https://raw.githubusercontent.com/tangjzh/EBike/master/swagger.yaml)
{% endswagger %}

{% swagger src="https://raw.githubusercontent.com/tangjzh/EBike/master/swagger.yaml" path="/maintenance/tips/{id}/" method="put" %}
[https://raw.githubusercontent.com/tangjzh/EBike/master/swagger.yaml](https://raw.githubusercontent.com/tangjzh/EBike/master/swagger.yaml)
{% endswagger %}

{% swagger src="https://raw.githubusercontent.com/tangjzh/EBike/master/swagger.yaml" path="/maintenance/tips/{id}/" method="delete" %}
[https://raw.githubusercontent.com/tangjzh/EBike/master/swagger.yaml](https://raw.githubusercontent.com/tangjzh/EBike/master/swagger.yaml)
{% endswagger %}

{% swagger src="https://raw.githubusercontent.com/tangjzh/EBike/master/swagger.yaml" path="/maintenance/tips/{id}/" method="patch" %}
[https://raw.githubusercontent.com/tangjzh/EBike/master/swagger.yaml](https://raw.githubusercontent.com/tangjzh/EBike/master/swagger.yaml)
{% endswagger %}

## 7 安全和举报模块

{% swagger src="https://raw.githubusercontent.com/tangjzh/EBike/master/swagger.yaml" path="/safety/reports/" method="get" %}
[https://raw.githubusercontent.com/tangjzh/EBike/master/swagger.yaml](https://raw.githubusercontent.com/tangjzh/EBike/master/swagger.yaml)
{% endswagger %}

{% swagger src="https://raw.githubusercontent.com/tangjzh/EBike/master/swagger.yaml" path="/safety/reports/" method="post" %}
[https://raw.githubusercontent.com/tangjzh/EBike/master/swagger.yaml](https://raw.githubusercontent.com/tangjzh/EBike/master/swagger.yaml)
{% endswagger %}

{% swagger src="https://raw.githubusercontent.com/tangjzh/EBike/master/swagger.yaml" path="/safety/reports/{id}/" method="get" %}
[https://raw.githubusercontent.com/tangjzh/EBike/master/swagger.yaml](https://raw.githubusercontent.com/tangjzh/EBike/master/swagger.yaml)
{% endswagger %}

{% swagger src="https://raw.githubusercontent.com/tangjzh/EBike/master/swagger.yaml" path="/safety/reports/{id}/" method="put" %}
[https://raw.githubusercontent.com/tangjzh/EBike/master/swagger.yaml](https://raw.githubusercontent.com/tangjzh/EBike/master/swagger.yaml)
{% endswagger %}

{% swagger src="https://raw.githubusercontent.com/tangjzh/EBike/master/swagger.yaml" path="/safety/reports/{id}/" method="patch" %}
[https://raw.githubusercontent.com/tangjzh/EBike/master/swagger.yaml](https://raw.githubusercontent.com/tangjzh/EBike/master/swagger.yaml)
{% endswagger %}

