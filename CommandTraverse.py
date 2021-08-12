import json
import os

from mcdreforged.api.all import *

PLUGIN_METADATA = {
    'id': 'cmd_tvs',
    'version': '0.1.0',
    'name': 'CommandTraverse',
    'author': [
            'zhangtianli2006',
    ],
    'link': 'https://github.com/zhangtianli2006/CommandTraverse'
}

CONFIG_PATH = 'config/cmd_tvs.json'

DEFAULT_CONFIG = {
    # 0:guest 1:user 2:helper 3:admin 4:owner
    'permissions': {
        'vanilla': {
            '?': 0,
            'help': 0,
            'list': 0,
            'me': 0,
            'msg': 0,
            'teammsg': 0,
            'tell': 0,
            'w': 0,
            'trigger': 0,
            'advancement': 3,
            'bossbar': 2,
            'clear': 3,
            'clone': 3,
            'data': 2,
            'datapack': 3,
            'effect': 3,
            'enchant': 3,
            'experience': 2,
            'fill': 3,
            'function': 3,
            'gamemode': 3,
            'give': 2,
            'kill': 3,
            'locate': 2,
            'loot': 3,
            'particle': 2,
            'playsound': 2,
            'recipe': 2,
            'reload': 3,
            'replaceitem': 3,
            'say': 1,
            'schedule': 2,
            'scoreboard': 2,
            'seed': 2,
            'setblock': 3,
            'setworldspawn': 3,
            'spawnpoint': 3,
            'spreadplayers': 3,
            'stop': 4,
            'stopsound': 2,
            'summon': 3,
            'tag': 3,
            'team': 2,
            'teleport': 3,
            'tellraw': 1,
            'time': 3,
            'title': 2,
            'weather': 2,
            'whitelist': 3,
            'worldborder': 3,
            'xp': 2,
            'execute': 4,
            'defaultgamemode': 3,
            'deop': 3,
            'op': 3,
            'difficulty': 3,
            'forceload': 3,
            'gamerule': 3,
            'ban': 3,
            'ban-ip': 3,
            'banlist': 3,
            'debug': 3,
            'kick': 3,
            'pardon': 3,
            'pardon-ip': 3,
            'setidletimeout': 3,
            'save-all': 3,
            'alwaysday': 3,
            'daylock': 3,
            'perf': 4,
            'publish': 4,
            'save-off': 4,
            'save-on': 4,
            'stop': 4
        },
        'carpet': {
            'log': 0,
            'info': 1,
            'ping': 1,
            'perimeterinfo': 1,
            'distance': 1,
            'c': 2,
            's': 2,
            'player': 2,
            'carpet': 3,
            'draw': 3,
            'tick': 3
        }
    }
}


def print_message(source: CommandSource, msg, tell=True, prefix='[CMD] '):
    msg = prefix + msg
    if source.is_player and not tell:
        source.get_server().say(msg)
    else:
        source.reply(msg)


class Config:
    def __init__(self, file_path: str):
        self.file_path = file_path
        self.data = {}

    def read_config(self):
        with open(self.file_path, 'r', encoding='UTF-8') as file:
            self.data.update(json.load(file))

    def write_config(self):
        with open(self.file_path, 'w', encoding='UTF-8') as file:
            json.dump(self.data, file, indent=4)

    def load(self, server: ServerInterface):
        if not os.path.isdir(os.path.dirname(self.file_path)):
            os.makedirs(os.path.dirname(self.file_path))
            server.logger.info('Config dir not found, created')
        if not os.path.isfile(self.file_path):
            self.data = DEFAULT_CONFIG
            self.write_config()
            server.logger.info(
                'Config file not found, using default')
        else:
            try:
                self.read_config()
            except json.JSONDecodeError:
                self.data = DEFAULT_CONFIG
                self.write_config()
                server.logger.info(
                    'Invalid config file, using default')


config = Config(CONFIG_PATH)


def on_load(server: ServerInterface, old):
    server.register_help_message(
        '!!<command>', 'Run command using MCDR permissions')
    config.load(server)


def on_user_info(server: ServerInterface, info: Info):
    if info.content.startswith('!!cmd') and info.player != None:
        if info.content == '!!cmd':
            info.get_command_source().reply('!!<command> Run commands using MCDR permissions')

        no_marker = info.content.lstrip('!!cmd').lstrip()
        cmd_header = no_marker.split(' ')[0]

        permission_req = config.data['permissions']['vanilla'].get(
            cmd_header, -1)
        if permission_req == -1:
            permission_req = config.data['permissions']['carpet'].get(
                cmd_header, -1)
        if permission_req == -1:
            info.get_command_source().reply(
                RText('Unknown command, input §7!!cmd§r for more information'))
        elif info.get_command_source().has_permission(permission_req):
            server.execute('execute as ' + info.player + ' at ' +
                           info.player + ' run ' + no_marker)
        else:
            info.get_command_source().reply('No permission')