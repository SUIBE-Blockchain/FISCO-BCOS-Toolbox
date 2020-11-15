# FISCO BCOS Toolbox
<!-- ALL-CONTRIBUTORS-BADGE:START - Do not remove or modify this section -->
[![All Contributors](https://img.shields.io/badge/all_contributors-7-orange.svg?style=flat-square)](#contributors-)
<!-- ALL-CONTRIBUTORS-BADGE:END -->
FISCO BCOS Toolbox created by SUIBE-Blockchain-Team.

由上海对外经贸大学区块链技术与应用研究中心研发的针对 FISCO BCOS 的工具箱。

**DEMO:** <https://tools.doge.university/>

![](https://img.shields.io/badge/SUIBE--B-CopyRight-blue)
  [![Build Status](https://travis-ci.com/SUIBE-Blockchain/FISCO_BCOS_Toolbox.svg?branch=master)](https://travis-ci.com/SUIBE-Blockchain/FISCO_BCOS_Toolbox)
  ![](https://img.shields.io/badge/language-python-orange.svg)
  ![](https://img.shields.io/badge/license-MIT-000000.svg)

内容包括：

- FISCO BCOS 地址生成（已完成）
- SDK Config 在线生成 （已完成）
- 开发中的数据模拟（构建中）
- 智能合约案例合集（构建中）
- SDK 功能通过WEB页面调用（构建中）
……

环境变量文件见`.envrc`。

![](https://tva1.sinaimg.cn/large/0081Kckwgy1gkpwnwalq8j30st0mmgov.jpg)

## 1. Toolbox使用演示视频

[上贸大区块链中心打造的「开源区块链开发工具箱」如何助力WeBase](https://www.bilibili.com/video/BV1Sz4y1C7AH)

## 2. Contributors

<!-- ALL-CONTRIBUTORS-LIST: START - Do not remove or modify this section -->
<!-- ALL-CONTRIBUTORS-LIST:START - Do not remove or modify this section -->
<!-- prettier-ignore-start -->
<!-- markdownlint-disable -->
<table>
  <tr>
    <td align="center"><a href="https://github.com/leeduckgo"><img src="https://avatars1.githubusercontent.com/u/12784118?v=4" width="100px;" alt=""/><br /><sub><b>李大狗</b></sub></a><br /><a href="https://github.com/SUIBE-Blockchain/FISCO_BCOS_Toolbox/commits?author=leeduckgo" title="Code">💻</a></td>
    <td align="center"><a href="https://blog.csdn.net/qq_19381989"><img src="https://avatars3.githubusercontent.com/u/45918704?v=4" width="100px;" alt=""/><br /><sub><b>HuiFeng Tang</b></sub></a><br /><a href="https://github.com/SUIBE-Blockchain/FISCO_BCOS_Toolbox/commits?author=99Kies" title="Code">💻</a></td>
    <td align="center"><a href="https://github.com/dengcheng6502"><img src="https://avatars0.githubusercontent.com/u/30894162?v=4" width="100px;" alt=""/><br /><sub><b>Mu Li</b></sub></a><br /><a href="https://github.com/SUIBE-Blockchain/FISCO_BCOS_Toolbox/commits?author=dengcheng6502" title="Code">💻</a></td>
    <td align="center"><a href="http://cnmf.net.cn"><img src="https://avatars1.githubusercontent.com/u/42673461?v=4" width="100px;" alt=""/><br /><sub><b>肖越</b></sub></a><br /><a href="https://github.com/SUIBE-Blockchain/FISCO_BCOS_Toolbox/commits?author=xiaoyue2019" title="Code">💻</a></td>
    <td align="center"><a href="https://github.com/lekko1988"><img src="https://avatars0.githubusercontent.com/u/19570787?v=4" width="100px;" alt=""/><br /><sub><b>lekko1988</b></sub></a><br /><a href="https://github.com/SUIBE-Blockchain/FISCO_BCOS_Toolbox/commits?author=lekko1988" title="Code">💻</a></td>
    <td align="center"><a href="http://hqwangningbo.gitee.io"><img src="https://avatars2.githubusercontent.com/u/57781136?v=4" width="100px;" alt=""/><br /><sub><b>hqwangningbo</b></sub></a><br /><a href="https://github.com/SUIBE-Blockchain/FISCO_BCOS_Toolbox/commits?author=hqwangningbo" title="Code">💻</a></td>
    <td align="center"><a href="https://github.com/whtech"><img src="https://avatars1.githubusercontent.com/u/8427564?v=4" width="100px;" alt=""/><br /><sub><b>whtech</b></sub></a><br /><a href="#infra-whtech" title="Infrastructure (Hosting, Build-Tools, etc)">🚇</a></td>
  </tr>
</table>

<!-- markdownlint-enable -->
<!-- prettier-ignore-end -->
<!-- ALL-CONTRIBUTORS-LIST:END -->
<!-- ALL-CONTRIBUTORS-LIST:END -->

## 3. 安装指南

### 3.1 环境变量配置

将如下内容写入环境变量：

```
export FLASK_APP=autoapp.py
export FLASK_DEBUG=1
export DATABASE_URL=sqlite:///test.db
export SECRET_KEY=123456
export SEND_FILE_MAX_AGE_DEFAULT=31556926
```

注：推荐使用[direnv](https://direnv.net/)进行环境管理。

### 3.2 配置虚拟环境

- 安装

```
virtualenv --no-site-packages venv
```

- 激活

```
. ./venv/bin/activate
```

### 3.3 安装依赖包

```
pip3 install -r requirements.txt
```

### 3.4 初始化数据库

```
python3 manager.py init_db
```

### 3.5 运行！
```
flask run
```
默认管理员账号：admin 密码：admin

默认admin管理页：http://url/admin
