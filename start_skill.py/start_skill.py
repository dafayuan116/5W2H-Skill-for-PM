import os

def run_skill():
    print("\n" + "="*40)
    print("🚀 5W2H 心理学增强需求定义引擎 v1.0")
    print("="*40)
    
    prompt_path = "5w2h-core-engine.md"
    
    if os.path.exists(prompt_path):
        print("✅ 心理学逻辑引擎加载成功！")
    else:
        print("⚠️ 提醒：请确保 5w2h-core-engine.md 在同目录下。")

    print("\n[使用指南]：")
    print("请输入你的初始想法，我将为你准备引导策略。")
    print("-" * 40)

    idea = input("💡 你的原始想法是什么？\n> ")
    
    print(f"\n[处理中...] 已针对“{idea}”准备好 5W2H 追问逻辑。")
    print("✨ 请前往 GitHub 复制完整 Prompt 开启对话！")
    print("-" * 40 + "\n")

if __name__ == "__main__":
    run_skill()