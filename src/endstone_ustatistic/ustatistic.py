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

player_break_count_data_file_path = os.path.join(first_dir, "player-break-count.json")

player_place_count_data_file_path = os.path.join(first_dir, "player-place-count.json")

player_death_count_data_file_path = os.path.join(first_dir, "player-death-count.json")

player_kill_player_count_data_file_path = os.path.join(first_dir, "player-kill-player-count.json")

player_kill_mob_count_data_file_path = os.path.join(first_dir, "player-kill-mob-count.json")

player_online_time_data_file_path = os.path.join(first_dir, "player-online-time.json")

player_pick_up_item_count_data_file_path = os.path.join(first_dir, "player-pick-up-item-count.json")

player_drop_item_count_data_file_path = os.path.join(first_dir, "player-drop-item-count.json")

player_move_distance_data_file_path = os.path.join(first_dir, "player-move-distance.json")

lang_dir = os.path.join(first_dir, "lang")

if not os.path.exists(lang_dir):
    os.mkdir(lang_dir)


class ustatistic(Plugin):
    api_version = '0.10'

    def __init__(self):
        super().__init__()

        # load data: player break count
        if not os.path.exists(player_break_count_data_file_path):
            with open(player_break_count_data_file_path, "w") as f:
                player_break_count_data = {}
                json_str = json.dumps(player_break_count_data, indent=4, ensure_ascii=False)
                f.write(json_str)
        else:
            with open(player_break_count_data_file_path, "r") as f:
                player_break_count_data = json.loads(f.read())

        self.player_break_count_data = player_break_count_data

        # load data: player place count
        if not os.path.exists(player_place_count_data_file_path):
            with open(player_place_count_data_file_path, "w") as f:
                player_place_count_data = {}
                json_str = json.dumps(player_place_count_data, indent=4, ensure_ascii=False)
                f.write(json_str)
        else:
            with open(player_place_count_data_file_path, "r") as f:
                player_place_count_data = json.loads(f.read())

        self.player_place_count_data = player_place_count_data

        # load data: player death count
        if not os.path.exists(player_death_count_data_file_path):
            with open(player_death_count_data_file_path, "w") as f:
                player_death_count_data = {}
                json_str = json.dumps(player_death_count_data, indent=4, ensure_ascii=False)
                f.write(json_str)
        else:
            with open(player_death_count_data_file_path, "r") as f:
                player_death_count_data = json.loads(f.read())

        self.player_death_count_data = player_death_count_data

        # load data: player kill player count
        if not os.path.exists(player_kill_player_count_data_file_path):
            with open(player_kill_player_count_data_file_path, "w") as f:
                player_kill_player_count_data = {}
                json_str = json.dumps(player_kill_player_count_data, indent=4, ensure_ascii=False)
                f.write(json_str)
        else:
            with open(player_kill_player_count_data_file_path, "r") as f:
                player_kill_player_count_data = json.loads(f.read())

        self.player_kill_player_count_data = player_kill_player_count_data

        # load data: player kill mob count
        if not os.path.exists(player_kill_mob_count_data_file_path):
            with open(player_kill_mob_count_data_file_path, "w") as f:
                player_kill_mob_count_data = {}
                json_str = json.dumps(player_kill_mob_count_data, indent=4, ensure_ascii=False)
                f.write(json_str)
        else:
            with open(player_kill_mob_count_data_file_path, "r") as f:
                player_kill_mob_count_data = json.loads(f.read())

        self.player_kill_mob_count_data = player_kill_mob_count_data

        # load data: player online time
        if not os.path.exists(player_online_time_data_file_path):
            with open(player_online_time_data_file_path, "w") as f:
                player_online_time_data = {}
                json_str = json.dumps(player_online_time_data, indent=4, ensure_ascii=False)
                f.write(json_str)
        else:
            with open(player_online_time_data_file_path, "r") as f:
                player_online_time_data = json.loads(f.read())

        self.player_online_time_data = player_online_time_data

        # load data: player pick up item count
        if not os.path.exists(player_pick_up_item_count_data_file_path):
            with open(player_pick_up_item_count_data_file_path, "w") as f:
                player_pick_up_item_count_data = {}
                json_str = json.dumps(player_pick_up_item_count_data, indent=4, ensure_ascii=False)
                f.write(json_str)
        else:
            with open(player_pick_up_item_count_data_file_path, "r") as f:
                player_pick_up_item_count_data = json.loads(f.read())

        self.player_pick_up_item_count_data = player_pick_up_item_count_data

        # load data: player drop item count
        if not os.path.exists(player_drop_item_count_data_file_path):
            with open(player_drop_item_count_data_file_path, "w") as f:
                player_drop_item_count_data = {}
                json_str = json.dumps(player_drop_item_count_data, indent=4, ensure_ascii=False)
                f.write(json_str)
        else:
            with open(player_drop_item_count_data_file_path, "r") as f:
                player_drop_item_count_data = json.loads(f.read())

        self.player_drop_item_count_data = player_drop_item_count_data

        # load data: player move distance
        if not os.path.exists(player_move_distance_data_file_path):
            with open(player_move_distance_data_file_path, "w") as f:
                player_move_distance_data = {}
                json_str = json.dumps(player_move_distance_data, indent=4, ensure_ascii=False)
                f.write(json_str)
        else:
            with open(player_move_distance_data_file_path, "r") as f:
                player_move_distance_data = json.loads(f.read())

        self.player_move_distance_data = player_move_distance_data

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

            player_name_list = [player_name for player_name in self.player_online_time_data.keys()]

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

                break_count = self.player_break_count_data[player_name]

                place_count = self.player_place_count_data[player_name]

                death_count = self.player_death_count_data[player_name]

                online_time = self.player_online_time_data[player_name]

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

                kill_player_count = self.player_kill_player_count_data[player_name]

                kill_mob_count = self.player_kill_mob_count_data[player_name]

                pick_up_item_count = self.player_pick_up_item_count_data[player_name]

                drop_item_count = self.player_drop_item_count_data[player_name]

                move_distance = self.player_move_distance_data[player_name]

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

    # save data
    def save_player_break_count_data(self):
        with open(player_break_count_data_file_path, "w+") as f:
            json_str = json.dumps(self.player_break_count_data, indent=4, ensure_ascii=False)
            f.write(json_str)

    def save_player_place_count_data(self):
        with open(player_place_count_data_file_path, "w+") as f:
            json_str = json.dumps(self.player_place_count_data, indent=4, ensure_ascii=False)
            f.write(json_str)

    def save_player_death_count_data(self):
        with open(player_death_count_data_file_path, "w+") as f:
            json_str = json.dumps(self.player_death_count_data, indent=4, ensure_ascii=False)
            f.write(json_str)

    def save_player_online_time_data(self):
        with open(player_online_time_data_file_path, "w+") as f:
            json_str = json.dumps(self.player_online_time_data, indent=4, ensure_ascii=False)
            f.write(json_str)

    def save_player_kill_player_count_data(self):
        with open(player_kill_player_count_data_file_path, "w+") as f:
            json_str = json.dumps(self.player_kill_player_count_data, indent=4, ensure_ascii=False)
            f.write(json_str)

    def save_player_kill_mob_count_data(self):
        with open(player_kill_mob_count_data_file_path, "w+") as f:
            json_str = json.dumps(self.player_kill_mob_count_data, indent=4, ensure_ascii=False)
            f.write(json_str)

    def save_player_pick_up_item_count_data(self):
        with open(player_pick_up_item_count_data_file_path, "w+") as f:
            json_str = json.dumps(self.player_pick_up_item_count_data, indent=4, ensure_ascii=False)
            f.write(json_str)

    def save_player_drop_item_count_data(self):
        with open(player_drop_item_count_data_file_path, "w+") as f:
            json_str = json.dumps(self.player_drop_item_count_data, indent=4, ensure_ascii=False)
            f.write(json_str)

    def save_player_move_distance_data(self):
        with open(player_move_distance_data_file_path, "w+") as f:
            json_str = json.dumps(self.player_move_distance_data, indent=4, ensure_ascii=False)
            f.write(json_str)

    @event_handler
    def on_player_join(self, e: PlayerJoinEvent):
        if self.player_online_time_data.get(e.player.name) is None:
            player_name = e.player.name

            self.player_break_count_data[player_name] = 0
            self.save_player_break_count_data()

            self.player_place_count_data[player_name] = 0
            self.save_player_place_count_data()

            self.player_death_count_data[player_name] = 0
            self.save_player_death_count_data()

            self.player_online_time_data[player_name] = 0
            self.save_player_online_time_data()

            self.player_kill_player_count_data[player_name] = 0
            self.save_player_kill_player_count_data()

            self.player_kill_mob_count_data[player_name] = 0
            self.save_player_kill_mob_count_data()

            self.player_pick_up_item_count_data[player_name] = 0
            self.save_player_pick_up_item_count_data()

            self.player_drop_item_count_data[player_name] = 0
            self.save_player_drop_item_count_data()

            self.player_move_distance_data[player_name] = 0
            self.save_player_move_distance_data()

    @event_handler
    def on_player_break(self, e: BlockBreakEvent):
        self.player_break_count_data[e.player.name] += 1

        self.save_player_break_count_data()

    @event_handler
    def on_player_place(self, e: BlockPlaceEvent):
        self.player_place_count_data[e.player.name] += 1

        self.save_player_place_count_data()

    @event_handler
    def on_player_death(self, e: PlayerDeathEvent):
        self.player_death_count_data[e.player.name] += 1

        self.save_player_death_count_data()

        source = e.damage_source.damaging_actor

        if isinstance(source, Player):
            source_name = source.name

            self.player_kill_player_count_data[source_name] += 1

            self.save_player_kill_player_count_data()

    @event_handler
    def on_actor_death(self, e: ActorDeathEvent):
        source = e.damage_source.damaging_actor

        if isinstance(source, Player):
            source_name = source.name

            self.player_kill_mob_count_data[source_name] += 1

            self.save_player_kill_mob_count_data()

    def player_online_time_task(self):
        online_player_list = self.server.online_players

        if len(online_player_list) != 0:
            for online_player in online_player_list:
                self.player_online_time_data[online_player.name] += 1

            self.save_player_online_time_data()

    @event_handler
    def on_player_pick_up_item(self, e: PlayerPickupItemEvent):
        num = e.item.item_stack.amount

        self.player_pick_up_item_count_data[e.player.name] += num

        self.save_player_pick_up_item_count_data()

    @event_handler
    def on_player_drop_item(self, e: PlayerDropItemEvent):
        num = e.item.amount

        self.player_drop_item_count_data[e.player.name] += num

        self.save_player_drop_item_count_data()

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

            self.player_move_distance_data[e.player.name] += distance

            self.save_player_move_distance_data()

    # API - Read only
    def api_get_statistical_data(self, statistical_type: str) -> dict:
        if statistical_type == "online_time":
            return self.player_online_time_data
        elif statistical_type == "break_count":
            return self.player_break_count_data
        elif statistical_type == "place_count":
            return self.player_place_count_data
        elif statistical_type == "death_count":
            return self.player_death_count_data
        elif statistical_type == "kill_player_count":
            return self.player_kill_player_count_data
        elif statistical_type == "kill_mob_count":
            return self.player_kill_mob_count_data
        elif statistical_type == "pick_up_item_count":
            return self.player_pick_up_item_count_data
        elif statistical_type == "drop_item_count":
            return self.player_drop_item_count_data
        else:
            return self.player_move_distance_data

    def api_get_player_statistical_data(self, statistical_type: str, player_name: str):
        if statistical_type == "online_time":
            if self.player_online_time_data.get(player_name) is None:
                self.logger.error(
                    f"{ColorFormat.RED}"
                    f"Player data not found.."
                )

                return

            return self.player_online_time_data[player_name]

        elif statistical_type == "break_count":
            if self.player_break_count_data.get(player_name) is None:
                self.logger.error(
                    f"{ColorFormat.RED}"
                    f"Player data not found.."
                )

                return

            return self.player_break_count_data[player_name]

        elif statistical_type == "place_count":
            if self.player_place_count_data.get(player_name) is None:
                self.logger.error(
                    f"{ColorFormat.RED}"
                    f"Player data not found.."
                )

                return

            return self.player_place_count_data[player_name]

        elif statistical_type == "death_count":
            if self.player_death_count_data.get(player_name) is None:
                self.logger.error(
                    f"{ColorFormat.RED}"
                    f"Player data not found.."
                )

                return

            return self.player_death_count_data[player_name]
        elif statistical_type == "kill_player_count":
            if self.player_kill_player_count_data.get(player_name) is None:
                self.logger.error(
                    f"{ColorFormat.RED}"
                    f"Player data not found.."
                )

                return

            return self.player_kill_player_count_data[player_name]

        elif statistical_type == "kill_mob_count":
            if self.player_kill_mob_count_data.get(player_name) is None:
                self.logger.error(
                    f"{ColorFormat.RED}"
                    f"Player data not found.."
                )

                return

            return self.player_kill_mob_count_data[player_name]

        elif statistical_type == "pick_up_item_count":
            if self.player_pick_up_item_count_data.get(player_name) is None:
                self.logger.error(
                    f"{ColorFormat.RED}"
                    f"Player data not found.."
                )

                return

            return self.player_pick_up_item_count_data[player_name]

        elif statistical_type == "drop_item_count":
            if self.player_drop_item_count_data.get(player_name) is None:
                self.logger.error(
                    f"{ColorFormat.RED}"
                    f"Player data not found.."
                )

                return

            return self.player_drop_item_count_data[player_name]

        else:
            if self.player_move_distance_data.get(player_name) is None:
                self.logger.error(
                    f"{ColorFormat.RED}"
                    f"Player data not found.."
                )

                return

            return self.player_move_distance_data[player_name]

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