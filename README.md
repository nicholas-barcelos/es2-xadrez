# Projeto de Engenharia de Software 2
## Jogo de Xadrez com Inteligência Artificial

# Arquitetura
- Linguagem de Programação: Python 3.6
- Framework a ser utilizado: Pygame 1.9.3
- Será utilizado o módulo de ambientes virtuais `virtualenv`

## Padrões de organização de código
- Indentação será feita com quatro espaços por marca de indentação.
- Nomes de variáveis e funções serão grafados em `camelCase`.
- Nomes de variáveis/funções/whatever serão todos em PORTUGUÊS.
- Deve-se evitar deixar as linhas de código muito grandes sempre que possível.

## Dependências
- Pygame 
- Pyinstaller [para criar o executável]

### Como instalar as dependências
`pip install pygame pyinstaller`

## Como rodar
 Com as dependências instaladas e dentro do seu ambiente virtual, rode
 `python game.py`
 
### Criando o executável
 `pyinstaller --onefile game.py`
 O executável será posto na pasta `dist`, e para executá-lo [LINUX]:
 `./game`
 Nota: É necessário copiar a pasta `assets` e colocá-la na mesma pasta onde irá se executar o jogo.