print("=" * 60)
print("❄️ 冰雪奇缘主题配色方案设计")
print("=" * 60)
# 冰雪奇缘主题色板
frozen_palette = {
    "primary": {
        "ice_blue": "#8AC6E8",      # 冰雪蓝 - 主色调
        "snow_white": "#F5F7FA",    # 雪白
        "frozen_purple": "#B39BC8",  # 冰晶紫
        "crystal_teal": "#64C4C4",   # 水晶青
        "silver": "#C0C0C0",        # 银白
    },
    "gradients": {
        "main": "linear-gradient(135deg, #8AC6E8 0%, #B39BC8 100%)",  # 冰雪魔法渐变
        "light": "linear-gradient(135deg, #F5F7FA 0%, #E3F2FD 100%)", # 雪地渐变
        "dark": "linear-gradient(135deg, #64C4C4 0%, #8AC6E8 100%)",  # 深冰渐变
        "sparkle": "linear-gradient(135deg, #FFFFFF 0%, #E3F2FD 50%, #FFFFFF 100%)", # 闪烁渐变
    },
    "accents": {
        "gold": "#FFD700",          # 金色点缀（皇冠）
        "pink": "#FFB6C1",          # 淡粉（安娜）
        "green": "#98FB98",         # 淡绿（艾莎礼服）
        "dark_blue": "#4169E1",     # 深蓝（夜空）
    }
}
# 界面组件配色映射
component_colors = {
    "header": frozen_palette["gradients"]["main"],
    "buttons": {
        "primary": frozen_palette["gradients"]["main"],
        "success": "linear-gradient(135deg, #64C4C4 0%, #98FB98 100%)",  # 冰晶绿
        "warning": "linear-gradient(135deg, #FFB6C1 0%, #FFD700 100%)",  # 安娜粉金
        "info": "linear-gradient(135deg, #B39BC8 0%, #E3F2FD 100%)",     # 紫白渐变
    },
    "cards": frozen_palette["primary"]["snow_white"],
    "text": {
        "primary": "#2C3E50",       # 深蓝灰
        "secondary": "#5D6D7E",     # 中灰
        "light": "#7F8C8D",         # 浅灰
        "white": "#FFFFFF",         # 纯白
    }
}
print("🎨 冰雪奇缘主题色板：")
print(f"   冰雪蓝：{frozen_palette['primary']['ice_blue']}")
print(f"   雪白色：{frozen_palette['primary']['snow_white']}")
print(f"   冰晶紫：{frozen_palette['primary']['frozen_purple']}")
print(f"   水晶青：{frozen_palette['primary']['crystal_teal']}")
print(f"   银白色：{frozen_palette['primary']['silver']}")
print("\n🌈 渐变方案：")
for name, gradient in frozen_palette["gradients"].items():
    print(f"   {name}: {gradient}")
print("\n✨ 点缀色：")
for name, color in frozen_palette["accents"].items():
    print(f"   {name}: {color}")
# 生成CSS变量
css_variables = ":root {\n"
for category, colors in frozen_palette.items():
    if isinstance(colors, dict):
        for name, value in colors.items():
            if isinstance(value, dict):
                for subname, subvalue in value.items():
                    var_name = f"--frozen-{category}-{name}-{subname}"
                    css_variables += f"  {var_name}: {subvalue};\n"
            else:
                var_name = f"--frozen-{category}-{name}"
                css_variables += f"  {var_name}: {value};\n"
css_variables += "}"
print("\n🎯 生成的CSS变量：")
print(css_variables[:200] + "...")
print("\n" + "=" * 60)
print("✅ 冰雪奇缘配色方案设计完成！")
print("=" * 60)
utils.set_state(
    success=True,
    palette=frozen_palette,
    gradients=frozen_palette["gradients"],
    accents=frozen_palette["accents"],
    css_variables=css_variables
)