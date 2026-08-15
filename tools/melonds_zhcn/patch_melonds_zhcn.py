#!/usr/bin/env python3
from pathlib import Path
import sys

root = Path(sys.argv[1] if len(sys.argv) > 1 else "melonDS")
main_cpp = root / "src/frontend/qt_sdl/main.cpp"
text = main_cpp.read_text(encoding="utf-8")

if "class ZhCnTranslator final" in text:
    print("zh-CN translator already present")
    raise SystemExit(0)

text = text.replace('#include <QApplication>\n', '#include <QApplication>\n#include <QTranslator>\n#include <QPair>\n')

translator = r'''

// Simplified Chinese UI translation layer for melonDS 1.1.
// Technical terms such as ROM, BIOS, Firmware, JIT, OpenGL, DSi and Action Replay
// are intentionally preserved where that improves clarity for emulator users.
class ZhCnTranslator final : public QTranslator
{
public:
    QString translate(const char* context, const char* sourceText,
                      const char* disambiguation = nullptr, int n = -1) const override
    {
        Q_UNUSED(context);
        Q_UNUSED(disambiguation);
        Q_UNUSED(n);
        if (!sourceText || !*sourceText) return {};

        const QString src = QString::fromUtf8(sourceText);

        struct Pair { const char* en; const char* zh; };
        static const Pair exact[] = {
            {"System", "系统"}, {"Config", "配置"}, {"View", "视图"}, {"Help", "帮助"},
            {"File", "文件"}, {"General", "常规"}, {"Advanced", "高级"}, {"Other", "其他"},
            {"OK", "确定"}, {"Cancel", "取消"}, {"Apply", "应用"}, {"Close", "关闭"},
            {"Yes", "是"}, {"No", "否"}, {"None", "无"}, {"Default", "默认"},
            {"Enabled", "已启用"}, {"Disabled", "已禁用"}, {"Enable", "启用"}, {"Disable", "禁用"},
            {"Auto", "自动"}, {"Automatic", "自动"}, {"Custom", "自定义"}, {"Browse...", "浏览..."},
            {"Open ROM...", "打开 ROM..."}, {"Open ROM", "打开 ROM"}, {"Open recent", "最近打开"},
            {"Open Recent", "最近打开"}, {"Clear recent files", "清除最近文件"},
            {"Boot firmware", "启动固件"}, {"Boot Firmware", "启动固件"},
            {"Boot game directly", "直接启动游戏"}, {"Eject cart", "弹出卡带"},
            {"Pause", "暂停"}, {"Resume", "继续"}, {"Reset", "重置"}, {"Stop", "停止"},
            {"Frame step", "单帧步进"}, {"Frame Step", "单帧步进"},
            {"Save state", "保存即时存档"}, {"Load state", "读取即时存档"},
            {"Save State", "保存即时存档"}, {"Load State", "读取即时存档"},
            {"Undo load state", "撤销读取即时存档"}, {"Undo Load State", "撤销读取即时存档"},
            {"Import savefile...", "导入存档..."}, {"Export savefile...", "导出存档..."},
            {"Import save file...", "导入存档..."}, {"Export save file...", "导出存档..."},
            {"Enable cheats", "启用金手指"}, {"Enable Cheats", "启用金手指"},
            {"Setup cheat codes", "金手指设置"}, {"Setup Cheat Codes", "金手指设置"},
            {"Cheat codes", "金手指"}, {"Cheats", "金手指"}, {"Quit", "退出"}, {"Exit", "退出"},
            {"Emulation settings", "模拟设置"}, {"Emulation Settings", "模拟设置"},
            {"Input and hotkeys", "输入与快捷键"}, {"Input and Hotkeys", "输入与快捷键"},
            {"Input config", "输入设置"}, {"Input Config", "输入设置"},
            {"Video settings", "视频设置"}, {"Video Settings", "视频设置"},
            {"Audio settings", "音频设置"}, {"Audio Settings", "音频设置"},
            {"Camera settings", "相机设置"}, {"Camera Settings", "相机设置"},
            {"Firmware settings", "固件设置"}, {"Firmware Settings", "固件设置"},
            {"Interface settings", "界面设置"}, {"Interface Settings", "界面设置"},
            {"Wi-Fi settings", "Wi-Fi 设置"}, {"Wi-Fi Settings", "Wi-Fi 设置"},
            {"Network settings", "网络设置"}, {"Network Settings", "网络设置"},
            {"Screen layout", "屏幕布局"}, {"Screen Layout", "屏幕布局"},
            {"Screen sizing", "屏幕尺寸"}, {"Screen Sizing", "屏幕尺寸"},
            {"Screen rotation", "屏幕旋转"}, {"Screen Rotation", "屏幕旋转"},
            {"Screen gap", "屏幕间距"}, {"Screen Gap", "屏幕间距"},
            {"Integer scaling", "整数缩放"}, {"Keep aspect ratio", "保持宽高比"},
            {"Swap screens", "交换屏幕"}, {"Swap Screens", "交换屏幕"},
            {"Fullscreen", "全屏"}, {"Window size", "窗口大小"}, {"Window Size", "窗口大小"},
            {"About", "关于"}, {"About melonDS", "关于 melonDS"},
            {"Vertical", "垂直"}, {"Horizontal", "水平"}, {"Hybrid", "混合"}, {"Natural", "自然"},
            {"Top", "上屏"}, {"Bottom", "下屏"}, {"Left", "左"}, {"Right", "右"},
            {"Rotation", "旋转"}, {"0 degrees", "0 度"}, {"90 degrees", "90 度"},
            {"180 degrees", "180 度"}, {"270 degrees", "270 度"},
            {"Renderer", "渲染器"}, {"Software", "软件渲染"}, {"OpenGL", "OpenGL"},
            {"VSync", "垂直同步"}, {"Internal resolution", "内部渲染分辨率"},
            {"Internal Resolution", "内部渲染分辨率"}, {"Display FPS", "显示 FPS"},
            {"Limit framerate", "限制帧率"}, {"Limit Framerate", "限制帧率"},
            {"Threaded 3D renderer", "多线程 3D 渲染"}, {"Threaded renderer", "多线程渲染"},
            {"Better polygons", "改进多边形渲染"}, {"Use VSync", "使用垂直同步"},
            {"Screen filtering", "屏幕滤镜"}, {"Linear filtering", "线性过滤"},
            {"Nearest-neighbor", "最近邻"}, {"Shader", "着色器"},
            {"Audio output", "音频输出"}, {"Audio Output", "音频输出"},
            {"Volume", "音量"}, {"Interpolation", "插值"}, {"Audio sync", "音频同步"},
            {"Audio Sync", "音频同步"}, {"Output device", "输出设备"}, {"Output Device", "输出设备"},
            {"Input device", "输入设备"}, {"Input Device", "输入设备"}, {"Latency", "延迟"},
            {"Microphone", "麦克风"}, {"Microphone input", "麦克风输入"},
            {"Microphone Input", "麦克风输入"}, {"Microphone source", "麦克风来源"},
            {"Device", "设备"}, {"Silence", "静音"}, {"White noise", "白噪声"},
            {"Input", "输入"}, {"Hotkeys", "快捷键"}, {"Keyboard", "键盘"},
            {"Joystick", "手柄"}, {"Controller", "控制器"}, {"Button", "按键"}, {"Key", "按键"},
            {"Clear", "清除"}, {"Clear all", "全部清除"}, {"Reset to defaults", "恢复默认"},
            {"Fast forward", "快进"}, {"Fast Forward", "快进"},
            {"Toggle fast forward", "切换快进"}, {"Toggle Fullscreen", "切换全屏"},
            {"Lid", "合盖"}, {"Mic", "麦克风"},
            {"Console type", "主机类型"}, {"Console Type", "主机类型"},
            {"DS", "DS"}, {"DSi", "DSi"}, {"DS mode", "DS 模式"}, {"DSi mode", "DSi 模式"},
            {"Use external BIOS/firmware files", "使用外部 BIOS/固件文件"},
            {"Use external BIOS", "使用外部 BIOS"}, {"BIOS", "BIOS"}, {"Firmware", "固件"},
            {"ARM9 BIOS", "ARM9 BIOS"}, {"ARM7 BIOS", "ARM7 BIOS"}, {"NAND", "NAND"},
            {"SD card", "SD 卡"}, {"SD Card", "SD 卡"}, {"Enable JIT", "启用 JIT"},
            {"JIT recompiler", "JIT 重编译器"}, {"JIT Recompiler", "JIT 重编译器"},
            {"Max block size", "最大代码块大小"}, {"Fast memory", "快速内存"},
            {"Direct boot", "直接启动"}, {"Language", "语言"}, {"Username", "用户名"},
            {"Birthday", "生日"}, {"Favorite color", "偏好颜色"}, {"Message", "个人信息"},
            {"Battery level", "电池电量"}, {"Charger connected", "已连接充电器"},
            {"Camera", "相机"}, {"Camera source", "相机来源"}, {"Image file", "图像文件"},
            {"Flip horizontally", "水平翻转"}, {"Flip vertically", "垂直翻转"},
            {"Internal camera", "内置相机"}, {"External camera", "外置相机"},
            {"Network", "网络"}, {"Local multiplayer", "本地联机"}, {"LAN", "局域网"},
            {"Netplay", "网络联机"}, {"Direct mode", "直连模式"}, {"Adapter", "网络适配器"},
            {"Host", "主机"}, {"Join", "加入"}, {"Address", "地址"}, {"Port", "端口"},
            {"Connect", "连接"}, {"Disconnect", "断开连接"}, {"Connection", "连接"},
            {"New category", "新建分类"}, {"New Category", "新建分类"},
            {"New AR code", "新建 AR 代码"}, {"New AR Code", "新建 AR 代码"},
            {"Action Replay code", "Action Replay 代码"}, {"Action Replay Code", "Action Replay 代码"},
            {"Delete", "删除"}, {"Rename", "重命名"}, {"Import", "导入"}, {"Export", "导出"},
            {"Import database", "导入数据库"}, {"Import Database", "导入数据库"},
            {"Cheat database", "金手指数据库"}, {"Cheat Database", "金手指数据库"},
            {"Code", "代码"}, {"Code name", "代码名称"}, {"Name", "名称"}, {"Category", "分类"},
            {"No cheats found", "未找到金手指"}, {"Game ID", "游戏 ID"},
            {"Select a file", "选择文件"}, {"Select file", "选择文件"}, {"Select folder", "选择文件夹"},
            {"Error", "错误"}, {"Warning", "警告"}, {"Information", "信息"},
            {"Confirm", "确认"}, {"Failed", "失败"}, {"Success", "成功"},
            {"Loading...", "正在加载..."}, {"Saving...", "正在保存..."},
            {"Not available", "不可用"}, {"Unknown", "未知"}, {"Refresh", "刷新"},
            {"Size", "大小"}, {"Path", "路径"}, {"Folder", "文件夹"}, {"File name", "文件名"},
            {"Read-only", "只读"}, {"Create", "创建"}, {"Format", "格式"},
            {"Always", "始终"}, {"Never", "从不"}, {"Ask", "询问"},
            {"Theme", "主题"}, {"System theme", "跟随系统"}, {"Light", "浅色"}, {"Dark", "深色"},
            {"Interface", "界面"}, {"Status bar", "状态栏"}, {"Tooltips", "工具提示"},
            {"Recent files", "最近文件"}, {"Updates", "更新"}
        };

        for (const Pair& p : exact)
            if (src == QString::fromUtf8(p.en)) return QString::fromUtf8(p.zh);

        // Phrase-level fallback. This deliberately keeps specialist emulator
        // terminology in English while translating ordinary UI wording.
        static const Pair phrases[] = {
            {"Use external BIOS/firmware", "使用外部 BIOS/固件"},
            {"Action Replay", "Action Replay"},
            {"internal resolution", "内部渲染分辨率"},
            {"Internal resolution", "内部渲染分辨率"},
            {"screen layout", "屏幕布局"}, {"Screen layout", "屏幕布局"},
            {"screen sizing", "屏幕尺寸"}, {"Screen sizing", "屏幕尺寸"},
            {"screen rotation", "屏幕旋转"}, {"Screen rotation", "屏幕旋转"},
            {"screen gap", "屏幕间距"}, {"Screen gap", "屏幕间距"},
            {"aspect ratio", "宽高比"}, {"Aspect ratio", "宽高比"},
            {"fast forward", "快进"}, {"Fast forward", "快进"}, {"Fast Forward", "快进"},
            {"save state", "即时存档"}, {"Save state", "保存即时存档"},
            {"load state", "读取即时存档"}, {"Load state", "读取即时存档"},
            {"save file", "存档文件"}, {"Save file", "存档文件"},
            {"cheat database", "金手指数据库"}, {"Cheat database", "金手指数据库"},
            {"cheat code", "金手指代码"}, {"Cheat code", "金手指代码"},
            {"cheats", "金手指"}, {"Cheats", "金手指"}, {"cheat", "金手指"}, {"Cheat", "金手指"},
            {"firmware", "固件"}, {"Firmware", "固件"},
            {"settings", "设置"}, {"Settings", "设置"},
            {"configuration", "配置"}, {"Configuration", "配置"},
            {"renderer", "渲染器"}, {"Renderer", "渲染器"},
            {"resolution", "分辨率"}, {"Resolution", "分辨率"},
            {"filtering", "过滤"}, {"Filtering", "过滤"},
            {"interpolation", "插值"}, {"Interpolation", "插值"},
            {"microphone", "麦克风"}, {"Microphone", "麦克风"},
            {"camera", "相机"}, {"Camera", "相机"},
            {"network", "网络"}, {"Network", "网络"},
            {"audio", "音频"}, {"Audio", "音频"},
            {"video", "视频"}, {"Video", "视频"},
            {"input", "输入"}, {"Input", "输入"},
            {"output", "输出"}, {"Output", "输出"},
            {"device", "设备"}, {"Device", "设备"},
            {"controller", "控制器"}, {"Controller", "控制器"},
            {"joystick", "手柄"}, {"Joystick", "手柄"},
            {"keyboard", "键盘"}, {"Keyboard", "键盘"},
            {"hotkey", "快捷键"}, {"Hotkey", "快捷键"},
            {"button", "按键"}, {"Button", "按键"},
            {"username", "用户名"}, {"Username", "用户名"},
            {"language", "语言"}, {"Language", "语言"},
            {"birthday", "生日"}, {"Birthday", "生日"},
            {"battery", "电池"}, {"Battery", "电池"},
            {"adapter", "适配器"}, {"Adapter", "适配器"},
            {"address", "地址"}, {"Address", "地址"},
            {"connection", "连接"}, {"Connection", "连接"},
            {"category", "分类"}, {"Category", "分类"},
            {"database", "数据库"}, {"Database", "数据库"},
            {"directory", "目录"}, {"Directory", "目录"},
            {"folder", "文件夹"}, {"Folder", "文件夹"},
            {"file", "文件"}, {"File", "文件"},
            {"path", "路径"}, {"Path", "路径"},
            {"size", "大小"}, {"Size", "大小"},
            {"default", "默认"}, {"Default", "默认"},
            {"automatic", "自动"}, {"Automatic", "自动"},
            {"enabled", "已启用"}, {"Enabled", "已启用"},
            {"disabled", "已禁用"}, {"Disabled", "已禁用"},
            {"enable", "启用"}, {"Enable", "启用"},
            {"disable", "禁用"}, {"Disable", "禁用"},
            {"select", "选择"}, {"Select", "选择"},
            {"browse", "浏览"}, {"Browse", "浏览"},
            {"open", "打开"}, {"Open", "打开"},
            {"close", "关闭"}, {"Close", "关闭"},
            {"save", "保存"}, {"Save", "保存"},
            {"load", "加载"}, {"Load", "加载"},
            {"import", "导入"}, {"Import", "导入"},
            {"export", "导出"}, {"Export", "导出"},
            {"create", "创建"}, {"Create", "创建"},
            {"delete", "删除"}, {"Delete", "删除"},
            {"remove", "移除"}, {"Remove", "移除"},
            {"clear", "清除"}, {"Clear", "清除"},
            {"reset", "重置"}, {"Reset", "重置"},
            {"refresh", "刷新"}, {"Refresh", "刷新"},
            {"apply", "应用"}, {"Apply", "应用"},
            {"cancel", "取消"}, {"Cancel", "取消"},
            {"warning", "警告"}, {"Warning", "警告"},
            {"error", "错误"}, {"Error", "错误"},
            {"failed", "失败"}, {"Failed", "失败"},
            {"unknown", "未知"}, {"Unknown", "未知"}
        };

        QString out = src;
        for (const Pair& p : phrases)
            out.replace(QString::fromUtf8(p.en), QString::fromUtf8(p.zh), Qt::CaseSensitive);

        // Translate standard accelerator menu labels while preserving '&'.
        out.replace("&System", "&系统"); out.replace("&Config", "&配置");
        out.replace("&View", "&视图"); out.replace("&Help", "&帮助");
        out.replace("&File", "&文件");

        return out == src ? QString() : out;
    }
};
'''

