from langchain_community.document_loaders import WebBaseLoader
from langchain_community.document_loaders import YoutubeLoader
from langchain_community.document_loaders import PyPDFLoader
from langchain.prompts import ChatPromptTemplate
from langchain_groq import ChatGroq
import os

api_key = 'SUA_CHAVE_AQUI'
os.environ['GROQ_API_KEY'] = api_key

chat = ChatGroq(model='llama-3.1-70b-versatile')

def resposta_bot(mensagens, documento):
  mensagem_sistema = '''
  Você é um assistente intelectualmente habilidoso chamado GenAILite.
  Você utiliza as seguintes informações para formular suas respostas: 
  {informacoes}
  '''
  mensagens_modelo = [('system', mensagem_sistema)]
  mensagens_modelo += mensagens
  template = ChatPromptTemplate.from_messages(mensagens_modelo)
  chain = template | chat
  return chain.invoke({'informacoes' : documento}).content


def carregar_site():
  url_site = input('Insira a url do site: ')
  loader_site = WebBaseLoader(url_site)
  lista_documentos_site = loader_site.load()

  documento_site = ''
  for doc_site in lista_documentos_site:
    documento_site += doc_site.page_content

  return documento_site

def carregar_youtube():
  url_youtube = input('Insira a url do vídeo: ')
  loader_youtube = YoutubeLoader.from_youtube_url(
      url_youtube,
      language=['pt']
  )

  lista_documentos_youtube = loader_youtube.load()

  documento_youtube = ''
  for doc_youtube in lista_documentos_youtube:
    documento_youtube += doc_youtube.page_content

  return documento_youtube

def carregar_pdf():
  caminho = input('Insira o caminho do arquivo pdf: ')
  loader_pdf = PyPDFLoader(caminho)
  lista_documentos_pdf = loader_pdf.load()

  documento_pdf = ''
  for doc_pdf in lista_documentos_pdf:
    documento_pdf += doc_pdf.page_content

  return documento_pdf

print('Bem vindo ao GenAILite!')

texto_selecao = '''
Digite:
1 - para conversar com o site
2 - para conversar com o pdf
3 - para conversar com o youtube
0 - SAIR
'''
selecao = input(texto_selecao)

while True:
  if selecao == '1':
    documento = carregar_site()
    break
  elif selecao == '2':
    documento = carregar_pdf()
    break
  elif selecao == '3':
    documento = carregar_youtube()
    break

  elif selecao == '0':
    print('Até mais!')
    break

  else:
    print('Opção inválida!')

mensagens = []

while True:
  pergunta = input('Usuário: ')
  if pergunta.lower() == 'x':
    break
  mensagens.append(('user', pergunta))
  resposta = resposta_bot(mensagens, documento)
  mensagens.append(('assistant', resposta))
  print(f'Bot: {resposta}')

print('Muito obrigado por usar o GenAILite!')
print(mensagens)