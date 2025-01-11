# 📸 **LLM LLaVA - Image to Text with LLaVA Model** 🤖

Transforme uma **imagem** em **texto** com o poder do modelo **LLaVA**! Este projeto permite enviar imagens para o modelo LLaVA, obter descrições detalhadas e fazer perguntas sobre o conteúdo da imagem. Perfeito para análises visuais avançadas! 🌟

## ⚡ **Funcionalidade** 🚀
Este projeto permite que você envie imagens para um modelo de linguagem visual (LLaVA) que analisa o conteúdo das imagens e responde a perguntas com base no que ele "vê"! 🖼️➡️💬

### Como funciona:
1. Carregue uma imagem 🖼️.
2. Digite uma pergunta sobre o conteúdo da imagem 🤔.
3. O modelo LLaVA analisa a imagem e retorna uma resposta detalhada! 💡

## 💻 **Tecnologias utilizadas**:
- **Streamlit**: Para a interface web simples e interativa 🌍.
- **Requests**: Para enviar a imagem para a API do LLaVA 💻.
- **Base64**: Para codificar a imagem antes de enviá-la 📥.

## 📦 **Instalação** 🔧

### 1️⃣ **Clone o repositório**:
```bash
git clone https://github.com/thaleson/LLMLLAVA.git
cd LLMLLAVA
```

### 2️⃣ **Crie e ative um ambiente virtual**:
**Para Linux/Mac**:
```bash
python3 -m venv .venv
source .venv/bin/activate
```

**Para Windows**:
```bash
python -m venv .venv
.\.venv\Scripts\activate
```

### 3️⃣ **Instale as dependências**:
```bash
pip install -r requirements.txt
```

## 🚀 **Configuração do Servidor Ollama** 🖥️

Este projeto depende do servidor **Ollama** para funcionar corretamente. Antes de executar o aplicativo, você precisa **baixar e executar o servidor Ollama** com o modelo LLaVA.

### 🌍 **Baixando o servidor Ollama e o modelo LLaVA**:

- **Ollama** é necessário para rodar o modelo **LLaVA**. Siga as instruções abaixo para instalá-lo no seu sistema.

### **Instruções para diferentes sistemas operacionais:**

#### 🐧 **Para Linux**:
1. Baixe e instale o **Ollama** com o seguinte comando:
   ```bash
   curl -sSL https://ollama.com/download/ollama-linux -o ollama.tar.gz
   tar -xvzf ollama.tar.gz
   sudo mv ollama /usr/local/bin/ollama
   ```
2. Baixe o modelo LLaVA com o comando:
   ```bash
   ollama pull llava
   ```
3. Inicie o servidor Ollama:
   ```bash
   ollama start
   ```

#### 🖥️ **Para Windows**:
1. Baixe o instalador do **Ollama** no [site oficial do Ollama](https://ollama.com/download).
2. Após a instalação, abra o Prompt de Comando ou PowerShell e execute:
   ```bash
   ollama pull llava
   ```
3. Inicie o servidor Ollama:
   ```bash
   ollama start
   ```

#### 🍏 **Para Mac**:
1. Baixe e instale o **Ollama** via Homebrew:
   ```bash
   brew install ollama
   ```
2. Baixe o modelo LLaVA com o comando:
   ```bash
   ollama pull llava
   ```
3. Inicie o servidor Ollama:
   ```bash
   ollama start
   ```

**Observação**: Se o **Ollama** não estiver instalado corretamente, o projeto não funcionará até que o servidor esteja em execução com o modelo LLaVA.

## 🚀 **Iniciando o Projeto**:

### 1️⃣ **Execute o Streamlit**:
```bash
streamlit run app.py
```

Isso abrirá o seu navegador padrão com a interface do Streamlit para você começar a usar o modelo LLaVA! 🌐

## 📝 **Como usar**:

1. **Envie uma imagem** usando o botão de upload de arquivos 📤.
2. **Digite sua pergunta** sobre o conteúdo da imagem no campo de texto 📝.
3. Clique no botão "Fazer Pergunta sobre a Imagem" e aguarde a resposta do modelo LLaVA! 🕒

🔍 O modelo irá analisar a imagem e gerar uma descrição detalhada, além de tentar responder à sua pergunta sobre o que está na imagem!

## 💡 **Exemplo de Uso**:

1. Carregue uma foto de um cachorro 🐕.
2. Pergunte: "What breed is this dog?" 🐾
3. O modelo vai analisar a imagem e fornecer uma resposta com base naquilo que "vê" na foto!

## 🌍 **Instruções para Diferentes Sistemas Operacionais**:

### **Para Linux** 💻:
1. Abra o terminal.
2. Siga os passos de instalação e execução descritos acima.
3. Se você não tem o `python3` ou o `pip`, instale-os primeiro com o comando `sudo apt-get install python3 python3-pip`.

### **Para Windows** 🖥️:
1. Abra o PowerShell ou Prompt de Comando.
2. Siga os passos de instalação e execução descritos acima.
3. Certifique-se de que o `python` e `pip` estão instalados. Caso contrário, baixe do [site oficial do Python](https://www.python.org/downloads/).

### **Para Mac** 🍏:
1. Abra o terminal.
2. Instale o Python se não tiver já instalado usando o Homebrew:
   ```bash
   brew install python
   ```
3. Siga os passos de instalação e execução descritos acima.

## 🛠️ **Recursos adicionais**:

- 🐍 **Python 3.x**.
- 💻 **Streamlit** para criar interfaces interativas.
- 🖼️ O modelo LLaVA foi integrado para fornecer respostas precisas sobre o conteúdo das imagens.

## 💬 **Contribuindo** 🤝

1. Fork o repositório 🍴.
2. Crie uma nova branch 🛠️ (`git checkout -b feature-nome-da-feature`).
3. Faça suas alterações e commit 📝.
4. Envie suas mudanças para o repositório remoto 🔄 (`git push origin feature-nome-da-feature`).
5. Abra um Pull Request no GitHub 🔀.



🎉 **Aproveite o poder do LLaVA para transformar imagens em texto e muito mais!** 🎉
```

