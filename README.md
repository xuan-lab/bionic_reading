# Bionic Reading 

## 项目简介

Bionic Reading 是一种新颖的阅读方法，通过在文本中设置人工固定点来引导眼睛的移动，从而提高阅读效率。本项目利用 OLLAMA 大模型（Gemma:7B）智能识别关键词，并加粗这些关键词，以帮助用户更好地理解和记忆文本内容。

## 功能

- **关键词识别**：自动识别文本中的重要关键词。
- **文本加粗**：将识别出的关键词加粗，提高阅读体验。
- **文件读写**：支持从文件读取输入文本，并将处理后的结果写入输出文件。

## 技术栈

- **Python 3.x**：程序开发语言。
- **OLLAMA**：用于运行大语言模型的工具。
- **requests**：用于处理 HTTP 请求（如果未来需要与外部服务交互）。

## 环境要求

- Python 3.7 及以上版本。
- OLLAMA 已安装并配置好，支持 Gemma:7B 模型。

## 安装步骤

1. **克隆或下载本项目**：

   ```bash
   git clone https://github.com/yourusername/bionic_reading.git
   cd bionic_reading
   ```

2. **安装依赖**：

   在项目目录中，使用以下命令安装所需的 Python 库：

   ```bash
   pip install -r requirements.txt
   ```

3. **准备输入文本**：

   在 `input` 文件夹中，您可以修改或添加 `sample_text.txt` 文件，输入您希望处理的文本。

## 使用方法

1. **运行主程序**：

   在终端中运行以下命令：

   ```bash
   python main.py
   ```

2. **查看结果**：

   处理完成后，结果将保存在 `output/highlighted_text.html` 文件中。您可以使用浏览器打开该文件，查看加粗后的文本内容。

## 代码结构

```
bionic_reading/
│
├── main.py                   # 主程序文件
├── requirements.txt          # 项目依赖文件
├── README.md                 # 项目说明文档
├── input/                    # 输入文本文件夹
│   └── sample_text.txt       # 示例文本文件
└── output/                   # 输出文件夹
    └── highlighted_text.html  # 处理后的结果文件
```

## 注意事项

- 请确保您的环境中已正确安装并配置 OLLAMA，并且能够成功运行 Gemma:7B 模型。
- 模型返回的关键词格式可能会影响代码，请根据实际情况调整 `main.py` 中的相关逻辑。
- 在处理较大文本时，可能需要更改一些模型参数以提高性能。

## 贡献

欢迎任何形式的贡献！如果您有建议或问题，请提出 Issue 或者提交 Pull Request。我们鼓励社区成员参与项目的改进。

## 联系方式

如有任何问题或建议，请通过以下方式联系我：

- 邮箱: [xiexuan@kernel-dev.com](mailto:xiexuan@kernel-dev.com)

## 许可证

本项目使用 MIT 许可证，详细信息请参见 LICENSE 文件。