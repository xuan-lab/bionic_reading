import subprocess
import json
import re
import os

def call_ollama_model(text):
    """调用 OLLAMA 模型以获取关键词"""
    result = subprocess.run(['ollama', 'run', 'gemma:7b', text],
                            capture_output=True, text=True)
    if result.returncode != 0:
        raise Exception("调用 OLLAMA 模型失败: " + result.stderr)
    return json.loads(result.stdout)  # 假设模型返回的是一个 JSON 格式的关键词列表

def emphasize_words(text, keywords):
    """加粗文本中的关键词"""
    word_pattern = re.compile(r"(\w+)")
    
    def emphasize_word(word):
        if word.lower() in keywords:
            return f"<strong>{word}</strong>"
        return word

    # 替换文本中的单词
    emphasized_text = word_pattern.sub(lambda match: emphasize_word(match.group(0)), text)
    return emphasized_text

def main():
    # 确保输出目录存在
    output_dir = 'output'
    os.makedirs(output_dir, exist_ok=True)

    # 读取输入文本文件
    input_file_path = 'input/sample_text.txt'
    with open(input_file_path, 'r', encoding='utf-8') as file:
        sample_text = file.read()

    # 调用模型获取关键词
    keywords = call_ollama_model(sample_text)

    # 强调关键词
    highlighted_text = emphasize_words(sample_text, keywords)

    # 输出结果到 HTML 文件
    output_file_path = os.path.join(output_dir, 'highlighted_text.html')
    with open(output_file_path, 'w', encoding='utf-8') as output_file:
        output_file.write(highlighted_text)

    print(f"处理完成，结果已保存到 {output_file_path}")

if __name__ == "__main__":
    main()
