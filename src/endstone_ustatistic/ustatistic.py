import os
import json
import math

from endstone import Player, ColorFormat
from endstone.plugin import Plugin
from endstone.command import Command, CommandSender
from endstone.form import ModalForm, Dropdown, ActionForm
from endstone.event import *

from endstone_ustatistic.lang import load_lang_data

current_dir = os.getcwd()

first_dir = os.path.join(current_dir, "plugins", "ustatistic")

if not os.path.exists(first_dir):
    os.mkdir(first_dir)

statistical_data_file_path = os.path.join(first_dir, "statistical_data.json")

lang_dir = os.path.join(first_dir, "lang")

if not os.path.exists(lang_dir):
    os.mkdir(lang_dir)


class ustatistic(Plugin):
    api_version = '0.10'

    def __init__(self):
        super().__init__()

        # load data: statistical data
        if not os.path.exists(statistical_data_file_path):
            with open(statistical_data_file_path, "w") as f:
                statistical_data = {}
                json_str = json.dumps(statistical_data, indent=4, ensure_ascii=False)
                f.write(json_str)
        else:
            with open(statistical_data_file_path, "r") as f:
                statistical_data = json.loads(f.read())

        self.statistical_data = statistical_data

        # load data: lang
        self.lang_data = load_lang_data(lang_dir)

    def on_enable(self):
        self.register_events(self)

        self.server.scheduler.run_task(self, self.player_online_time_task, delay=0, period=1200)

        self.logger.info(
            f"{ColorFormat.YELLOW}"
            f"U-Statistic is enabled..."
        )

    commands = {
        "ustc": {
            "description": "Call out the main form of U-Statistic",
            "usages": ["/ustc"],
            "permissions": ["ustatistic.command.ustc"]
        }
    }

    permissions = {
        "ustatistic.command.ustc": {
            "description": "Call out the main form of U-Statistic",
            "default": True
        }
    }

    def on_command(self, sender: CommandSender, command: Command, args: list[str]):
        if command.name == 'ustc':
            if not isinstance(sender, Player):
                sender.send_message(
                    f"{ColorFormat.RED}"
                    f"This command can only be executed by a player..."
                )

                return

            player_name_list = [player_name for player_name in self.statistical_data.keys()]

            player_name_list.sort(key=lambda x:x[0].lower(), reverse=False)

            dropdown = Dropdown(
                label=f"{ColorFormat.GREEN}"
                      f"{self.get_text(sender, 'main_form.dropdown.label')}",
                options=player_name_list,
                default_index=0
            )

            main_form = ModalForm(
                title=f"{ColorFormat.BOLD}{ColorFormat.LIGHT_PURPLE}"
                      f"{self.get_text(sender, 'main_form.title')}",
                controls=[dropdown],
                submit_button=f"{ColorFormat.YELLOW}"
                              f"{self.get_text(sender, 'main_form.submit_button')}",
                on_close=None
            )

            def on_submit(p: Player, json_str: str):
                data = json.loads(json_str)

                player_name = player_name_list[data[0]]

                values = self.statistical_data[player_name]

                break_count = values["break_count"]

                place_count = values["place_count"]

                death_count = values["death_count"]

                online_time = values["online_time"]

                year_minute = 365 * 24 * 60
                day_minute = 24 * 60
                hour_minute = 60

                year = online_time // year_minute
                remain = online_time % year_minute

                day = remain // day_minute
                remain %= day_minute

                hour = remain // hour_minute
                minute = remain % hour_minute

                online_time_display = f"{year}Y{day}D{hour}H{minute}M"

                kill_player_count = values["kill_player_count"]

                kill_mob_count = values["kill_mob_count"]

                pick_up_item_count = values["pick_up_item_count"]

                drop_item_count = values["drop_item_count"]

                move_distance = values["move_distance"]

                result_form = ActionForm(
                    title=f"{ColorFormat.BOLD}{ColorFormat.LIGHT_PURPLE}"
                          f"{player_name}",
                    content=f'{ColorFormat.GREEN}'
                            f'{self.get_text(p, "online_time")}: '
                            f'{ColorFormat.WHITE}'
                            f'{online_time_display}\n'
                            f'{ColorFormat.GREEN}'
                            f'{self.get_text(p, "break_count")}: '
                            f'{ColorFormat.WHITE}'
                            f'{break_count}\n'
                            f'{ColorFormat.GREEN}'
                            f'{self.get_text(p, "place_count")}: '
                            f'{ColorFormat.WHITE}'
                            f'{place_count}\n'
                            f'{ColorFormat.GREEN}'
                            f'{self.get_text(p, "death_count")}: '
                            f'{ColorFormat.WHITE}'
                            f'{death_count}\n'
                            f'{ColorFormat.GREEN}'
                            f'{self.get_text(p, "kill_player_count")}: '
                            f'{ColorFormat.WHITE}'
                            f'{kill_player_count}\n'
                            f'{ColorFormat.GREEN}'
                            f'{self.get_text(p, "kill_mob_count")}: '
                            f'{ColorFormat.WHITE}'
                            f'{kill_mob_count}\n'
                            f'{ColorFormat.GREEN}'
                            f'{self.get_text(p, "pick_up_item_count")}: '
                            f'{ColorFormat.WHITE}'
                            f'{pick_up_item_count}\n'
                            f'{ColorFormat.GREEN}'
                            f'{self.get_text(p, "drop_item_count")}: '
                            f'{ColorFormat.WHITE}'
                            f'{drop_item_count}\n'
                            f'{ColorFormat.GREEN}'
                            f'{self.get_text(p, "move_distance")}: '
                            f'{ColorFormat.WHITE}'
                            f'{move_distance}',
                    on_close=self.back_to_main_form
                )

                result_form.add_button(
                    f"{ColorFormat.YELLOW}"
                    f"{self.get_text(p, 'result_form.button')}",
                    icon="textures/ui/refresh_light",
                    on_click=self.back_to_main_form
                )

                p.send_form(result_form)

            main_form.on_submit = on_submit

            sender.send_form(main_form)

    def save_statistical_data(self):
        with open(statistical_data_file_path, "w+") as f:
            json_str = json.dumps(self.statistical_data, indent=4, ensure_ascii=False)
            f.write(json_str)

    @event_handler
    def on_player_join(self, e: PlayerJoinEvent):
        if self.statistical_data.get(e.player.name) is None:
            self.statistical_data[e.player.name] = {
                "break_count": 0,
                "place_count": 0,
                "death_count": 0,
                "kill_player_count": 0,
                "kill_mob_count": 0,
                "online_time": 0,
                "pick_up_item_count": 0,
                "drop_item_count": 0,
                "move_distance": 0
            }

            self.save_statistical_data()

    @event_handler
    def on_player_break(self, e: BlockBreakEvent):
        self.statistical_data[e.player.name]["break_count"] += 1

        self.save_statistical_data()

    @event_handler
    def on_player_place(self, e: BlockPlaceEvent):
        self.statistical_data[e.player.name]["place_count"] += 1

        self.save_statistical_data()

    @event_handler
    def on_player_death(self, e: PlayerDeathEvent):
        self.statistical_data[e.player.name]["death_count"] += 1

        source = e.damage_source.damaging_actor

        if isinstance(source, Player):
            source_name = source.name

            self.statistical_data[source_name]["kill_player_count"] += 1

        self.save_statistical_data()

    @event_handler
    def on_actor_death(self, e: ActorDeathEvent):
        source = e.damage_source.damaging_actor

        if isinstance(source, Player):
            source_name = source.name

            self.statistical_data[source_name]["kill_mob_count"] += 1

            self.save_statistical_data()

    def player_online_time_task(self):
        online_player_list = self.server.online_players

        if len(online_player_list) != 0:
            for online_player in online_player_list:
                self.statistical_data[online_player.name]["online_time"] += 1

            self.save_statistical_data()

    @event_handler
    def on_player_pick_up_item(self, e: PlayerPickupItemEvent):
        num = e.item.item_stack.amount

        self.statistical_data[e.player.name]["pick_up_item_count"] += num

        self.save_statistical_data()

    @event_handler
    def on_player_drop_item(self, e: PlayerDropItemEvent):
        num = e.item.amount

        self.statistical_data[e.player.name]["drop_item_count"] += num

        self.save_statistical_data()

    @event_handler
    def on_player_move(self, e: PlayerMoveEvent):
        from_location = e.from_location

        to_location = e.to_location

        from_pos = [
            math.floor(from_location.x),
            math.floor(to_location.y),
            math.floor(to_location.z)
        ]

        to_pos = [
            math.floor(to_location.x),
            math.floor(to_location.y),
            math.floor(to_location.z)
        ]

        if from_pos != to_pos:
            square_distance = 0

            for i in range(3):
                square_distance += (from_pos[i] - to_pos[i])**2

            distance = round(square_distance**0.5)

            self.statistical_data[e.player.name]["move_distance"] += distance

            self.save_statistical_data()

    # API - Read only
    def api_get_statistical_data(self, statistical_type: str) -> dict:
        result = {}

        for key, value in self.statistical_data.items():
            result[key] = value[statistical_type]

        return result

    def api_get_player_statistical_data(self, statistical_type: str, player_name: str) -> int:
        return self.statistical_data[player_name][statistical_type]

    def get_text(self, player: Player, text_key: str) -> str:
        player_lang = player.locale

        try:
            if self.lang_data.get(player_lang) is None:
                text_value = self.lang_data["en_US"][text_key]
            else:
                if self.lang_data[player_lang].get(text_key) is None:
                    text_value = self.lang_data["en_US"][text_key]
                else:
                    text_value = self.lang_data[player_lang][text_key]

            return text_value
        except Exception as e:
            self.logger.error(
                f"{ColorFormat.RED}"
                f"{e}"
            )

            return text_key

    def back_to_main_form(self, player: Player):
        player.perform_command('ustc')