anchor = 'using namespace melonDS;\n\nQString* systemThemeName;'
if anchor not in text:
    raise RuntimeError("main.cpp anchor not found")
text = text.replace(anchor, 'using namespace melonDS;' + translator + '\n\nQString* systemThemeName;')

install_anchor = '    MelonApplication melon(argc, argv);\n    pathInit();'
if install_anchor not in text:
    raise RuntimeError("application install anchor not found")
text = text.replace(
    install_anchor,
    '    MelonApplication melon(argc, argv);\n'
    '    static ZhCnTranslator zhCnTranslator;\n'
    '    melon.installTranslator(&zhCnTranslator);\n'
    '    pathInit();'
)

# A few user-visible strings bypass Qt translation APIs in upstream 1.1.
direct = {
    'Failed to initialize SDL. This could indicate an issue with your audio driver.\\n\\nThe error was: ': 'SDL 初始化失败，可能是音频驱动存在问题。\\n\\n错误信息：',
    'Unable to write to config.\\nPlease check the write permissions of the folder you placed melonDS in.': '无法写入配置文件。\\n请检查 melonDS 所在文件夹的写入权限。',
    'Warning: use the a.zip|b.nds format at your own risk!\\n': '警告：a.zip|b.nds 这种写法存在兼容风险，请谨慎使用！\\n',
    "SDL couldn't init rumble\\n": 'SDL 无法初始化震动功能\\n',
    "SDL couldn't init joystick\\n": 'SDL 无法初始化手柄\\n',
    "SDL couldn't init motion sensors\\n": 'SDL 无法初始化运动传感器\\n',
}
for a, b in direct.items():
    text = text.replace(a, b)

main_cpp.write_text(text, encoding="utf-8", newline="\n")
print(f"Patched {main_cpp}")
