import yaml
from pathlib import Path
import time

from classify import HIDE_TAGS

CONFIG_FILENAME = "config.yaml"


def load_config():
    config_file = Path(CONFIG_FILENAME)
    if not config_file.exists():
        default_config = {
            "hide_tags": HIDE_TAGS,
            "stackoverflow_key": "",
            "last-sync": int(time.time())
        }
        with open(CONFIG_FILENAME, "w") as f:
            yaml.dump(default_config, f)

    with open(CONFIG_FILENAME, "r") as stream:
        try:
            return yaml.safe_load(stream)
        except yaml.YAMLError as exc:
            print(exc)
            exit(-1)


def save_config(config):
    with open(CONFIG_FILENAME, "w") as f:
        yaml.dump(config, f)


def set_value(param, value):
    config = load_config()
    config[param] = value
    save_config(config)
