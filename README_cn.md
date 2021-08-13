# CommandTraverse

**中文版** | [English](https://github.com/zhangtianli2006/CommandTraverse/blob/master/README.md)

一个用 [MCDR](https://github.com/Fallen-Breath/MCDReforged) 实现的插件，用于自定义指令的使用权限（支持 Carpet mod）。

![License](https://img.shields.io/github/license/zhangtianli2006/CommandTraverse?label=License&style=flat-square) ![Last Commit](https://img.shields.io/github/last-commit/zhangtianli2006/CommandTraverse?label=Last%20Commit&style=flat-square)

## 安装

1. 安装 [MCDR](https://github.com/Fallen-Breath/MCDReforged).
2. 把 `CommandTraverse.py` 放入 `plugin/` 文件夹.

## 玩家的使用方式

`!!cmd` 显示帮助信息。

`!!cmd <command>` 以配置的权限运行指令。

`!!cmd check_per <command>` 查看运行一条指令的最低权限要求。

`!!cmd check_my_per` 查看玩家自身的权限（仅玩家可用）。

`!!cmd run_as <player> <command>` 简化 `/execute as <player> at <player> run <command>` （需要玩家拥有 `/execute` 权限）。

**例子**

`!!cmd tp @a @s`

`!!cmd gamemode spectator @s`

`!!cmd check_per summon`

`!!cmd check_my_per`

`!!cmd run_as steve tp alex @s`

如果玩家的权限不够，会返回  `No permission`。

**!! 注意 !!**

插件还在开发中，还有这些虫：
1. 指令的返回信息无法显示给玩家。
2. 指令都会被当做聊天消息处理，会泄露给其他玩家。

[![PRs Welcome](https://img.shields.io/badge/PRs-welcome-brightgreen.svg?style=flat-square)](http://makeapullrequest.com)

## 权限设置

1. 设置 MCDR 的权限（`permissions.yml`）。
2. 设置（修改） `config/cmd_tvs.json`。

在 `config/cmd_tvs.json` 中, `"指令": 数字` 数字是使用指令的最低权限。

权限和数字的对应表如下：

| MCDR 中的权限名称 | 对应的数字 |
|:---------------:|:--------:|
|      guest      |    0     |
|      user       |    1     |
|      helper     |    2     |
|      admin      |    3     |
|      owner      |    4     |

可以在 `"others"` 中添加其他的指令。

```json
{
    "permissions": {
        "vanilla": {
            "msg": 0,
            ...
            "setblock": 2,
            ...
            "ban": 3,
            ...
            "save-off": 4
        },
        "carpet": {
            "log": 0,
            ...
            "info": 1,
            ...
            "carpet": 3
        },
        "others": {
            "your_own_command": <your_own_level_setting>
        }
    }
}
```
