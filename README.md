# GLaDOS 自动签到⚡

- 基于 [Python](https://www.python.org/)语言
- 可自定义签到时间（crontab）
- 支持多账户
- 支持部署在[青龙面板](https://github.com/whyour/qinglong)
- 支持多种通知推送方式
- [更新日志](#更新日志)

## 简单介绍一下GLaDOS

>GLaDOS是一家高速稳定的V2Ray/Trojan机场，超过4年的老品牌，官方网站使用自主开发的管理系统，属于技术派的老站，支持WireGuard协议加速，而且流量套餐性价比非常高。

GLaDOS家的优惠活动非常良心，新账号注册一段时间后基本都会赠送一次30天的基础套餐激活码，如果你的账户是教育版edu账户，甚至可以直接得到365天的基础套餐。不仅如此，每天签到也会获得一天当前套餐的续期，因此才有了本项目。

[GLaDOS 项目地址](https://github.com/glados-network/GLaDOS)

## 使用说明

### 一、准备工作

- 账号的 cookie（并非仅此单一获取方式）

  1. 注册 GLaDos 并登陆，在首页往下拉，找到 **我的会员 > 会员签到**

     ![checkin_entrance](assets/checkin_entrance.png)

  2. 点击跳转到签到页面

     ![checkin_page](assets/checkin_page.png)

  3. 打开 "开发者工具"，通常快捷键为 **F12**，或是点击 **浏览器选项 > 更多工具 > 开发者工具**，打开后如图所示点击 "**network**" 标签

     ![devtools](assets/devtools.png)

  4. 在签到页面点击签到，相对应的开发者工具 **network** 标签下会出现 "**checkin**" 请求，点击该请求，会出现更多信息，找到 "**Request Headers**" 里的 "**cookie**"，接下来设置密钥时需要用到

     ![cookie](assets/cookie.png)
## 二、在青龙面板中设置环境变量

![cookie](assets/GR_cookie.png)
- 多账号多次添加，运行脚本将自动遍历变量
## 三、在青龙中拉取本仓库
```
ql repo https://github.com/hennessey-v/GlaDOS_Checkin_ql.git "checkin.py" "backUp|assets|README.md" "sendNotify.py"
```
## 四、运行脚本查看运行结果

![cookie](assets/push_detail.png)

## 更新日志

### [1.0.0] - 2023-01-12

项目发布

#### 变更

- 兼容多账户，推送信息增加账户邮箱信息提示

#### 新增

- 多账号签到
- 多种推送渠道
  - Bark服务
  - TGBot推送
  - QQ机器人
  - 企业微信应用
  - 企业微信BOT
  - 微信推送Plus+


## 鸣谢
- 部分程序代码来源于开源项目[glados_checkin](https://github.com/akinlau/glados_checkin)，此外md文档风格及部分内容借鉴于[DullSword](https://github.com/DullSword)大佬


## Star⭐

**如果你觉得这个项目还不错的话，可以支持一下点个 Star⭐.**
