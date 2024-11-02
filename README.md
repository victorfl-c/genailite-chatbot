# GenAILite Chatbot
**GenAILite** é um chatbot interativo desenvolvido para responder a perguntas do usuário com base em informações retiradas de fontes externas, como sites, vídeos do YouTube e arquivos PDF. O chatbot utiliza um modelo de linguagem grande, llama-3.1-70b-versatile, para processar perguntas e respostas, oferecendo interações personalizadas e relevantes para o usuário.

## Recursos Principais
- **Interação Dinâmica:** Responde a perguntas com base em um documento específico carregado pelo usuário.
- **Suporte a Diferentes Fontes de Dados:** Pode extrair conteúdo de sites, vídeos do YouTube e PDFs.
- **Flexível e Extensível:** Integrado com o LangChain, o que permite a expansão para outras fontes e fluxos de trabalho de IA.

### Sumário
- [Instalação](https://github.com/victorfl-c/genailite-chatbot/edit/main/README.md#instala%C3%A7%C3%A3o)
- [Configuração](Configuração)
- [Como Usar](ComoUsar)
- [Estrutura do Código](Estrutura_do_codigo)
- [Contribuição](contribuição)
- [Licença](licença)

## Instalação

1. Clone o repositório

```bash
git clone https://github.com/seu_usuario/genailite-chatbot.git
cd genailite-chatbot
```

2. Crie e ative um ambiente virtual (opcional, mas recomendado):

```bash
python3 -m venv venv
source venv/bin/activate  # Linux/MacOS
venv\Scripts\activate     # Windows
```
3. Instale as dependências:

```bash
pip install -r requirements.txt
```
## Configuração
Este chatbot requer uma chave de API para acessar o modelo **llama-3.1-70b-versatile**. Configure a chave de API antes de iniciar.
Note que estamos utilizando especificamente a [GROQ Cloud](https://console.groq.com/playground).
Crie uma conta e vá para a aba "API Keys" e, em seguida clique em "Create Api Key"

1. No código, defina a chave da API para autenticação:

```bash
api_key = 'SUA_CHAVE_API'
os.environ['GROQ_API_KEY'] = api_key
```
2. Salve a chave em um arquivo **.env** ou como uma variável de ambiente para segurança:

```bash
export GROQ_API_KEY="SUA_CHAVE_API"
```

## Como Usar

1. **Execute o Script**

```bash
python genailite_chatbot.py
```

2. **Escolha a fonte de dados**

  - Ao iniciar, o GenAILite pedirá que você escolha entre carregar um site, um arquivo PDF ou um vídeo do YouTube para análise e resposta.

3. **Interaja com o Chatbot**

  - Após selecionar a fonte, o chatbot estará pronto para responder às suas perguntas com base no conteúdo carregado.
  - Digite **x** para encerrar a interação.

4. **Salvar o Histórico de Conversa:**

  - Ao final da execução, todo o histórico de perguntas e respostas é impresso para possível análise.

## Estrutura do código
O script **(genailite_chatbot.py)** está organizado da seguinte forma:

- Funções de Carregamento:

  - carregar_site(): Carrega conteúdo de um site a partir de uma URL.
  - carregar_youtube(): Extrai legendas de um vídeo do YouTube.
  - carregar_pdf(): Lê o conteúdo de um arquivo PDF.
  
- Função **resposta_bot():**

  - Configura e interage com o modelo llama-3.1-70b-versatile, formatando respostas com base nas mensagens enviadas pelo usuário.
    
- Interação com o Usuário:

  - O chatbot processa as perguntas e as responde até que o usuário opte por sair, mantendo um registro de toda a conversa.

## Dependências
Este projeto depende das seguintes bibliotecas:

- langchain_community
- langchain_groq
- os (embutido no Python)

Para instalar todas as dependências de uma só vez, execute:
```bash
pip install -r requirements.txt
```

## Contribuição
Contribuições são bem-vindas! Sinta-se à vontade para fazer um fork do projeto, criar uma branch com suas mudanças e abrir um pull request. Para problemas ou sugestões, abra uma issue.

## Como Contribuir
1. Faça um fork do projeto.
2. Crie uma nova branch para suas alterações **(git checkout -b minha-nova-feature)**.
3. Commit suas mudanças **(git commit -m 'Adiciona nova feature')**.
4. Envie para o branch principal **(git push origin minha-nova-feature)**.
5. Abra um Pull Request.

## Licença
Este projeto é licenciado sob a Licença MIT. Veja o arquivo [LICENSE](License) para mais detalhes.
