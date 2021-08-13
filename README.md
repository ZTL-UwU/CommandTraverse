# CommandTraverse

**English** | [中文版](https://github.com/zhangtianli2006/CommandTraverse/blob/master/README_cn.md)

An [MCDR](https://github.com/Fallen-Breath/MCDReforged) plugin to customize command permissions, supports Carpet mod.

![License](https://img.shields.io/github/license/zhangtianli2006/CommandTraverse?label=License&style=flat-square) ![Last Commit](https://img.shields.io/github/last-commit/zhangtianli2006/CommandTraverse?label=Last%20Commit&style=flat-square)

## Installation

1. Install [MCDR](https://github.com/Fallen-Breath/MCDReforged).
2. Place `CommandTraverse.py` in the `plugin/` folder.
3. Start the server and use it!

## Player Usage

`!!cmd` Show help message.

`!!cmd <command>` Run command using MCDR permission.

`!!cmd check_per <command>` Check the permission requirement of a command.

`!!cmd check_my_per` Check my permission level (player-only).

**Example**

`!!cmd tp @a @s`

`!!cmd gamemode spectator @s`

`!!cmd check_per summon`

If a player doesn't reach the permission requirement, `No permission` will be returned.

**!! Warning !!**

This plugin is still under development, there are these bugs remaining: 
1. The default text response is not shown.
2. All commands will be treated as chat messages and get shown to all players.

[![PRs Welcome](https://img.shields.io/badge/PRs-welcome-brightgreen.svg?style=flat-square)](http://makeapullrequest.com)

## Permission configuration

1. Set the MCDR's default permission setting `permissions.yml`.
2. Configure `config/cmd_tvs.json`.

In `config/cmd_tvs.json`, the number is the minimum permission required for the command before it, change them according to your needs.

The numbers represent the permissions like the table below.

| permission names in MCDR | numbers for them |
|:------------------------:|:----------------:|
|           guest          |         0        |
|           user           |         1        |
|           helper         |         2        |
|           admin          |         3        |
|           owner          |         4        |

Add your own commands in `"others"`.

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
