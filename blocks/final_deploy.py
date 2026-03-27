import subprocess
import os
import shutil
print("=" * 60)
print("🚀 汪汪队英语乐园 - 最终部署到 GitHub Pages")
print("=" * 60)
# 获取 GitHub 用户名
print("\n📋 步骤1：获取 GitHub 用户信息...")
result = subprocess.run(['gh', 'api', 'user', '--jq', '.login'], capture_output=True, text=True)
if result.returncode == 0:
    github_username = result.stdout.strip()
    print(f"   ✅ GitHub 用户名：{github_username}")
else:
    print("   ❌ 无法获取用户信息，请先运行 gh auth login")
    utils.set_state(success=False, error="未登录 GitHub")
    exit(1)
# 仓库名称
repo_name = "paw-patrol-english-game"
print(f"\n📋 步骤2：准备仓库 '{repo_name}'...")
# 检查仓库是否存在
result = subprocess.run(['gh', 'repo', 'view', repo_name], capture_output=True, text=True)
if result.returncode != 0:
    # 创建新仓库
    print("   正在创建新仓库...")
    result = subprocess.run([
        'gh', 'repo', 'create', repo_name,
        '--public',
        '--description', '🐾 汪汪队英语乐园 - 幼儿园小朋友的英语启蒙游戏',
        '--confirm'
    ], capture_output=True, text=True)
    if result.returncode == 0:
        print(f"   ✅ 仓库创建成功！")
    else:
        print(f"   ❌ 创建失败：{result.stderr}")
        utils.set_state(success=False, error="创建仓库失败")
        exit(1)
else:
    print(f"   ✅ 仓库已存在")
# 准备部署文件
print("\n📋 步骤3：准备部署文件...")
deploy_dir = "/Users/btt/aipywork/CXEbTdw7Fvi2jCCYdUs9c/CZMUn4piLZVxKt55xCPUd/deploy_github"
os.makedirs(deploy_dir, exist_ok=True)
# 复制 HTML 文件
src_file = "/Users/btt/aipywork/CXEbTdw7Fvi2jCCYdUs9c/CZMUn4piLZVxKt55xCPUd/blocks/index_v7.html"
dst_file = os.path.join(deploy_dir, "index.html")
if os.path.exists(src_file):
    shutil.copy(src_file, dst_file)
    print(f"   ✅ 文件已复制：index.html")
else:
    # 尝试其他可能的文件名
    for fname in ['index.html', 'game.html', 'paw_patrol_game.html']:
        test_path = f"/Users/btt/aipywork/CXEbTdw7Fvi2jCCYdUs9c/CZMUn4piLZVxKt55xCPUd/blocks/{fname}"
        if os.path.exists(test_path):
            shutil.copy(test_path, dst_file)
            print(f"   ✅ 文件已复制：{fname} -> index.html")
            break
    else:
        print("   ❌ 找不到 HTML 文件")
        utils.set_state(success=False, error="找不到源文件")
        exit(1)
# Git 操作
print("\n📋 步骤4：推送到 GitHub...")
os.chdir(deploy_dir)
# 初始化或清理
if os.path.exists('.git'):
    shutil.rmtree('.git')
subprocess.run(['git', 'init'], capture_output=True)
subprocess.run(['git', 'add', '.'], capture_output=True)
subprocess.run(['git', 'commit', '-m', '🎉 汪汪队英语乐园首次部署'], capture_output=True)
# 设置远程
repo_url = f"https://github.com/{github_username}/{repo_name}.git"
subprocess.run(['git', 'remote', 'add', 'origin', repo_url], capture_output=True)
subprocess.run(['git', 'branch', '-M', 'main'], capture_output=True)
# 推送
result = subprocess.run(['git', 'push', '-u', 'origin', 'main', '--force'], 
                       capture_output=True, text=True)
if result.returncode == 0:
    print("   ✅ 代码推送成功！")
else:
    print(f"   ⚠️ 推送信息：{result.stderr}")
# 启用 GitHub Pages
print("\n📋 步骤5：配置 GitHub Pages...")
result = subprocess.run([
    'gh', 'api',
    f'repos/{github_username}/{repo_name}/pages',
    '-X', 'POST',
    '-f', 'source[branch]=main',
    '-f', 'source[path]=/'
], capture_output=True, text=True)
if result.returncode == 0 or 'already' in result.stderr.lower():
    print("   ✅ GitHub Pages 已启用！")
else:
    print(f"   ⚠️ Pages 配置：{result.stderr}")
    print("   可能需要手动在 GitHub 仓库设置中启用 Pages")
# 完成
print("\n" + "=" * 60)
print("🎉 部署成功完成！")
print("=" * 60)
website_url = f"https://{github_username}.github.io/{repo_name}/"
repo_url = f"https://github.com/{github_username}/{repo_name}"
print(f"\n🌐 游戏访问地址：")
print(f"   {website_url}")
print(f"\n📱 手机使用方法：")
print(f"   1. 在手机浏览器打开上面的网址")
print(f"   2. 可以添加到主屏幕，像 App 一样使用")
print(f"\n🔗 代码仓库：")
print(f"   {repo_url}")
print(f"\n⏰ 提示：GitHub Pages 生效需要 1-3 分钟")
print(f"   如果暂时打不开，请稍等再试")
print("=" * 60)
# 清理
os.chdir("/Users/btt/aipywork/CXEbTdw7Fvi2jCCYdUs9c/CZMUn4piLZVxKt55xCPUd")
shutil.rmtree(deploy_dir, ignore_errors=True)
utils.set_state(
    success=True,
    url=website_url,
    repo=repo_url,
    username=github_username
)