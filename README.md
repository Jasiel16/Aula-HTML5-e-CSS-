# Aula-HTML5-e-CSS-

Aula como usar HTML5 e CSS#

## Chatbot com Groq

O arquivo `groq_chatbot.py` demonstra como usar a API da Groq para criar
um chatbot simples em linha de comando. Uma mensagem de sistema define
que o bot se comporte como um assistente bastante inteligente e fornece
respostas concisas. Para rodar o exemplo você
precisa de Python 3 e instalar a dependência `requests`:

```bash
pip install -r requirements.txt
```

Defina a chave da API em uma variável de ambiente chamada
`GROQ_API_KEY` e execute o script:

```bash
export GROQ_API_KEY="sua-chave-aqui"
python groq_chatbot.py
```

Digite suas mensagens e o chatbot responderá usando a API da Groq.
Digite `sair` para encerrar o diálogo.
