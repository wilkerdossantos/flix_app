# FlixApp

FlixApp é um frontend escrito em Python usando a biblioteca Streamlit. O projeto segue a abordagem de Domain-Driven Design (DDD), implementando os padrões Service e Repository. O FlixApp consome dados da **FlixApi**, um backend responsável por fornecer informações sobre filmes e séries.

## Tecnologias Utilizadas

- **Python**: Linguagem principal do projeto.
- **Streamlit**: Framework para desenvolvimento de aplicações web interativas.
- **DDD (Domain-Driven Design)**: Estruturação baseada em domínios de negócio.
- **Padrão Service e Repository**: Para separação de responsabilidades e melhor organização do código.
- **FlixApi**: API que fornece os dados consumidos pelo frontend.

## Estrutura do Projeto

```
flix_app/
|-- app.py                  # Ponto de entrada da aplicação Streamlit
|-- requirements.txt        # Dependências do projeto
|-- actors/                 # Módulo de atores
|   |-- __init__.py         # Inicializador do módulo
|   |-- page.py             # Página de exibição de atores
|   |-- repository.py       # Repositório para acesso a dados de atores
|   |-- service.py          # Regras de negócio para atores
|-- genres/                 # Módulo de gêneros
|   |-- __init__.py         # Inicializador do módulo
|   |-- page.py             # Página de exibição de gêneros
|   |-- repository.py       # Repositório para acesso a dados de gêneros
|   |-- service.py          # Regras de negócio para gêneros
|-- movies/                 # Módulo de filmes
|   |-- __init__.py         # Inicializador do módulo
|   |-- page.py             # Página de exibição de filmes
|   |-- repository.py       # Repositório para acesso a dados de filmes
|   |-- service.py          # Regras de negócio para filmes
|-- reviews/                # Módulo de avaliações
|   |-- __init__.py         # Inicializador do módulo
|   |-- page.py             # Página de exibição de avaliações
|   |-- repository.py       # Repositório para acesso a dados de avaliações
|   |-- service.py          # Regras de negócio para avaliações
|-- home/                   # Módulo da página inicial
|   |-- __init__.py         # Inicializador do módulo
|   |-- page.py             # Página principal
|-- login/                  # Módulo de autenticação
|   |-- __init__.py         # Inicializador do módulo
|   |-- page.py             # Página de login
|   |-- service.py          # Regras de autenticação
|-- api/                    # Módulo para comunicação com APIs externas
|   |-- __init__.py         # Inicializador do módulo
|   |-- service.py          # Serviço para requisições à API
```

## Instalação e Execução

### 1. Clone o repositório

```sh
git clone https://github.com/wilkerdossantos/flix_app.git
cd flix_app
```

### 2. Crie um ambiente virtual e instale as dependências

```sh
python -m venv venv
source venv/bin/activate  # Linux/macOS
venv\Scripts\activate     # Windows
pip install -r requirements.txt
```

### 3. Execute o FlixApp

```sh
streamlit run app.py
```

## Configuração da FlixApi

Certifique-se de que a **FlixApi** esteja rodando corretamente e configurada no repositório para que o frontend consiga consumir os dados.

## Contribuição

1. Faça um fork do repositório.
2. Crie uma branch (`feature/nova-funcionalidade`).
3. Faça commit das suas alterações.
4. Envie um pull request.

## Licença

Este projeto está sob a licença MIT. Veja o arquivo [LICENSE](LICENSE) para mais detalhes.

---

Feito com ❤️ por [Wilker dos Santos](https://github.com/wilkerdossantos)
