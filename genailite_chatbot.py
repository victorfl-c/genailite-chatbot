# Importação de módulos necessários para carregar documentos e estruturar o chatbot
from langchain_community.document_loaders import WebBaseLoader  # Carrega conteúdo de sites
from langchain_community.document_loaders import YoutubeLoader  # Carrega legendas de vídeos do YouTube
from langchain_community.document_loaders import PyPDFLoader    # Carrega texto de arquivos PDF
from langchain.prompts import ChatPromptTemplate                # Cria um template de prompts de chat
from langchain_groq import ChatGroq                             # Conecta com o modelo de linguagem Groq para gerar respostas
import os                                                      # Módulo para definir variáveis de ambiente

# Definindo a chave da API para o serviço de IA, que será usada para autenticar o acesso ao modelo
api_key = 'SUA_CHAVE_AQUI'
os.environ['GROQ_API_KEY'] = api_key                           # Armazena a chave como variável de ambiente

# Inicializando o modelo de linguagem usando ChatGroq com um modelo de grande capacidade
chat = ChatGroq(model='llama-3.1-70b-versatile')

# Função para obter uma resposta do chatbot baseada nas mensagens do usuário e no documento fornecido
def resposta_bot(mensagens, documento):
  # Definindo a mensagem inicial do sistema que descreve o comportamento do assistente
  mensagem_sistema = '''
  Você é um assistente intelectualmente habilidoso chamado GenAILite.
  Você utiliza as seguintes informações para formular suas respostas: 
  {informacoes}
  '''
  
  # Inicializa a conversa com uma mensagem do sistema explicando o propósito do assistente
  mensagens_modelo = [('system', mensagem_sistema)]
  mensagens_modelo += mensagens  # Adiciona as mensagens do usuário e respostas do assistente
  
  # Cria um template de prompt usando as mensagens modeladas para estruturar a entrada do chatbot
  template = ChatPromptTemplate.from_messages(mensagens_modelo)
  
  # Executa a cadeia de mensagens no modelo, permitindo que o chatbot use o documento como referência
  chain = template | chat
  return chain.invoke({'informacoes' : documento}).content  # Retorna o conteúdo da resposta do modelo

# Funções para carregar diferentes tipos de documentos. Estas funções permitem ao usuário fornecer dados
# que o chatbot usará para responder com contexto específico.

# Carrega o conteúdo de um site a partir de uma URL fornecida pelo usuário
def carregar_site():
  url_site = input('Insira a url do site: ')               # Pede a URL ao usuário
  loader_site = WebBaseLoader(url_site)                    # Inicializa o loader para sites
  lista_documentos_site = loader_site.load()               # Carrega o conteúdo do site como lista de documentos
  
  documento_site = ''                                      # Inicializa uma string para armazenar o conteúdo do site
  for doc_site in lista_documentos_site:                   # Concatena o conteúdo de cada página carregada
    documento_site += doc_site.page_content

  return documento_site                                    # Retorna o conteúdo como uma única string

# Carrega o conteúdo de legendas de um vídeo do YouTube usando a URL fornecida
def carregar_youtube():
  url_youtube = input('Insira a url do vídeo: ')           # Pede a URL do vídeo ao usuário
  loader_youtube = YoutubeLoader.from_youtube_url(
      url_youtube,
      language=['pt']                                      # Define o idioma da legenda como português
  )
  
  lista_documentos_youtube = loader_youtube.load()         # Carrega o conteúdo do vídeo como lista de documentos
  
  documento_youtube = ''                                   # Inicializa uma string para armazenar o conteúdo das legendas
  for doc_youtube in lista_documentos_youtube:             # Concatena o conteúdo de cada parte carregada das legendas
    documento_youtube += doc_youtube.page_content

  return documento_youtube                                 # Retorna o conteúdo como uma única string

# Carrega o conteúdo de um arquivo PDF a partir do caminho do arquivo fornecido
def carregar_pdf():
  caminho = input('Insira o caminho do arquivo pdf: ')     # Pede o caminho do arquivo PDF ao usuário
  loader_pdf = PyPDFLoader(caminho)                        # Inicializa o loader para arquivos PDF
  lista_documentos_pdf = loader_pdf.load()                 # Carrega o conteúdo do PDF como lista de documentos
  
  documento_pdf = ''                                       # Inicializa uma string para armazenar o conteúdo do PDF
  for doc_pdf in lista_documentos_pdf:                     # Concatena o conteúdo de cada página carregada do PDF
    documento_pdf += doc_pdf.page_content

  return documento_pdf                                     # Retorna o conteúdo como uma única string

# Exibe um menu de seleção para o usuário escolher o tipo de documento que deseja carregar
print('Bem vindo ao GenAILite!')

# Exibe as opções para o usuário e espera uma escolha
texto_selecao = '''
Digite:
1 - para conversar com o site
2 - para conversar com o pdf
3 - para conversar com o youtube
0 - SAIR
'''
selecao = input(f'{texto_selecao}\nUsuário:')

# Loop para escolher o tipo de documento e chamá-lo. Cada opção chama a função correspondente.
while True:
  if selecao == '1':
    documento = carregar_site()                            # Chama função para carregar conteúdo de um site
    break

  elif selecao == '2':
    documento = carregar_pdf()                             # Chama função para carregar conteúdo de um PDF
    break

  elif selecao == '3':
    documento = carregar_youtube()                         # Chama função para carregar conteúdo de um vídeo do YouTube
    break

  elif selecao == '0':
    print('Até mais!')                                     # Mensagem de despedida ao escolher sair
    break

  else:
    print('Opção inválida!')                               # Exibe uma mensagem se a entrada for inválida

# Inicializa uma lista de mensagens para armazenar o histórico da conversa
mensagens = []

# Loop de interação com o usuário para conversar com o chatbot até o usuário digitar 'x'
while True:
  pergunta = input('Usuário: ')                           # Recebe uma pergunta do usuário
  if pergunta.lower() == 'x':                             # Termina o loop se o usuário digitar 'x'
    break
  mensagens.append(('user', pergunta))                    # Adiciona a pergunta do usuário à lista de mensagens
  
  resposta = resposta_bot(mensagens, documento)           # Gera uma resposta do bot usando a função resposta_bot
  mensagens.append(('assistant', resposta))               # Adiciona a resposta do bot à lista de mensagens
  
  print(f'Bot: {resposta}')                               # Exibe a resposta do bot

# Exibe uma mensagem final e imprime todo o histórico da conversa
print('Muito obrigado por usar o GenAILite!')
print(mensagens)                                          # Imprime a lista de mensagens para revisão e log
