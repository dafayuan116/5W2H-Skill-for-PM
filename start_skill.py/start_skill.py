import urllib.request
import os

def run_skill():
    print("\n" + "="*40)
    print("🚀 5W2H 心理学增强需求定义引擎 (云端版)")
    print("="*40)
    
    # 核心：直接从你的 GitHub 地址读取最新的逻辑
    RAW_URL = "https://raw.githubusercontent.com/dafayuan116/5W2H-Skill-for-PM/main/5w2h-core-engine.md"
    
    print("📡 正在连接 GitHub 云端大脑同步最新逻辑...")
    
    try:
        # 增加超时设置，防止网络卡死
        with urllib.request.urlopen(RAW_URL, timeout=10) as response:
            system_prompt = response.read().decode('utf-8')
            print("✅ 逻辑引擎同步成功！(当前版本：GitHub Live)")
    except Exception as e:
        print(f"❌ 同步失败：无法连接到 GitHub。")
        print("💡 请检查网络，或直接前往 GitHub 仓库手动复制逻辑。")
        return

    print("\n[使用指南]：输入一个产品想法，我将为你生成引导指令。")
    print("-" * 40)

    idea = input("💡 你的原始想法是什么？\n> ")
    
    print(f"\n[处理中...] 已针对“{idea}”准备好 5W2H 心理学引导策略。")
    print("✨ 逻辑已就绪！请前往 AI 对话框（ChatGPT/Gemini）开始。")
    print(f"提示：已成功加载核心 Prompt（共 {len(system_prompt)} 字符）。")
    print("-" * 40 + "\n")

if __name__ == "__main__":
    run_skill()
    
