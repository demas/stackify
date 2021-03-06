import commands
import ui
from cli import Command
from cli import CommandType
from cli import POSITION_LIST
from cli import Parser

ui.say_hello()
parser = Parser([
    Command(command_type=CommandType.EQUAL, value="init", action=commands.init),
    Command(command_type=CommandType.EQUAL, value="f", action=commands.fetch_and_ls),  # todo: get list of actions
    Command(command_type=CommandType.START_WITH, value="ls", action=commands.show_questions_by_tag),
    Command(command_type=CommandType.START_WITH, value="s ", action=commands.show_questions),
    Command(command_type=CommandType.START_WITH, value="sn ", action=commands.show_new_questions),
    Command(command_type=CommandType.START_WITH, value="del", action=commands.delete_questions),
    Command(command_type=CommandType.START_WITH, value="hide", action=commands.hide_tag),
    Command(command_type=CommandType.START_WITH, value="unhide", action=commands.unhide_tag),
    Command(command_type=CommandType.IN_LIST, value=POSITION_LIST, action=commands.open_question),
    Command(command_type=CommandType.START_WITH, value="o", action=commands.open_questions_list),
])

while True:
    message = input("> ")
    parser.process_message(message)
