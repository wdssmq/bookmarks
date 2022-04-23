# 水水的书签收藏

## 前言

偶尔会发现一些有意思的网址，但是加浏览器书签又不是很必要，就搞了这个站来记录；

发布地址：https://wdssmq.github.io/bookmarks/#/

博客：https://www.wdssmq.com/

搭建：docsify

更新时间： {docsify-updated}

参考：[基于 Github Pages + docsify，我花了半天就搭建好了个人博客 - 知乎](https://zhuanlan.zhihu.com/p/101126727 "基于Github Pages + docsify，我花了半天就搭建好了个人博客 - 知乎")

## 云足迹

终于想明白，比起书签我更需要「云足迹」，只是一直没有合用的工具，直到看到下边项目：

> twfb/DeployIssue：
>
> [https://github.com/twfb/DeployIssue](https://github.com/twfb/DeployIssue "twfb/DeployIssue")

使用 Actions 调用 deploy_issue.py，用于将 issue 内容生成至 docsify 文档；

## 关于 docsify

官网：[docsify](https://docsify.js.org/#/zh-cn/ "docsify") ← 已经指向中文说明

基本的命令备忘：

```bash
# npm i docsify-cli -g
cnpm i docsify-cli -g

# cd "/d/node/bookmarks"
docsify init ./docs

# cd "/d/node/bookmarks"
docsify serve docs
```

注释内容请根据实际情况选用；

配置项
https://docsify.js.org/#/zh-cn/configuration?id=submaxlevel

之前了解过一些同类型的东西，尤以 wiki-in-box 和本项目最为类似，只是需要额外实现 web 环境。

而 docsify 基于 node.js 部属，可以直接开一个 web 服务，同时修改也能自动刷新；

## 类似的 Wiki 项目

dmscode/Wiki-in-box: 一个可以放在各种网盘，各种空间的，Markdown 语法支持的 Wiki 系统

https://github.com/dmscode/Wiki-in-box

TiddlyWiki — a non-linear personal web notebook

https://tiddlywiki.com/
