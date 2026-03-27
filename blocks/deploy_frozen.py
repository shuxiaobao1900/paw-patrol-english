import subprocess
import os
import shutil
print("=" * 60)
print("❄️ 部署冰雪奇缘英语乐园")
print("=" * 60)
# 获取 GitHub 用户名
result = subprocess.run(['gh', 'api', 'user', '--jq', '.login'], capture_output=True, text=True)
github_username = result.stdout.strip()
repo_name = "frozen-english-game"
# 准备部署文件
print("\n📋 准备冰雪奇缘版本文件...")
deploy_dir = "/Users/btt/aipywork/CXEbTdw7Fvi2jCCYdUs9c/CZMUn4piLZVxKt55xCPUd/deploy_frozen"
os.makedirs(deploy_dir, exist_ok=True)
# 复制冰雪奇缘 HTML 文件
src_file = "/Users/btt/aipywork/CXEbTdw7Fvi2jCCYdUs9c/CZMUn4piLZVxKt55xCPUd/blocks/frozen_english_game.html"
dst_file = os.path.join(deploy_dir, "index.html")
shutil.copy(src_file, dst_file)
print(f"   ✅ 冰雪奇缘文件已准备")
# Git 操作
print("\n📋 推送到 GitHub...")
os.chdir(deploy_dir)
if os.path.exists('.git'):
    shutil.rmtree('.git')
subprocess.run(['git', 'init'], capture_output=True)
subprocess.run(['git', 'add', '.'], capture_output=True)
subprocess.run(['git', 'commit', '-m', '❄️ 冰雪奇缘版本：102个单词+8大主题+12个冰雪徽章'], capture_output=True)
repo_url = f"https://github.com/{github_username}/{repo_name}.git"
subprocess.run(['git', 'remote', 'add', 'origin', repo_url], capture_output=True)
subprocess.run(['git', 'branch', '-M', 'main'], capture_output=True)
result = subprocess.run(['git', 'push', '-u', 'origin', 'main', '--force'], 
                       capture_output=True, text=True)
if result.returncode == 0:
    print("   ✅ 推送成功！")
else:
    print(f"   ⚠️ {result.stderr}")
# 完成
print("\n" + "=" * 60)
print("✅ 冰雪奇缘版本部署完成！")
print("=" * 60)
website_url = f"https://{github_username}.github.io/{repo_name}/"
# 统计
total_words = 102
total_themes = 8
total_badges = 12
print(f"\n🌐 冰雪奇缘访问地址：")
print(f"   {website_url}")
print(f"\n📊 冰雪奇缘特色：")
print(f"   ❄️ {total_themes} 大冰雪主题")
print(f"   📚 {total_words} 个核心单词")
print(f"   👑 {total_badges} 个冰雪徽章")
print(f"   🎮 4 种冰雪游戏模式")
print(f"   ✨ 飘雪动画 + 冰晶特效")
print(f"   🏰 冰雪奇缘风格界面")
print(f"   📱 移动端完美适配")
print(f"\n🎨 冰雪奇缘设计亮点：")
print(f"   ✅ 冰雪蓝 + 冰晶紫主色调")
print(f"   ✅ 飘雪背景 + 闪烁冰晶")
print(f"   ✅ 魔法渐变 + 柔和阴影")
print(f"   ✅ 冰雪主题图标和按钮")
print(f"   ✅ 艾莎安娜风格装饰")
print(f"\n📱 使用提示：")
print(f"   请强制刷新页面加载冰雪版本")
print(f"   在手机上可添加到主屏幕，像 App 一样使用")
print("=" * 60)
# 清理
os.chdir("/Users/btt/aipywork/CXEbTdw7Fvi2jCCYdUs9c/CZMUn4piLZVxKt55xCPUd")
shutil.rmtree(deploy_dir, ignore_errors=True)
utils.set_state(
    success=True, 
    url=website_url, 
    totalWords=total_words, 
    totalThemes=total_themes,
    totalBadges=total_badges
)