<code><a href="https://github.com/U-Blocks/U_Beautiful_Chat"><img height="20" src="./logo/logo.jpg" alt="UStatistic" /></a>&nbsp;<a href="https://github.com/U-Blocks/U_Beautiful_Chat">UStatistic</a></code>

![Total Git clones](https://img.shields.io/badge/dynamic/json?label=Total%20Git%20clones&query=$&url=https://cdn.jsdelivr.net/gh/umarurize/UStatistic@master/clone_count.txt&color=brightgreen)
![GitHub Downloads (all assets, all releases)](https://img.shields.io/github/downloads/umarurize/UStatistic/total)
![](https://img.shields.io/badge/language-python-blue.svg) 
[![GitHub License](https://img.shields.io/github/license/umarurize/UTP)](LICENSE)

***

### ✨ Introductions
* **9 types of statistical indicators**
* **Free of tedious file editing**
* **Support with full GUI forms**
* **Support with hot reloading**
* **Support with localized multi-language**

<div style="width: 100%; text-align: left;">
  <img src="./images/ustc.jpg" style="max-width: 100%; height: 300px;">
</div>

***

### 📦 Installation
<details>
<summary>Check your Endstone's version</summary>

* **Endstone 0.10.0+**
  * 251220

</details>

<details>
<summary>Check your pre-plugins</summary>

* **Optional pre-plugin**
  * [ZX_UI](https://www.minebbs.com/resources/zx-ui.9830/)

</details>

1. Ensure you have downloaded the correct version and installed all required pre-plugins
2. Place the `.whl` file into your server's `plugins` folder
3. Restart your server
4. Enter the command `/ubd` to call out the main form of UStatistic

***

### 📄 File structure
```
plugins/
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

***

### 🌎 Localized multi-language
* Currently supported localized languages for UStatistic:
- [x] `zh_CN`
- [x] `en_US`
* How to add more languages to UStatistic? Here we use Japanese for an example.
  * Create a file named `ja_JP.json` and place it into `lang` folder
  * Copy all key-value pairs from `en_US.json` and paste them into `ja_JP.json`
  * Refer to the English values and translate them all into Japanese, then save the file.
  * Restart your server, and you're all done!
* If you'd like your translated language to be included as one of the official languages of this plugin, feel free to shoot over a PR.

***

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
***

### 💡 Plugins
- [x] [U-Beautiful-Chat](https://github.com/U-Blocks/U_Beautiful_Chat)
- [ ] UPlayer (Plugin in press)


