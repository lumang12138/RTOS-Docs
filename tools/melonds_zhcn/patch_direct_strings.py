#!/usr/bin/env python3
from pathlib import Path
import sys

root = Path(sys.argv[1] if len(sys.argv) > 1 else "melonDS")
qt = root / "src/frontend/qt_sdl"

def replace_quoted(path: Path, mapping: dict[str, str]):
    text = path.read_text(encoding="utf-8")
    changed = 0
    for en, zh in mapping.items():
        old = '"' + en.replace('"', '\\"') + '"'
        new = '"' + zh.replace('"', '\\"') + '"'
        count = text.count(old)
        if count:
            text = text.replace(old, new)
            changed += count
    path.write_text(text, encoding="utf-8", newline="\n")
    print(f"{path.name}: translated {changed} direct string occurrence(s)")

window = {
    "File": "文件",
    "Open ROM...": "打开 ROM...",
    "Open recent": "最近打开",
    "Boot firmware": "启动固件",
    "DS slot: ": "DS 卡槽：",
    "Insert cart...": "插入卡带...",
    "Eject cart": "弹出卡带",
    "GBA slot: ": "GBA 卡槽：",
    "Insert ROM cart...": "插入 ROM 卡带...",
    "Insert add-on cart": "插入扩展卡带",
    "Import savefile": "导入存档",
    "Save state": "保存即时存档",
    "Load state": "读取即时存档",
    "File...": "文件...",
    "Undo state load": "撤销读取即时存档",
    "Open melonDS directory": "打开 melonDS 数据目录",
    "Quit": "退出",
    "System": "系统",
    "Pause": "暂停",
    "Reset": "重置",
    "Stop": "停止",
    "Frame step": "单帧步进",
    "Power management": "电源管理",
    "Date and time": "日期和时间",
    "Enable cheats": "启用金手指",
    "Setup cheat codes": "金手指设置",
    "ROM info": "ROM 信息",
    "RAM search": "RAM 搜索",
    "Manage DSi titles": "管理 DSi 软件",
    "Multiplayer": "联机",
    "Launch new instance": "启动新实例",
    "Host LAN game": "创建局域网游戏",
    "Join LAN game": "加入局域网游戏",
    "View": "视图",
    "Screen size": "屏幕大小",
    "Screen rotation": "屏幕旋转",
    "Screen gap": "屏幕间距",
    "Screen layout": "屏幕布局",
    "Natural": "自然",
    "Vertical": "垂直",
    "Horizontal": "水平",
    "Hybrid": "混合",
    "Swap screens": "交换屏幕",
    "Screen sizing": "屏幕比例",
    "Even": "等大",
    "Emphasize top": "突出上屏",
    "Emphasize bottom": "突出下屏",
    "Auto": "自动",
    "Top only": "仅上屏",
    "Bottom only": "仅下屏",
    "Force integer scaling": "强制整数缩放",
    "Aspect ratio": "宽高比",
    "Top": "上屏",
    "Bottom": "下屏",
    "Open new window": "打开新窗口",
    "Screen filtering": "屏幕滤镜",
    "Show OSD": "显示 OSD",
    "Config": "配置",
    "Emu settings": "模拟设置",
    "Preferences...": "偏好设置...",
    "Input and hotkeys": "输入与快捷键",
    "Video settings": "视频设置",
    "Camera settings": "相机设置",
    "Audio settings": "音频设置",
    "Multiplayer settings": "联机设置",
    "Wifi settings": "Wi-Fi 设置",
    "Firmware settings": "固件设置",
    "Interface settings": "界面设置",
    "Path settings": "路径设置",
    "Savestate settings": "即时存档设置",
    "Separate savefiles": "即时存档使用独立存档文件",
    "Limit framerate": "限制帧率",
    "Audio sync": "音频同步",
    "Help": "帮助",
    "About...": "关于...",
    "Fullscreen": "全屏",
    "Toggle fullscreen": "切换全屏",
}
replace_quoted(qt / "Window.cpp", window)

cheats = {
    "(new category)": "（新分类）",
    "(new AR code)": "（新 AR 代码）",
    "Confirm deletion": "确认删除",
    "Really delete the selected item?": "确定删除所选项目吗？",
    "Select cheat database...": "选择金手指数据库...",
    "R4 cheat database (*.dat);;Any file (*.*)": "R4 金手指数据库 (*.dat);;所有文件 (*.*)",
    "Failed to open this cheat database file.": "无法打开该金手指数据库文件。",
    "No cheat codes were found in this database for the current game.": "该数据库中没有找到当前游戏对应的金手指代码。",
    "Error: no name entered.": "错误：未输入名称。",
    "Error: the code entered is empty or invalid.": "错误：输入的代码为空或无效。",
}
replace_quoted(qt / "CheatsDialog.cpp", cheats)

# Dynamic import dialog messages that are not generated from .ui files.
import_dialog = qt / "CheatImportDialog.cpp"
if import_dialog.exists():
    replace_quoted(import_dialog, {
        "Cheat import": "导入金手指",
        "Import cheats": "导入金手指",
        "No matching cheats found.": "未找到匹配的金手指。",
        "Remove existing cheats": "移除现有金手指",
    })

# Common file-dialog filters and user-visible errors in the main window.
replace_quoted(qt / "Window.cpp", {
    "Nintendo DS ROMs (*.nds *.srl *.dsi *.ids);;All files (*.*)": "Nintendo DS ROM (*.nds *.srl *.dsi *.ids);;所有文件 (*.*)",
    "Game Boy Advance ROMs (*.gba *.agb);;All files (*.*)": "Game Boy Advance ROM (*.gba *.agb);;所有文件 (*.*)",
    "All files (*.*)": "所有文件 (*.*)",
    "Select ROM": "选择 ROM",
    "Select savefile": "选择存档",
})
