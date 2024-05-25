# 🎯 项目开发计划

## 1 项目概述

### 1.1 基本信息

该项目由 [唐锦洲](https://app.gitbook.com/u/eDuOQyxxq5RjDyaODgK5zwjGuh33 "mention")、[liuzh297](https://app.gitbook.com/u/bw4Ev4MapOPvz8RNNkgkZ1rgLHh1 "mention")、[刘畅](https://app.gitbook.com/u/YRJxqSSYRWVX7Q0psj7XxEMwVbL2 "mention")、[shenpf3](https://app.gitbook.com/u/WDLjcnYaJZOnTaxPipybuPYEI153 "mention")、[刘书睿](https://app.gitbook.com/u/PcGO1DW7MZVbMxHRPMyWROKZzwn1 "mention")、[吴恺云](https://app.gitbook.com/u/AQ6nuwfgkYc0IYRPpl20FomZGiU2 "mention")、[黄楚丹](https://app.gitbook.com/u/38TEZLZFTeapfDVwbsEy94kt0rq2 "mention") 开发维护。

基于业务进行充分沟通后，该项目命名为"易拜 E-bike"。

### 1.2 项目主要联系人

### 1.3 对用户作出的承诺

1. **功能完整性**：我们将确保软件包含所有在项目需求文档中定义的功能。
2. **交付时间**：我们承诺在2024年5月22日前完成软件的开发和测试，并准备交付。
3. **用户支持**：我们将提供全面的用户支持，包括培文档和客服服务。
4. **数据安全**：我们保证软件将遵守所有相关的数据保护法规，并采取适当的安全措施来保护用户数据。
5. **持续改进**：我们将根据用户反馈不断改进软件，确保满足用户不断变化的需求。
6. **功能完整性**：我们将确保软件包含所有在项目需求文档中定义的功能。
7. **性能标准**：软件将满足或超过在性能标准文档中定义的性能指标。
8. **交付时间**：我们承诺在2024年5月25日前完成软件的开发和测试，并准备交付。
9. **用户支持**：我们将提供全面的用户支持，包括文档支持和客服服务。
10. **数据安全**：我们保证软件将遵守所有相关的数据保护法规，并采取适当的安全措施来保护用户数据。
11. **持续改进**：我们将根据用户反馈不断改进软件，确保满足用户不断变化的需求。

### 1.4 项目范围以及完成标志

项目范围包含以下几个方面

1.  **项目目标**

    为校园用户提供一站式电动车服务的Online to offline平台，包括销售信息、点评、交易、社交和充电服务。
2. **功能需求**
   * 电动车销售信息展示：提供电动车品牌、型号、价格、促销活动等信息。
   * 第三方电动车消费点评：允许用户对电动车产品进行评价和评论。
   * 二手电动车交易：创建一个平台，让用户可以发布和浏览二手电动车交易信息。
   * 车友社交：提供一个社区，供电动车爱好者交流心得、分享经验。
   * 电动车充电服务：集成充电站地图和预约服务，方便用户查找和使用充电设施。
3. **项目边界**
   * 本项目不包含电动车的实体销售和物流配送。
   * 本项目不包含真实的电动车维修服务。
4.  **项目范围变更声明**

    任何范围变更必须经过项目管理团队的审查和批准。
5. **功能需求：**
   * 电动自行车信息展示
   * 充电桩监控
   * 电动车维修保养预约
   * 电动自行车消防安全监测与排查
   * 车小圈
   * 二手转让
6. **非功能需求**
   * 系统支持至少1000个并发用户。
   * 数据传输加密。
   * 系统应在所有主流浏览器上运行。

### 1.5 假设与约束

在项目规划阶段，团队对这些假设和依赖关系进行详细的分析和评估，以确保项目的成功。如果这些假设中的任何一个不成立，或者依赖关系中的任何一个出现问题，都可能对项目的成功造成影响。因此，项目管理团队也制定了相应的风险管理计划，以应对可能出现的问题。

1. 假设
   * **用户基础**：假设校园内已经有足够数量的电动车用户和潜在用户，他们对使用该平台感兴趣。
   * **政策支持**：假设校园管理层长期稳定支持电动车使用，并可能提供必要的政策和场地支持。
   * **市场调研**：假设市场调研结果准确，反映了用户的真实需求和偏好。
   * **第三方服务**：假设第三方服务提供商（如地图服务等）将提供稳定可靠的服务。
   * **法律法规**：假设项目符合所有相关的法律法规，包括数据保护和电子商务法规。
   * **资金和资源**：假设项目团队能够获得足够的资金和资源来完成项目。
   * **用户接受度**：假设用户愿意接受并适应新平台的使用。
2. 约束
   * **第三方服务**：项目依赖于第三方服务的正常运作，如地图服务、云服务等。
   * **校园合作**：项目可能依赖于与校园管理部门的合作，以获得必要的支持和资源。
   * **政策变化**：依赖于对政府和校园管理层政策变化的敏感性，以便及时调整项目策略。
   *   **用户教育**：依赖于有效的用户教育和培训，以确保用户能够充分利用平台。



## 2 项目组织结构、职责

### 2.1 项目组织结构图

本项目开发在tier0分设项目总工程师和项目总经理，项目总工程师负责整体推进项目，项目总经理负责确保各部门按照计划如期完成任务。

<figure><img src=".gitbook/assets/安全组织架构图.bmp" alt="" width="375"><figcaption><p>项目组织架构图</p></figcaption></figure>

### 2.2 岗位与职责

<table><thead><tr><th width="125" align="center">Group</th><th width="128" align="center">Position</th><th align="center">Duty</th></tr></thead><tbody><tr><td align="center">设计部门</td><td align="center">UX</td><td align="center">交互设计/原型设计</td></tr><tr><td align="center">设计部门</td><td align="center">UI</td><td align="center">视觉设计/原型设计</td></tr><tr><td align="center">开发部门</td><td align="center">前端</td><td align="center">用户界面实现</td></tr><tr><td align="center">开发部门</td><td align="center">后端</td><td align="center">API开发</td></tr><tr><td align="center">测试部门</td><td align="center">前端测试</td><td align="center">界面验证</td></tr><tr><td align="center">测试部门</td><td align="center">后端测试</td><td align="center">逻辑验证</td></tr></tbody></table>

## 3 项目计划

### 3.1 选择生命周期模型

本项目选用RUP的迭代式模型。在确定初始计划后，不断通过以下路径进行迭代。

1. 计划
2. 业务工程
3. 需求调研
4. 分析设计
5. 实施部署
6. 测试评估

### 3.2 开发标准、平台及工具

#### 3.2.1 开发标准

#### 3.2.2 **开发平台**

* Github 代码托管平台
  * 地址：[https://github.com/tangjzh/EBike](https://github.com/tangjzh/EBike)

{% @github-files/github-code-block url="https://github.com/tangjzh/EBike" %}

* Gitbook 项目文档管理平台
  * 地址：[https://liu-shu-ruisorganization.gitbook.io/ebike](https://liu-shu-ruisorganization.gitbook.io/ebike)

{% embed url="https://liu-shu-ruisorganization.gitbook.io/ebike" %}
Ebike文档
{% endembed %}

* Notion 团队协作平台
  * 地址：[https://www.notion.so/](https://www.notion.so/)

{% embed url="https://www.notion.so/" %}

#### 3.2.2 **开发语言和**工具

后端采用 Python 作为首选开发语言，基于 Django 框架开发算法和业务逻辑。整个后端系统遵循 RESTful API 标准和 OpenAPI 协议，并在设计哲学上遵循微软的 [API 设计理念](https://learn.microsoft.com/zh-cn/azure/architecture/best-practices/api-design)。

前端采用 JavaScript 作为首选开发语言，基于  Vue3 框架开发前端界面。整个前端系统遵循 [Vue 设计哲学](https://cn.vuejs.org/guide/introduction.html)，继承响应式布局和渐进式开发特性。

软件开发环境如下：

* 硬件环境
  * CPU:  AMD Ryzen 9 5900HX 16核32线程
  * RAM: 40G DDR4
* 软件环境
  * Python: 3.10
  * Django: 4.10
  * PyTorch: 1.6.0
  * Node.js/JavaScript
  * Vue3
* 开发工具
  * VSCode
  * Postman

后端生产环境如下：

* 硬件环境
  * CPU: Intel Xeon Platinum 8280 28核56线程（虚拟化4核8线程）
  * RAM: 8G
* 软件环境：与开发环境一致

#### 3.2.2 前端开发

### 3.3 项目估算

本项目估算主要对软件规模进行估算，从而预估开发工期。在规模上主要基于功能点对功能规模进行估算。

本估算采用ISO14143 IFPUG标准进行估算，得到经过调整后的功能点数。

{% embed url="https://ifpug.org/ifpug-standards/sfp" %}
ISO14143 IFPUG.
{% endembed %}

#### 3.3.1 ILF功能点数

<table data-full-width="false"><thead><tr><th>ILF</th><th>RET</th><th>DET</th><th>复杂度</th><th>未调整FP个数</th></tr></thead><tbody><tr><td>电动车信息</td><td>品牌、类型、价钱、评分、商品介绍、发布日期，共6个</td><td>12</td><td>平均</td><td>10</td></tr><tr><td>社交帖子评论信息</td><td>文本、点赞量，共2个</td><td>4</td><td>简单</td><td>6</td></tr><tr><td>社交帖子信息</td><td>标题、文本、创建时间、提交时间、浏览量、点赞量，共6个</td><td>8</td><td>平均</td><td>7</td></tr><tr><td>用户信息</td><td>密码、最近登录时间、昵称、实名姓名、加入日期、性别、生日、邮箱、电话，共9个</td><td>20</td><td>复杂</td><td>12</td></tr></tbody></table>

合计 = 7+10+10+15 = 42。

#### 3.3.2 ELF功能点数

<table data-full-width="false"><thead><tr><th>EIF</th><th>RET</th><th>DET</th><th>复杂度</th><th>未调整的FP个数</th></tr></thead><tbody><tr><td>Follower表</td><td>用户信息、用户<br>信息，共2个</td><td>8</td><td>简单</td><td>7</td></tr><tr><td>Following表</td><td>用户信息、用户信息，共2个</td><td>10</td><td>简单</td><td>9</td></tr><tr><td>Comment表</td><td>社交帖子信息、<br>社交帖子评论信息，共2个</td><td>12</td><td>简单</td><td>7</td></tr><tr><td>exchange表</td><td>电动车信息、<br>用户信息，共2个</td><td>8</td><td>简单</td><td>5</td></tr><tr><td>post_user表</td><td>用户信息、社交帖子信息，共2个</td><td>10</td><td>简单</td><td>7</td></tr><tr><td>bike_user表</td><td>用户信息、电动车信息，共2个</td><td>10</td><td>简单</td><td>5</td></tr></tbody></table>

合计 = 5+5+5+5+5+5 = 30。

#### 3.3.3 EI功能点数

<table data-full-width="false"><thead><tr><th>EI</th><th>FTR</th><th>DET</th><th>复杂度</th><th>未调整FP个数</th></tr></thead><tbody><tr><td>添加用户信息</td><td>用户信息、following表/follower表</td><td>24</td><td>复杂</td><td>6</td></tr><tr><td>修改用户信息</td><td>用户信息、following表/follower表</td><td>24</td><td>复杂</td><td>6</td></tr><tr><td>删除用户信息</td><td>用户信息、following表/follower表</td><td>24</td><td>复杂</td><td>4</td></tr><tr><td>添加社交帖子评论信息</td><td>用户信息、社交帖子评论信息、comment表</td><td>18</td><td>复杂</td><td>4</td></tr><tr><td>修改社交帖子评论信息</td><td>用户信息、社交帖子评论信息、comment表</td><td>18</td><td>复杂</td><td>3</td></tr><tr><td>删除社交帖子评论信息</td><td>用户信息、社交帖子评论信息、comment表</td><td>18</td><td>复杂</td><td>3</td></tr><tr><td>添加社交帖子信息</td><td>用户信息、社交帖子信息、post_user表</td><td>22</td><td>复杂</td><td>3</td></tr><tr><td>修改社交帖子信息</td><td>用户信息、社交帖子信息、post_user表</td><td>22</td><td>复杂</td><td>3</td></tr><tr><td>删除社交帖子<br>信息</td><td>用户信息、社交帖子信息、post_user表</td><td>22</td><td>复杂</td><td>4</td></tr><tr><td>添加电动车信息</td><td>电动车信息、用户信息、bike_user表</td><td>18</td><td>复杂</td><td>4</td></tr><tr><td>修改电动车信息</td><td>电动车信息、用户信息、bike_user表</td><td>18</td><td>复杂</td><td>6</td></tr><tr><td>删除电动车信息</td><td>电动车信息、用户信息、bike_user表</td><td>18</td><td>复杂</td><td>3</td></tr></tbody></table>

合计 = 6+6+6+6+6+6+6+6+6+6+6+6 = 72。

#### 3.3.4 EQ功能点数

<table data-full-width="false"><thead><tr><th>EQ</th><th>FTR</th><th>DET</th><th>复杂度</th><th>未调整FP个数</th></tr></thead><tbody><tr><td>查询用户信息</td><td>用户信息</td><td>2</td><td>简单</td><td>3</td></tr><tr><td>查询follower信息</td><td>用户信息、following表</td><td>20</td><td>复杂</td><td>4</td></tr><tr><td>查询follower信息</td><td>用户信息、follower表</td><td>20</td><td>复杂</td><td>4</td></tr><tr><td>查询帖子信息</td><td>社交帖子信息</td><td>2</td><td>简单</td><td>3</td></tr><tr><td>查询电动车信息</td><td>电动车信息、bike_user表</td><td>18</td><td>复杂</td><td>3</td></tr></tbody></table>

合计 = 3+3+6+6+6 = 24。

#### 3.3.5 EO功能点数

<table data-full-width="false"><thead><tr><th>EO</th><th>FTR</th><th>DET</th><th>复杂度</th><th>未调整FP个数</th></tr></thead><tbody><tr><td>统计商家入驻情况</td><td>用户信息</td><td>2个</td><td>简单</td><td>4</td></tr></tbody></table>

合计 = 4。

#### 3.3.6 计算调整因子

合集19，调整因子=19\*0.01+0.65 = 0.84

最终调整后的功能点数 = 0.84\*(4+24+72+30+42) = 144.48。

#### 3.3.7 评估

最终调整后的功能点数为144.18，在业务逻辑上属于中小型软件，应提前预留充足工期，约1个月的开发时间。

### 3.4 里程碑计划

[唐锦洲](https://app.gitbook.com/u/eDuOQyxxq5RjDyaODgK5zwjGuh33 "mention")

在本项目中，我们将整个项目流程分为几个里程碑，并设定完成时间，作为整体进度计划，以控制整个项目流程。

<table><thead><tr><th width="117">里程碑</th><th width="381">完成标准</th><th>完成时间</th></tr></thead><tbody><tr><td>需求分析</td><td>撰写<a href="ruan-jian-xu-qiu-shuo-ming-shu.md">需求分析</a>文档，构思完成产品所需功能</td><td>2024/04/10</td></tr><tr><td>技术验证</td><td>完成技术选型，提供可运行的技术原型</td><td>2024/04/21</td></tr><tr><td>产品开发</td><td>完成系统前后端基本功能</td><td>2024/05/15</td></tr><tr><td>内部测试</td><td>完成所有<a href="ruan-jian-ce-shi-ji-hua.md">测试计划</a>中的前后端测试目标</td><td>2024/05/20</td></tr><tr><td>用户测试</td><td>完成所有<a href="ruan-jian-ce-shi-ji-hua.md">测试计划</a>中的用户测试目标</td><td>2024/05/24</td></tr></tbody></table>

### 3.5 风险管理计划

[liuzh297](https://app.gitbook.com/u/bw4Ev4MapOPvz8RNNkgkZ1rgLHh1 "mention")

### 3.6 产品评审计划

#### 3.6.1 产品评审目标

产品评审计划的目的是确保“易拜”小程序项目在开发的各个阶段符合预定的要求和标准。通过定期评审，可以及时发现和解决潜在问题，提高产品的质量和用户满意度。

#### 3.6.2 评审阶段

产品评审将贯穿项目开发的整个生命周期，主要分为需求、设计、代码、功能、系统集成，以及验收等六个评审阶段。

**1) 需求评审**

* **时间节点：**项目启动后两周内
* **参与人员：**项目经理、开发团队、UX/UI设计师、测试团队
* **评审内容：**需求文档、功能规格说明书、用户实例
* **目标：**确保项目需求的完整性、可行性和明确性

<table><thead><tr><th width="180">需求评审会议议程</th><th>时间</th><th>参与人员</th><th>主要讨论内容</th></tr></thead><tbody><tr><td>需求概述</td><td>2024/04/19上午9:00-9:30</td><td>项目经理、开发团队</td><td>总体需求介绍，功能需求讨论</td></tr><tr><td>详细需求讨论</td><td>2024/04/19上午9:30-10:30</td><td>全体参与人员</td><td>详细功能需求、用户实例评审</td></tr><tr><td>需求确认与记录</td><td>2024/04/19上午10:30-11:00</td><td>项目经理、开发团队</td><td>需求确认，总结和记录评审意见</td></tr></tbody></table>

**2) 设计评审**

* **时间节点：**需求评审通过后一周内&#x20;
* **参与人员：**项目经理、开发团队、UX/UI设计师、测试团队
* **评审内容：**系统设计文档、数据库设计、界面设计原型
* **目标：**确保设计符合需求，界面友好，系统架构合理

<figure><img src=".gitbook/assets/设计评审 (1).png" alt="" width="563"><figcaption><p>设计评审流程图</p></figcaption></figure>

**3) 代码评审**

* **时间节点：**每个迭代开发完成后&#x20;
* **参与人员：**开发团队、代码审查员
* **评审内容：**源代码、单元测试结果
* **目标：**确保代码质量、可维护性和可扩展性

<table><thead><tr><th width="190">代码评审标准</th><th>评审内容</th></tr></thead><tbody><tr><td>代码规范</td><td>代码是否符合编码规范，命名是否合理</td></tr><tr><td>功能实现</td><td>代码是否实现预期功能，是否通过单元测试</td></tr><tr><td>可维护性</td><td>代码结构是否清晰，是否易于维护和扩展</td></tr></tbody></table>

**4) 功能评审**

* **时间节点：**每个功能模块开发完成后
* **参与人员：**项目经理、开发团队、UX/UI设计师、测试团队
* **评审内容：**功能实现情况、功能测试结果
* **目标：**确保功能实现符合需求，功能无重大缺陷

<table><thead><tr><th width="224">功能评审模块</th><th>描述</th></tr></thead><tbody><tr><td><strong>电动自行车喜爱度排行</strong></td><td>展示校园内最受欢迎的电动自行车排名，帮助用户了解热门车型。</td></tr><tr><td><strong>电动自行车评论动态贴</strong></td><td>用户可以对电动自行车发表评价和动态贴，分享使用心得和经验，增强社区氛围。</td></tr><tr><td><strong>车辆充电桩/柜信息展示</strong></td><td>实时展示校园内各充电桩和充电柜的位置信息及使用状态。用户可以通过小程序轻松查找和使用充电设施，减少等待时间和充电困难。</td></tr><tr><td><strong>车辆维修预约</strong></td><td>提供在线上门预约维修服务，用户可以方便地安排电动自行车的维修时间，查看维修进度，保障车辆的正常使用。</td></tr><tr><td><strong>车辆安全监控</strong></td><td>该功能主要针对校园内电动自行车的违停、违规拉线等行为进行监控，旨在减少消防隐患。平台设有小型电动车辆事故反馈系统，用户可以通过该系统报告事故和安全隐患，管理方会及时处理这些反馈，确保校园环境的安全和秩序。通过实时监控用户反馈，平台能够有效地预防和减少电动自行车使用中的安全问题，保障用户的安全。</td></tr><tr><td><strong>电动车辆二手转让</strong></td><td>为用户提供二手电动自行车的交易平台，促进资源循环利用。</td></tr></tbody></table>

**5) 系统集成评审**

* **时间节点：**系统集成完成后
* **参与人员：**项目经理、开发团队、UX/UI设计师、测试团队、运维团队
* **评审内容：**系统集成测试结果、性能测试结果、安全测试结果
* **目标：**确保系统集成顺利，性能和安全性符合要求

<figure><img src=".gitbook/assets/集成评审流程 (1).png" alt=""><figcaption><p>系统集成评审流程图</p></figcaption></figure>

**6) 验收评审**

* **时间节点：**系统开发完成后
* **参与人员：**项目经理、开发团队、UX/UI设计师、测试团队、用户代表
* **评审内容：**验收测试结果、用户反馈
* **目标：**确保系统满足最终用户需求，可以正式投入使用

<table><thead><tr><th width="190">验收评审会议议程</th><th width="182" align="center">时间</th><th width="134">参与人员</th><th>主要讨论内容</th></tr></thead><tbody><tr><td>验收测试报告</td><td align="center"><p>2024/05/19</p><p>上午9:00-9:30</p></td><td>项目经理、测试团队、用户代表</td><td>验收测试结果汇报</td></tr><tr><td>用户反馈讨论</td><td align="center"><p>2024/05/19</p><p>上午9:30-10:30</p></td><td>全体参与人员</td><td>用户反馈收集和讨论</td></tr><tr><td>最终确认与总结</td><td align="center"><p>2024/05/19</p><p>上午10:30-11:00</p></td><td>全体参与人员</td><td>最终验收确认，总结评审结果</td></tr></tbody></table>

#### 3.6.3 评审标准

评审标准根据不同阶段和内容制定，确保“易拜”小程序在各个阶段均符合预定的质量和性能要求。具体标准包括以下几个方面：

1. **需求特性**
   * 完整性：所有用户需求和功能需求都应当被充分捕捉和记录。
   * 明确性：需求描述应当清晰、无歧义，确保开发团队能够准确理解和实现。
   * 一致性：需求文档与项目目标和用户预期一致，无冲突和重复。
   * 可验证性：需求具有可测量的标准，便于后期的验证和测试。
2. **设计的合理性和可行性**
   * 系统架构设计：系统架构合理、稳定，能够支持预期的负载和扩展需求。
   * 模块设计：模块划分明确，各模块之间的接口和依赖关系清晰。
   * 技术方案：选择的技术方案成熟可靠，能够满足项目需求。
   * UI/UX设计：界面设计符合用户体验原则，易于使用，视觉效果良好。
3. **代码的质量和规范性**
   * 代码规范：代码遵循团队制定的编码规范和最佳实践，包括命名、注释、格式等方面。
   * 代码质量：代码逻辑清晰、结构合理，无冗余代码。
   * 代码审查：通过代码审查工具和团队审查，确保代码的正确性和质量。
   * 单元测试：编写充分的单元测试，确保代码功能的正确性和稳定性。
4. **功能的实现程度和测试通过率**
   * 功能实现：按照需求文档完整实现所有功能，无遗漏和错误。
   * 功能测试：功能模块经过充分的测试，测试用例覆盖全面，测试通过率高。
   * 缺陷率：功能模块缺陷率低，且所有已发现缺陷都被及时修复。
   * 用户体验：功能实现符合用户预期，操作简便，用户反馈良好。
5. **系统集成的顺利程度和测试结果**
   * 集成测试：各功能模块集成后，应当通过系统集成测试，确保模块间协同工作正常。
   * 性能测试：系统在预期负载下应当表现良好，响应时间和资源使用率在可接受范围内。
   * 安全测试：系统需要经过严格的安全测试，无明显漏洞和安全隐患。
   * 稳定性：系统运行稳定，无频繁崩溃和重大故障。
6. **用户反馈和验收结果**
   * 用户满意度：用户对系统的使用体验满意，反馈积极。
   * 需求满足度：系统功能和性能应当达到用户需求和预期，验收测试结果良好。
   * 培训效果：用户和管理员经过培训后能够熟练使用系统。
   * 持续改进：根据用户反馈进行改进和优化，确保系统不断提升用户体验和功能完善。

通过严格的评审标准和过程管理，我们方可确保“易拜”小程序项目的高质量交付，满足用户需求，实现预期目标和效益。

#### 3.6.4 评审方法

评审将采用多种方法，包括会议评审、文档评审和测试评审，确保“易拜”小程序项目的各个方面均符合预定标准。具体步骤如下：

1. **准备评审材料：**在进行评审前，相关人员需准备好所有必要的评审材料。这些材料包括但不限于需求文档、设计图纸、代码和测试报告等。准备充分的材料能够确保评审过程的高效和有序，使每个环节都能得到详细的审查和讨论。
2. **召开评审会议：**组织相关人员召开正式的评审会议。在会议中，团队成员对评审材料进行详细讨论，分析项目的各个方面，包括需求的明确性、设计的合理性、代码的质量和功能的实现等。会议过程中，评审人员需记录所有的评审意见和建议，确保所有问题都被准确捕捉和记录。
3. **形成评审报告：**评审会议结束后，由评审主持人负责汇总会议内容，形成正式的评审报告。该报告应详细列出评审过程中发现的所有问题、改进建议以及任何需要进一步讨论的事项。评审报告不仅是对评审会议的总结，也是后续问题跟踪和解决的依据。
4. **问题跟踪和解决：**根据评审报告中提出的问题和建议，项目团队需进行相应的修改和优化。在此过程中，团队需要持续跟踪每个问题的解决情况，确保所有问题都能得到有效处理。此外，团队还应定期召开会议，检查问题解决的进度，并根据实际情况进行调整，确保项目的顺利进行和最终质量的达成。

#### 3.6.5 评审工具

评审过程中将使用以下工具：

* 项目管理工具（如JIRA、Trello）进行任务和问题的跟踪
* 代码管理工具（如Git）进行代码审查
* 协作工具（如Office、Notion）进行文档共享和评审

#### 3.6.6 评审日程

根据项目的整体开发计划，我们制定了详细的评审日程表，确保每个评审阶段按时进行，并为评审会议预留足够的时间。

<table><thead><tr><th width="166" align="center">评审阶段</th><th width="181" align="center">日期</th><th align="center">主要内容</th></tr></thead><tbody><tr><td align="center">需求评审</td><td align="center">2024/04/19</td><td align="center">制定需求文档、功能规格说明书</td></tr><tr><td align="center">设计评审</td><td align="center">2024/04/26</td><td align="center">系统设计文档、界面设计原型</td></tr><tr><td align="center">代码评审</td><td align="center">2024/05/04</td><td align="center">源代码、单元测试结果</td></tr><tr><td align="center">功能评审</td><td align="center">2024/05/08</td><td align="center">功能实现情况、功能测试结果</td></tr><tr><td align="center">系统集成评审</td><td align="center">2024/05/12</td><td align="center">系统集成测试结果</td></tr><tr><td align="center">验收评审</td><td align="center">2024/05/19</td><td align="center">验收测试结果、用户反馈</td></tr></tbody></table>

#### 3.6.7 评审反馈和改进

每次评审结束后，我们团队都会收集评审反馈，总结评审中的经验和教训，不断改进评审过程，提高评审的有效性和项目的整体质量。

通过详细的产品评审计划，我们方可确保“易拜”小程序项目的每个阶段都能得到充分的检查和优化，从而提高项目的成功率和用户满意度。

### 3.7 项目跟踪计划

#### 3.7.1 跟踪目标

本跟踪计划的目标在于确保易拜 E-bike 项目按计划顺利进行，及时发现并解决潜在问题，提升团队沟通效率，具体目标包括：

**确保项目按时推进：**

* 精确监控项目各阶段的进度，确保项目按照既定的时间表进行。
* 对关键里程碑和交付成果进行重点跟踪，及时发现进度延误并采取纠正措施。

**保障项目质量：**

* 设立质量检查点，确保项目各阶段的工作成果符合质量标准。
* 及时反馈质量问题，督促团队成员进行改进。

**及时发现并解决问题：**

* 定期进行项目风险评估，识别潜在问题和风险。
* 设立问题跟踪机制，确保问题得到及时记录、分析和解决。
* 对重大问题或风险进行专项讨论，制定应对策略。

**提升团队沟通效率：**

* 建立定期沟通机制，确保项目团队、利益相关者及用户之间的信息畅通。
* 利用有效的沟通工具和平台，提高信息传递的效率和准确性。
* 鼓励团队成员积极反馈问题和建议，促进团队协作和知识共享。

#### 3.7.2 跟踪范围

**各阶段的完成情况：**

* 监控并跟踪项目从启动、规划、执行到收尾等各个阶段的完成情况。
* 对照项目计划，检查各阶段的任务是否已按时完成，确保项目按计划推进。
* 对于未完成或延期完成的任务，要分析原因，并制定相应的补救措施

**项目质量：**

* 对软件进行定期测试和性能检查，确保产品性能达到预定标准。
* 收集用户反馈，分析软件问题，制定改进措施，不断提升软件服务和性能。

**项目风险：**

* 定期进行项目风险评估，识别潜在的风险因素，制定应对策略。
* 监控潜在风险的变化情况，确保风险应对策略的有效性。
* 分配责任人负责实施应对措施，并监控其执行情况并根据情况进行调整优化。

#### 3.7.3 跟踪方法

1. **周例会：**每周召开项目团队例会，汇报项目进度、问题和风险，讨论解决方案。
2. **进度报告：**每周编制项目进度报告，汇总本周工作内容、进度情况和下周工作计划。
3. **项目总结会：**在项目阶段性时间点进行工作总结，并检查当前阶段性成果是否渡河质量标准。
4. **专题会议：**针对当前的风险情况进行分析，讨论潜在风险的应对方法，并对已存在的风险讨论解决方法、确认解决进度。
5. **状态检查：**由项目经理进行整体状态检查，部门负责人进行部门内状态检查。

#### 3.7.4 跟踪时间安排

本部分仅对例会外无规律时间的事件进行时间安排，未在下表列出的时间安排可见项目里程碑。

<table><thead><tr><th width="181" align="center">跟踪时间</th><th width="266" align="center">会议地点</th><th align="center">时间</th></tr></thead><tbody><tr><td align="center">风险分析专题会议</td><td align="center">深圳校区小研修间-图书馆405</td><td align="center">2024/4/24、2024/5/18</td></tr><tr><td align="center">整体状态检查</td><td align="center">深圳校区小研修间-图书馆506</td><td align="center">2024/4/28、2024/5/19</td></tr><tr><td align="center">前端状态检查</td><td align="center">深圳校区小研修间-图书馆405</td><td align="center">2024/4/30、2024/5/15</td></tr><tr><td align="center">后端状态检查</td><td align="center">深圳校区小研修间-图书馆506</td><td align="center">2024/4/30、2024/5/15</td></tr><tr><td align="center">测试状态检查</td><td align="center">深圳校区小研修间-图书馆502</td><td align="center">2024/4/30、2024/5/20</td></tr></tbody></table>

#### 3.7.5 跟踪负责人

|   职务  |  姓名 |                        任务                       |
| :---: | :-: | :---------------------------------------------: |
|  项目经理 | 刘书睿 | 负责整体项目的跟踪管理，包括协调团队成员、汇总项目进度、成本和风险等信息，确保项目按计划进行。 |
| 前端负责人 | 沈鹏飞 |       负责前端任务的跟踪管理，包括定期汇报任务进度、遇到的问题和解决方案等。       |
| 后端负责人 | 唐锦洲 |       负责后端任务的跟踪管理，包括定期汇报任务进度、遇到的问题和解决方案等。       |
| 测试负责人 | 吴恺云 |       负责测试任务的跟踪管理，包括定期汇报任务进度、遇到的问题和解决方案等。       |

#### 3.7.6 跟踪措施和调整

1. **发现问题**：通过周例会、进度报告、质量检查和风险评估等方式，发现项目执行过程中出现的问题和风险。
2. **制定措施**：针对发现的问题和风险，项目团队需制定相应的解决措施或调整方案，确保问题得到及时解决或项目按计划进行。
3. **实施措施**：按照制定的措施或调整方案，项目团队需及时采取措施或调整项目计划，确保项目顺利推进。
4. **跟踪效果评估**：对实施措施或调整后的项目进行跟踪，确保问题得到解决或项目按计划进行。如问题仍未解决或项目进展不如预期，需重新评估并制定新的解决措施或调整方案。

### 3.8 培训计划

#### 3.8.1 培训目标

本培训计划的目标是确保团队成员能够熟练掌握项目所需的技能和知识，提高工作效率，提高工作质量。具体目标包括：

* 增强设计团队和前端团队使用现代前端技术的能力，提升界面设计和用户体验设计的专业水平，确保团队能够高效地开发出符合业务需求的响应式和交互式网页应用。
* 提升后端团队使用Python和Django框架开发后端服务的能力并学习微软API设计理念的实践应用，以便能够设计和实现符合当前业界最佳实践的高效、可维护的后端系统。
* 加强测试团队的专业能力，确保团队能够有效地进行前端和后端的测试，使用先进的测试工具和方法，以提高软件的质量和可靠性。
* 强化团队协作精神和项目管理技能，提高团队的整体执行力和项目成功率。

#### 3.8.2 培训内容

* 软件项目基础知识培训：包括项目概述、项目目标、项目计划、项目流程等内容；
* 技术知识培训：根据项目需求确定培训内容，包括技术框架、开发工具、编程语言等方面；
* 团队协作培训：包括团队协作意识培养、沟通技巧培训、冲突解决等方面；
* 项目管理培训：包括项目计划制定、进度管理、风险管理等方面。

#### 3.8.3 培训方式

本培训计划采用多种培训方式，包括：

* 线上培训：利用网络平台进行培训，成员可以随时随地进行学习，并在线上讨论区发表自己的见解；
* 线下培训：在图书馆研讨室共同学习，面对面探讨更复杂的问题。
* 自主学习：鼓励成员自主学习，根据个人情况选择学习方式和学习时间。

#### 3.8.4 培训时间安排

<table><thead><tr><th width="203" align="center">培训内容</th><th width="263" align="center">培训地点</th><th align="center">培训时间</th></tr></thead><tbody><tr><td align="center">软件项目基础</td><td align="center">深圳校区小研修间-图书馆405</td><td align="center">1天</td></tr><tr><td align="center">技术深入与实践</td><td align="center">深圳校区小研修间-图书馆502</td><td align="center">2天</td></tr><tr><td align="center">团队协作与沟通</td><td align="center">深圳校区小研修间-图书馆405</td><td align="center">上午</td></tr><tr><td align="center">项目管理与综合应用</td><td align="center">深圳校区小研修间-图书馆506</td><td align="center">下午</td></tr></tbody></table>

### 3.9 沟通计划

#### 3.9.1 沟通目标

* 确保所有团队成员对项目进度和目标有清晰的理解。
* 及时解决问题和冲突。
* 维持项目的透明度，确保所有相关方都持续更新。

#### 3.9.2 沟通方法和工具

* 各种项目文档
* 各种项目规范
* 各种项目报告
* 项目会议与会议记录
* 电子邮件
* 电话
* 其他：微信、Notion和Gitbook

#### 3.9.3 利益相关方沟通计划

<table><thead><tr><th width="166" align="center">沟通工作名称</th><th width="103" align="center">沟通方</th><th width="100" align="center">沟通形式</th><th align="center">负责人</th></tr></thead><tbody><tr><td align="center">校园电动车管理</td><td align="center">保卫处</td><td align="center">电话</td><td align="center">黄楚丹、刘畅</td></tr><tr><td align="center">充电设施管理</td><td align="center">长盛泰富</td><td align="center">邮件</td><td align="center">唐锦洲</td></tr><tr><td align="center">电动车交易</td><td align="center">车店老板</td><td align="center">面谈</td><td align="center">刘子豪、刘书睿</td></tr><tr><td align="center">群众需求</td><td align="center">同学</td><td align="center">面谈</td><td align="center">吴恺云</td></tr><tr><td align="center">需求调研</td><td align="center">大众</td><td align="center">线上问卷</td><td align="center">刘畅、沈鹏飞、刘子豪</td></tr></tbody></table>

#### 3.9.4 项目信息计划

<table><thead><tr><th width="313" align="center">报表名称</th><th align="center">填报人</th></tr></thead><tbody><tr><td align="center">《项目开发计划》</td><td align="center">项目全体成员</td></tr><tr><td align="center">《软件需求说明书》</td><td align="center">项目全体成员</td></tr><tr><td align="center">《问题定义及可行性分析》</td><td align="center">刘畅</td></tr><tr><td align="center">《后端接口定义》</td><td align="center">唐锦洲</td></tr><tr><td align="center">《设计说明书》</td><td align="center">刘书睿、唐锦洲、沈鹏飞、刘畅</td></tr><tr><td align="center">《软件测试计划》</td><td align="center">黄楚丹、吴恺云</td></tr><tr><td align="center">《测试分析报告》</td><td align="center">黄楚丹、吴恺云</td></tr><tr><td align="center">《用户手册》</td><td align="center">刘子豪、刘畅、沈鹏飞</td></tr></tbody></table>

#### 3.9.5 会议管理

<table><thead><tr><th width="149" align="center">会议名称</th><th width="237" align="center">会议内容</th><th width="92" align="center">举行频度</th><th align="center">参与人员</th></tr></thead><tbody><tr><td align="center">项目例会</td><td align="center">项目每周执行情况汇总和通报，报告当前截止工作进度，以及讨论本周工作协调和调整。跟踪项目本周来的状态，包括需求、进度、成本、质量和风险等内容</td><td align="center">每周三</td><td align="center">项目全体成员</td></tr><tr><td align="center">项目总结会</td><td align="center">当前项目阶段或里程碑工作结束时进行工作总结</td><td align="center">里程碑</td><td align="center">项目全体成员</td></tr><tr><td align="center">协调会</td><td align="center">项目各组之间的协调会，协调各种资源配置和调度</td><td align="center">不定期</td><td align="center">各部门负责人</td></tr><tr><td align="center">专题会议</td><td align="center">针对出现的特殊、重大的事件进行专题讨论，包括技术问题、重大变更和严重冲突</td><td align="center">不定期</td><td align="center">项目全体成员</td></tr><tr><td align="center">分组定期检查</td><td align="center">包括日查和周查，检查项目进度和质量</td><td align="center">每周2-3次</td><td align="center">各部门成员</td></tr><tr><td align="center">项目定期检查</td><td align="center">周查，检查各组情况</td><td align="center">每周1次</td><td align="center">各部门成员</td></tr></tbody></table>

#### 3.9.6 组间协作计划

<table><thead><tr><th width="117" align="center">协作内容</th><th align="center">提供方</th><th align="center">接收方</th><th>接收标准</th></tr></thead><tbody><tr><td align="center">UI设计</td><td align="center">设计部门</td><td align="center">开发部门-前端</td><td>设计稿完整，满足功能需求，已审批通过</td></tr><tr><td align="center">前端设计</td><td align="center">开发部门-前端</td><td align="center">开发部门-后端</td><td>功能页面完整实现</td></tr><tr><td align="center">API文档</td><td align="center">开发部门-后端</td><td align="center">开发部门-前端</td><td>文档清晰完整，包括所有必要的细节和示例</td></tr><tr><td align="center">接口实现</td><td align="center">开发部门-后端</td><td align="center">开发部门-前端</td><td>接口符合文档描述，无错误，响应时间快</td></tr><tr><td align="center">集成代码</td><td align="center">开发部门</td><td align="center">测试部门</td><td>代码运行稳定，符合开发规范，准备好进行测试</td></tr><tr><td align="center">功能测试报告</td><td align="center">测试部门</td><td align="center">开发部门</td><td>测试报告详细，包含测试结果和发现的问题</td></tr><tr><td align="center">性能测试和安全测试结果</td><td align="center">测试部门</td><td align="center">开发部门 </td><td>测试覆盖全面，问题清晰记录，提出优化建议</td></tr><tr><td align="center">最终部署的软件版本</td><td align="center">开发部门</td><td align="center">测试部门</td><td>软件无严重错误，性能符合预期</td></tr></tbody></table>
