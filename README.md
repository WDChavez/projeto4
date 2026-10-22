[README.md](https://github.com/user-attachments/files/33843576/README.md)
# 🎬 API de Filmes

API REST desenvolvida com **Python**, **Django** e **Django REST Framework** para um projeto acadêmico de gerenciamento de filmes. O projeto utiliza **django-filter** e um banco de dados **SQLite**.

> **Status:** projeto acadêmico em desenvolvimento. Algumas funcionalidades e rotas podem estar em implementação.

## 🛠️ Tecnologias utilizadas

- Python
- Django 6.1.2
- Django REST Framework 3.18.3
- django-filter 26.2
- SQLite

## 📋 Requisitos

- Python compatível com a versão do Django indicada em `requirements.txt`
- Git
- pip

## 🚀 Como executar o projeto

### Windows (CMD)

```bat
git clone https://github.com/WDChavez/projeto4.git
cd projeto4
python -m venv venv
venv\Scripts\activate
python -m pip install -r requirements.txt
python manage.py migrate
python manage.py runserver
```

### Windows (PowerShell)

```powershell
git clone https://github.com/WDChavez/projeto4.git
cd projeto4
python -m venv venv
.\venv\Scripts\Activate.ps1
python -m pip install -r requirements.txt
python manage.py migrate
python manage.py runserver
```

### Linux / macOS

```bash
git clone https://github.com/WDChavez/projeto4.git
cd projeto4
python3 -m venv venv
source venv/bin/activate
python -m pip install -r requirements.txt
python manage.py migrate
python manage.py runserver
```

Depois, acesse `http://127.0.0.1:8000/` no navegador. O endereço exibido não garante que exista uma página inicial configurada; consulte as rotas do projeto.

## 🗃️ Banco de dados

O repositório contém o arquivo `db.sqlite3` e o conjunto de dados `base_filmes.csv`. O comando `python manage.py migrate` aplica as migrações configuradas.

### Importação de dados

O projeto também contém o script `importarDados.py`. Antes de executá-lo, confira seu funcionamento e se ele evita a duplicação de registros.

```bash
python importarDados.py
```

## 🔗 Endpoints

As rotas da API devem ser conferidas nos arquivos `urls.py` do projeto e do aplicativo `filmes`. Assim que forem verificadas, esta seção poderá incluir uma tabela com os caminhos e métodos HTTP disponíveis.

## 📁 Estrutura do repositório

```text
projeto4/
├── filmes/             # Aplicação Django
├── projeto4/           # Configurações do projeto Django
├── base_filmes.csv     # Dados de filmes
├── db.sqlite3          # Banco de dados SQLite
├── importarDados.py    # Script de importação
├── manage.py           # Utilitário de gerenciamento do Django
└── requirements.txt    # Dependências Python
```

## 👨‍💻 Autores

**Wanderson Chaves Alves**, 
**Daniel Paz Dos Passos**
GitHub: [@WDChavez](https://github.com/WDChavez)

---

*Projeto desenvolvido para fins de estudo e prática de desenvolvimento backend com Django.*
