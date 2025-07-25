# consulta-notas-selenium 🧑‍💻

Um bot simples em Python que automatiza o login no SIGAA e realiza a consulta de notas do usuário. Criado com a biblioteca [Selenium](https://selenium-python.readthedocs.io/) como forma de aprendizado e prática.

## 🚀 Sobre o Projeto

Este projeto automatiza o processo de:

1. Acessar o site do SIGAA.
2. Realizar login com suas credenciais.
3. Navegar até a aba de "Consultar Minhas Notas".

> ⚠️ Este projeto foi feito apenas para fins educacionais e **não deve ser utilizado para automatizar ações maliciosas ou em larga escala em plataformas institucionais**.

## 🔧 Instalação

1 - Clone o repositório e instale as dependências:

```bash
git clone https://github.com/seu-usuario/consulta-notas-selenium.git
cd consulta-notas-selenium
pip install -r requirements.txt
```
2 - Crie um arquivo `.env` com as seguintes variáveis:
```
USER=seu_usuario
PASSWORD=sua_senha 
```
> ⚠️ **Não compartilhe** o arquivo `.env`! Adicione-o ao seu `.gitignore` para proteger seus dados.

## ▶️ Como usar 
Basta executar o script:
```
python main.py
```