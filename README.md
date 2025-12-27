## UStatistic

<code><a href="https://github.com/umarurize/UStatistic"><img height="25" src="./logo/logo.jpg" alt="UStatistic" /></a>&nbsp;UStatistic</code>

![Total Git clones](https://img.shields.io/badge/dynamic/json?label=Total%20Git%20clones&query=$&url=https://cdn.jsdelivr.net/gh/umarurize/UStatistic@master/clone_count.txt&color=brightgreen)
![GitHub Downloads (all assets, all releases)](https://img.shields.io/github/downloads/umarurize/UStatistic/total)

### 🔔Introductions
* **Full GUI**
* **9 types of statistical indicators**
* **Localized languages support**
<div style="width: 100%; text-align: left;">
  <img src="./images/ustc.jpg" style="max-width: 100%; height: 250px;">
</div>

### 🔨Installation
<details>
<summary>Check your Endstone's version</summary>

* **Endstone 0.10.0+**
  * 251220

</details>

[Optional pre-plugin] ZX_UI

Put `.whl` file into the endstone plugins folder, and then start the server. Enter the command `/ustc` to call out the main form.

### 💻Download
Now, you can get the release version form this repo or <code><a href="https://www.minebbs.com/resources/umoney-jian-dan-shi-yong-qu-zhi-ling-hua-de-jing-ji-xi-tong.10622/"><img height="20" src="./logo/minebbs.png" alt="Minebbs" /></a>&nbsp;Minebbs</code>.

### 📁File structure
```
Plugins/
├─ ustatistic/
│  ├─ player-break-count.json
│  ├─ player-place-count.json
│  ├─ player-death-count.json
│  ├─ player-kill-mob-count.json
│  ├─ player-kill-player-count.json
│  ├─ player-drop-item-count.json
│  ├─ player-pick-up-item-count.json
│  ├─ player-move-distance.json
│  ├─ player-online-time.json
│  ├─ lang/
│  │  ├─ zh_CN.json
│  │  ├─ en_US.json
```

### 🌐Languages
- [x] `zh_CN`
- [x] `en_US`

Of course, you can add your mother language to UStatistic, just create `XX_XX.json` (such as `ja_JP.json`) and translate value with reference to `en_US.json`.

You can also create a PR to this repo to make your mother language one of the official languages of UStatistic.

### 💪API
```python
"""
Read only

Ustatistic provides two types of API.

For type A, you can get the data of all players for the specified statistical indicators,
and it returns a dict.

For type B, you can get the data of a specified player for a specified statistical indicator,
and it returns an int.
"""

# Type A
self.server.plugin_manager.get_plugin("ustatistic").api_get_statistical_data(statistical_type: str) -> dict

# Type B
self.server.plugin_manager.get_plugin("ustatistic").api_get_player_statistical_data(statistical_type: str, player_name: str) -> int

"""
What is statistical type?

Statistical type is used to specify a statistical indicator, you can select one of the following values for input.
- break_count
- place_count
- death_count
- kill_mob_count
- kill_player_count
- drop_item_count
- pick_up_item_count
- move_distance
- online_time
"""
```

### :electric_plug:Plugins
- [ ] U-Beautiful-Chat (Plugin in press)
- [ ] UPlayer (Plugin in press)

![](https://img.shields.io/badge/language-python-blue.svg) [![GitHub License](https://img.shields.io/github/license/umarurize/UTP)](LICENSE)
