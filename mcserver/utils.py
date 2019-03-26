import inspect
from os.path import dirname, join

DEFAULT_SERVER_PROPERTIES = {
    'generator-settings': '', 
    'force-gamemode': False, 
    'allow-nether': True,
    'enforce-whitelist': False, 
    'gamemode': 0, 
    'broadcast-console-to-ops': True,
    'enable-query': False, 
    'player-idle-timeout': 0, 
    'difficulty': 1,
    'spawn-monsters': True, 
    'op-permission-level': 4, 
    'pvp': True,
    'snooper-enabled': True, 
    'level-type': 'DEFAULT', 
    'hardcore': False,
    'enable-command-block': False, 
    'max-players': 20,
    'network-compression-threshold': 256, 
    'resource-pack-sha1': '',
    'max-world-size': 29999984, 
    'server-port': 25565, 
    'server-ip': '',
    'spawn-npcs': True, 
    'allow-flight': False, 
    'level-name': 'world',
    'view-distance': 10, 
    'resource-pack': '', 
    'spawn-animals': True, 
    'white-list': False,
    'generate-structures': True, 
    'online-mode': True, 
    'max-build-height': 256,
    'level-seed': '', 
    'prevent-proxy-connections': False, 
    'use-native-transport': True,
    'enable-rcon': False, 
    'motd': 'A Minecraft Server'
}


def get_free_id():
    x = 0
    while True:
        yield x
        x += 1


def open_local(filename: str):
    dir_name = dirname(inspect.stack()[1].filename)
    return open(join(dir_name, filename))


def read_config(file):
    data = {}
    for line in file.readlines():
        line = line.strip()
        if line and not line.startswith("#"):
            k, v = line.split("=", 1)
            data[k] = v
    return data
