from typing import List
from typing import Union


class CommandType:
    EQUAL = "equal"
    START_WITH = "start_with"
    IN_LIST = "in_list"


class Command:
    def __init__(self, command_type: str, value: Union[str, List[str]], action):
        self.command_type = command_type
        self.value = value
        self.action = action


class Parser:
    def __init__(self):
        self.commands: List[Command] = []

    def add_command(self, command: Command) -> None:
        self.commands.append(command)

    def process_message(self, message: str) -> None:
        for command in self.commands:
            if command.command_type == CommandType.EQUAL:
                if message == command.value:
                    return command.action()
            elif command.command_type == CommandType.START_WITH:
                if message.startswith(command.value):
                    params = message[len(command.value):]
                    return command.action(params)
            elif command.command_type == CommandType.IN_LIST:
                if message in command.value:
                    return command.action(message)