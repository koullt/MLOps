from flask import Flask, request, jsonify
from flask_basicauth import BasicAuth #autenticação de segurança basica
from textblob import TextBlob #biblioteca para analise de sentimento " aprendizado de máquina ja criado"
from googletrans import Translator #bibliote de tradução
from sklearn.linear_model import LinearRegression #aprendizado de maquina com regressão linear para predição
import numpy as np #biblioteca para formatação dos valores 
import pickle #para importar arquivos sav que foram exportados em pickle (serialização)
import os

modelo = pickle.load(open('../../models/modelo.sav','rb')) #subindo o modelo de maquina criado no jupyter notebook para esse ambiente.

js = ['tamanho', 'ano', 'garagem'] #definindo os 3 argumentos que o arquivo json precisa ter no endpoint de houses, para o aprendizado de maquina.


app = Flask(__name__) #criando a API com o flask
app.config['BASIC_AUTH_USERNAME'] = os.environ.get('BASIC_AUTH_USERNAME') #criando a auth
app.config['BASIC_AUTH_PASSWORD'] = os.environ.get('BASIC_AUTH_PASSWORD') #criando a auth

basic_auth = BasicAuth(app) #ativando a autenticação na API

#primeiro endpoint
@app.route('/') #cria a rota
def home(): #cria a função que vai executar o que vai ser passado quando acessar a rota
    return "Minha primeira API." #retorna o resultado.

#segundo endpoint
@app.route('/sentimento/<frase>') #rota
@basic_auth.required #para solicitar a autenticação
def sentimento(frase): #cria a função que vai executar o que vai ser passado quando acessar a rota
    tradutor = Translator() #função de tradução
    polaridade = None  # Inicialize a variável aqui

    try:
        traducao = tradutor.translate(frase, src='pt', dest='en').text #o textblob só trabalha com frases em ingles para fazer analise, por isso o tradutor pt > en
        
        tb_en = TextBlob(traducao) #vai pegar a frase traduzida e transformar em obj
        polaridade = tb_en.sentiment.polarity #faz a analise da frase com o aprendizado de maquina treinado.
        
    except Exception as e:
        print(f"Erro na tradução: {e}")
        
    return "polaridade: {}".format(polaridade) #retorna o resultado da analise

#terceiro endpoint
@app.route('/cotacao/', methods=['POST']) #metodo post criado para receber algo em json
@basic_auth.required
def cotacao():
    dados = request.get_json() #vai pegar os dados em json passado.
    
    try:
        # Extrair e garantir que todos os arguemntos necessários estão presentes
        dados_input = [dados[col] for col in js]
        dados_input = np.array(dados_input).reshape(1, -1)  # Converter para o formato correto
        
        # Prever o preço
        preco = modelo.predict(dados_input)
        
        return jsonify(preco=preco[0]) #retorna o resultado.
    
    except KeyError as e:
        return jsonify(erro=f"Chave ausente nos dados de entrada: {str(e)}"), 400 #validação de dados
    
    except Exception as e:
        return jsonify(erro=f"Erro na previsão: {str(e)}"), 500 #exception

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0') #rodar a aplicação, e toda vez que for atualizado vai reiniciar a aplicação com o debug.
