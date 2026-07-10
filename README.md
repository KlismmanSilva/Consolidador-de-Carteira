# Consolidador de Carteira de Investimentos 📈

Um projeto Full-Stack focado no controlo e acompanhamento de ativos financeiros (ações e FIIs), desenvolvido com **FastAPI** (Backend), **React** (Frontend) e **SQLite**.

## 📋 Índice

- [Sobre o Projeto](#sobre-o-projeto)
- [Funcionalidades](#-funcionalidades)
- [Tecnologias](#-tecnologias)
- [Pré-requisitos](#pré-requisitos)
- [Instalação](#-instalação)
- [Uso](#-uso)
- [Estrutura do Projeto](#-estrutura-do-projeto)
- [Contribuição](#-contribuição)
- [Licença](#-licença)

## Sobre o Projeto

Este projeto permite gerir e monitorar sua carteira de investimentos de forma centralizada, oferecendo uma visão clara do seu patrimônio, lucros e prejuízos em tempo real.

## 🚀 Funcionalidades

- ✅ Registo e listagem de transações financeiras
- ✅ Banco de dados relacional para gerir Ativos e Compras
- ✅ Consulta de cotações em tempo real via `yfinance` (ex: ITSA4, BBSE3, TRXF11)
- ✅ Dashboard visual com cálculo automático de património, lucro e prejuízo

## 💻 Tecnologias

| Camada | Tecnologia | Versão |
|--------|-----------|--------|
| Backend | FastAPI | - |
| Frontend | React | - |
| Banco de Dados | SQLite | - |
| Cotações | yfinance | - |
| Python | 3.10+ | - |

## Pré-requisitos

- Python 3.10 ou superior
- Git configurado
- pip (gerenciador de pacotes Python)

## 📦 Instalação

### 1. Clonar o repositório

```bash
git clone https://github.com/SEU_USUARIO/consolidador-de-carteira.git
cd consolidador-de-carteira
```

### 2. Criar e ativar o Ambiente Virtual (venv)

**Windows:**
```bash
python -m venv venv
venv\Scripts\activate
```

**macOS/Linux:**
```bash
python -m venv venv
source venv/bin/activate
```

> 💡 Saberá que deu certo quando visualizar `(venv)` no início da linha do terminal.

### 3. Instalar as dependências

```bash
pip install -r requirements.txt
```

### 4. Executar o servidor

```bash
uvicorn main:app --reload
```

O servidor estará disponível em: **http://localhost:8000**

## 🎯 Uso

### Acessar a documentação da API

A documentação interativa automática da API está disponível em:

- **Swagger UI:** http://localhost:8000/docs
- **ReDoc:** http://localhost:8000/redoc

Aqui pode testar todas as rotas disponíveis.

## 📁 Estrutura do Projeto

```
consolidador-de-carteira/
├── main.py                 # Arquivo principal da aplicação FastAPI
├── requirements.txt        # Dependências do projeto
├── README.md              # Este arquivo
└── [Adicionar mais estrutura conforme necessário]
```

## 🤝 Contribuição

Contribuições são bem-vindas! Para contribuir:

1. Faça um Fork do projeto
2. Crie uma branch para sua feature (`git checkout -b feature/MinhaFeature`)
3. Commit suas mudanças (`git commit -m 'Adiciona MinhaFeature'`)
4. Push para a branch (`git push origin feature/MinhaFeature`)
5. Abra um Pull Request

**Desenvolvido com ❤️**