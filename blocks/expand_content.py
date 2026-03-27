import json
print("=" * 60)
print("📚 汪汪队英语乐园 - 内容库扩展计划")
print("=" * 60)
# 扩展题库
extended_questions = {
    "letters": [
        {"letter": "A", "word": "Apple", "emoji": "🍎", "color": "红色"},
        {"letter": "B", "word": "Banana", "emoji": "🍌", "color": "黄色"},
        {"letter": "C", "word": "Cat", "emoji": "🐱", "color": "灰色"},
        {"letter": "D", "word": "Dog", "emoji": "🐶", "color": "棕色"},
        {"letter": "E", "word": "Elephant", "emoji": "🐘", "color": "灰色"},
        {"letter": "F", "word": "Fish", "emoji": "🐟", "color": "蓝色"},
        {"letter": "G", "word": "Giraffe", "emoji": "🦒", "color": "黄色"},
        {"letter": "H", "word": "House", "emoji": "🏠", "color": "红色"},
        {"letter": "I", "word": "Ice Cream", "emoji": "🍦", "color": "白色"},
        {"letter": "J", "word": "Jellyfish", "emoji": "🐙", "color": "透明"}
    ],
    "categories": [
        {
            "name": "动物世界",
            "words": [
                {"en": "Cat", "zh": "猫", "emoji": "🐱", "sound": "meow"},
                {"en": "Dog", "zh": "狗", "emoji": "🐶", "sound": "woof"},
                {"en": "Bird", "zh": "鸟", "emoji": "🐦", "sound": "tweet"},
                {"en": "Fish", "zh": "鱼", "emoji": "🐟", "sound": "blub"},
                {"en": "Rabbit", "zh": "兔子", "emoji": "🐰", "sound": "hop"},
                {"en": "Elephant", "zh": "大象", "emoji": "🐘", "sound": "trumpet"}
            ]
        },
        {
            "name": "水果乐园",
            "words": [
                {"en": "Apple", "zh": "苹果", "emoji": "🍎", "color": "红色"},
                {"en": "Banana", "zh": "香蕉", "emoji": "🍌", "color": "黄色"},
                {"en": "Orange", "zh": "橙子", "emoji": "🍊", "color": "橙色"},
                {"en": "Grape", "zh": "葡萄", "emoji": "🍇", "color": "紫色"},
                {"en": "Watermelon", "zh": "西瓜", "emoji": "🍉", "color": "绿色"},
                {"en": "Strawberry", "zh": "草莓", "emoji": "🍓", "color": "红色"}
            ]
        },
        {
            "name": "颜色认知",
            "words": [
                {"en": "Red", "zh": "红色", "emoji": "🔴", "color": "red"},
                {"en": "Blue", "zh": "蓝色", "emoji": "🔵", "color": "blue"},
                {"en": "Yellow", "zh": "黄色", "emoji": "🟡", "color": "yellow"},
                {"en": "Green", "zh": "绿色", "emoji": "🟢", "color": "green"},
                {"en": "Orange", "zh": "橙色", "emoji": "🟠", "color": "orange"},
                {"en": "Purple", "zh": "紫色", "emoji": "🟣", "color": "purple"}
            ]
        },
        {
            "name": "数字王国",
            "words": [
                {"en": "One", "zh": "一", "emoji": "1️⃣", "count": 1},
                {"en": "Two", "zh": "二", "emoji": "2️⃣", "count": 2},
                {"en": "Three", "zh": "三", "emoji": "3️⃣", "count": 3},
                {"en": "Four", "zh": "四", "emoji": "4️⃣", "count": 4},
                {"en": "Five", "zh": "五", "emoji": "5️⃣", "count": 5},
                {"en": "Six", "zh": "六", "emoji": "6️⃣", "count": 6}
            ]
        }
    ],
    "game_modes": [
        {"id": "flashcard", "name": "闪卡学习", "icon": "📖", "desc": "看图认单词"},
        {"id": "matching", "name": "配对游戏", "icon": "🧩", "desc": "英文中文配对"},
        {"id": "spelling", "name": "拼写练习", "icon": "✍️", "desc": "拼写单词"},
        {"id": "listening", "name": "听力测试", "icon": "🎧", "desc": "听音辨词"},
        {"id": "speaking", "name": "口语练习", "icon": "🗣️", "desc": "跟读发音"},
        {"id": "story", "name": "故事模式", "icon": "📚", "desc": "情景对话"}
    ]
}
print(f"\n📊 内容库统计：")
print(f"   ✅ 字母学习：{len(extended_questions['letters'])} 个字母")
print(f"   ✅ 主题分类：{len(extended_questions['categories'])} 个主题")
print(f"   ✅ 单词总数：{sum(len(cat['words']) for cat in extended_questions['categories'])} 个单词")
print(f"   ✅ 游戏模式：{len(extended_questions['game_modes'])} 种玩法")
print(f"\n🎯 扩展计划：")
print(f"   1. 增加更多主题（身体部位、交通工具、家庭成员等）")
print(f"   2. 添加简单句子和对话")
print(f"   3. 设计汪汪队主题故事线")
print(f"   4. 加入奖励徽章系统")
# 保存到文件
content_file = "/Users/btt/aipywork/CXEbTdw7Fvi2jCCYdUs9c/CZMUn4piLZVxKt55xCPUd/content_library.json"
with open(content_file, 'w', encoding='utf-8') as f:
    json.dump(extended_questions, f, ensure_ascii=False, indent=2)
print(f"\n💾 内容库已保存到：{content_file}")
print("=" * 60)
utils.set_state(success=True, content_file=content_file, stats=extended_questions)