mlops_deploy
==============================

Criação de uma API utilizando Flask para utilizar Modelos de Machine Learning criados || 
Aqui você vai poder visualizar:

Como criar novos endpoints, 
Como fazer análise de sentimento usando TextBlob, 
Criar um endpoint com uma análise de sentimento, 
Treinar um modelo com a base House Pricing, 
Como colocar um modelo de machine learning em uma API, 
Como criar um endpoint para receber chamadas POST, 
Como fazer uma chamada POST, 
Como gravar um modelo em um arquivo, 
Como proteger um endpoint com login e senha, 
Como fazer uma chamada HTTP com uma autenticação básica, 
Como usar o Requests para consumir API’s.

Project Organization
------------
    ├── LICENSE
    ├── Makefile           <- Makefile com comandos como `make data` ou `make train`
    ├── README.md          <- O README de nível superior para desenvolvedores que usam este projeto.
    ├── data
    │   ├── external       <- Dados de fontes de terceiros.
    │   ├── interim        <- Dados intermediários que foram transformados.
    │   ├── processed      <- Conjuntos de dados finais, canônicos, para modelagem.
    │   └── raw            <- O dump de dados original e imutável.
    │
    ├── docs               <- Um projeto padrão do Sphinx; veja sphinx-doc.org para detalhes
    │
    ├── models             <- Modelos treinados e serializados, modelos (Sentimento " Para análise de sentimento" e Cotacao "Para análise de preço das casas") 
    │                         Foi convertido em sav, utilizando a biblíoteca Pickle para o código main da API não ficar tão extenso.
    │
    ├── notebooks          <- Notebooks Jupyter. 
    │
    ├── references         <- Dicionários de dados, manuais e todos os outros materiais explicativos.
    │
    ├── reports            <- Análises geradas como HTML, PDF, LaTeX, etc.
    │   └── figures        <- Gráficos e figuras gerados para serem usados nos relatórios
    │
    ├── requirements.txt   <- O arquivo de requisitos para reproduzir o ambiente de análise, por exemplo,
    │                         gerado com `pip freeze > requirements.txt`
    │
    ├── setup.py           <- Torna o projeto instalável via pip (pip install -e .) para que o src possa ser importado
    ├── src                <- Código-fonte para uso neste projeto
    │   ├── App            <- Pasta com os códigos da aplicação
        └── main.py        <- código main da API para rodar
    │   ├── __init__.py    <- Torna src um módulo Python
    │   │
    │   ├── data           <- Scripts para baixar ou gerar dados
    │   │   └── make_dataset.py
    │   │
    │   ├── features       <- Scripts para transformar dados brutos em recursos para modelagem
    │   │   └── build_features.py
    │   │
    │   ├── models         <- Scripts para treinar modelos e depois usar modelos treinados para fazer
    │   │   │                 previsões
    │   │   ├── model.sav
    │   │   
    │   │
    │   └── visualization  <- Scripts para criar visualizações exploratórias e orientadas a resultados
    │       └── visualize.py
    │
    └── tox.ini            <- Arquivo tox com configurações para executar tox; veja tox.readthedocs.io



--------

<p><small>Project based on the <a target="_blank" href="https://drivendata.github.io/cookiecutter-data-science/">cookiecutter data science project template</a>. #cookiecutterdatascience</small></p>
