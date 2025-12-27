import os
import json


def load_lang_data(lang_dir: str) -> dict:
    zh_CN_file_path = os.path.join(lang_dir, "zh_CN.json")
    en_US_file_path = os.path.join(lang_dir, "en_US.json")

    if not os.path.exists(zh_CN_file_path):
        with open(zh_CN_file_path, "w", encoding="utf-8") as f:
            zh_CN = {
                "main_form.title": "U-Statistic - 主表单",
                "main_form.dropdown.label": "选择玩家...",
                "main_form.submit_button": "查询",
                "result_form.button": "返回",

                "break_count": "破坏数",
                "place_count": "放置数",
                "death_count": "死亡数",
                "online_time": "在线时长",
                "kill_player_count": "击杀玩家数",
                "kill_mob_count": "击杀生物数",
                "pick_up_item_count": "拾取物品数",
                "drop_item_count": "丢弃物品数",
                "move_distance": "移动距离"
            }
            json_str = json.dumps(zh_CN, indent=4,ensure_ascii=False)
            f.write(json_str)

    if not os.path.exists(en_US_file_path):
        with open(en_US_file_path, "w", encoding="utf-8") as f:
            en_US = {
                "main_form.title": "U-Statistic - main form",
                "main_form.dropdown.label": "Please select a player...",
                "main_form.submit_button": "Query",
                "result_form.button": "Back to previous",

                "break_count": "Break count",
                "place_count": "Place count",
                "death_count": "Death count",
                "online_time": "Online time",
                "kill_player_count": "Kill player count",
                "kill_mob_count": "Kill mob count",
                "pick_up_item_count": "Pick up item count",
                "drop_item_count": "Drop item count",
                "move_distance": "Move distance"
            }
            json_str = json.dumps(en_US, indent=4,ensure_ascii=False)
            f.write(json_str)

    lang_data = {}

    for lang in os.listdir(lang_dir):
        lang_name = lang.strip(".json")

        lang_file_path = os.path.join(lang_dir, lang)

        with open(lang_file_path, "r", encoding="utf-8") as f:
            lang_data[lang_name] = json.loads(f.read())

    return lang_data
