# 🏛️ JURI.AI - Sistema Inteligente de Gestão Jurídica

![Python](https://img.shields.io/badge/Python-3.11+-blue.svg)
![Django](https://img.shields.io/badge/Django-5.0+-green.svg)
![OpenAI](https://img.shields.io/badge/OpenAI-GPT--4-orange.svg)
![LangChain](https://img.shields.io/badge/LangChain-Enabled-purple.svg)

Sistema completo de inteligência artificial para gestão jurídica, análise de documentos e atendimento automatizado via WhatsApp, desenvolvido com Django e integrado com múltiplas APIs de IA.

---

## 📋 Índice

- [Visão Geral](#-visão-geral)
- [Funcionalidades Principais](#-funcionalidades-principais)
- [Agentes de IA](#-agentes-de-ia)
- [Integrações](#-integrações)
- [Estrutura do Projeto](#-estrutura-do-projeto)
- [Tecnologias Utilizadas](#-tecnologias-utilizadas)
- [Instalação](#-instalação)
- [Configuração](#-configuração)
- [Uso](#-uso)
- [API Endpoints](#-api-endpoints)
- [Arquitetura RAG](#-arquitetura-rag)
- [Contribuindo](#-contribuindo)

---

## 🎯 Visão Geral

O **JURI.AI** é uma plataforma completa para escritórios de advocacia que combina inteligência artificial, processamento de documentos e automação de atendimento. O sistema utiliza técnicas avançadas de RAG (Retrieval-Augmented Generation), OCR e análise jurisprudencial para fornecer insights precisos e automatizar tarefas repetitivas.

### Principais Diferenciais

- ✅ **Análise Automática de Jurisprudência** com pontuação de risco
- ✅ **OCR Inteligente** para extração de texto de documentos jurídicos
- ✅ **Agentes de IA Especializados** para diferentes domínios
- ✅ **RAG (Retrieval-Augmented Generation)** com base de conhecimento vetorizada
- ✅ **Integração WhatsApp** via Evolution API
- ✅ **Agendamento Inteligente** com Google Calendar
- ✅ **Consulta API DataJud (CNJ)** para processos judiciais

---

## 🚀 Funcionalidades Principais

### 1. Análise de Jurisprudência

Sistema avançado de análise de documentos jurídicos que identifica:

- **Erros de Coerência e Lacunas Argumentativas**
  - Detecção automática de inconsistências
  - Identificação de argumentos fracos ou incompletos
  - Sugestões de melhorias

- **Riscos Jurídicos**
  - Análise de precedentes desfavoráveis
  - Identificação de pontos vulneráveis
  - Avaliação de probabilidade de sucesso

- **Problemas de Formatação e Estrutura**
  - Verificação de padrões ABNT
  - Análise de organização do documento
  - Checklist de elementos obrigatórios

- **Red Flags Críticas**
  - Identificação de erros graves
  - Prazos e prescrições
  - Competência e legitimidade

- **Índice de Risco Geral (0-100)**
  - Baixo (0-30): Documento bem estruturado
  - Médio (31-60): Necessita revisão pontual
  - Alto (61-80): Requer atenção urgente
  - Crítico (81-100): Alto risco de indeferimento

### 2. OCR (Reconhecimento Óptico de Caracteres)

- Extração automática de texto de PDFs escaneados
- Suporte para múltiplos formatos de documento
- Processamento em lote
- Indexação automática para busca

### 3. Chat Jurídico com RAG

Sistema de chat inteligente com:
- Respostas baseadas em documentos do cliente
- Consulta automática à base de conhecimento
- Memória de conversação
- Referências e citações automáticas
- Streaming de respostas em tempo real

### 4. Atendimento WhatsApp Automatizado

- Secretária virtual 24/7
- Agendamento de reuniões
- Consulta de informações sobre produtos/serviços
- Qualificação de leads
- Integração com Evolution API

### 5. Gestão de Clientes e Documentos

- Upload e organização de documentos
- Histórico de conversas
- Análises realizadas
- Dashboard de métricas

---

## 🤖 Agentes de IA

### 1. JuriAI - Assistente Jurídico Virtual

**Especialidade:** Consultas jurídicas e análise de processos

**Capacidades:**
- Acesso a base de conhecimento vetorizada (RAG)
- Consulta à API pública do DataJud (CNJ)
- Busca de jurisprudências e precedentes
- Análise contextual de documentos do cliente
- Memória de conversação persistente

**Ferramentas:**
- `search_datajud_api`: Busca processos judiciais
- Knowledge Base Search: Consulta documentos vetorizados
- Memory System: SQLite para histórico

**Código de Exemplo:**
```python
agent = JuriAI.build_agent(
    knowledge_filters={'cliente_id': cliente_id}
)
response = agent.run("Qual o status do processo 0000832-35.2018.4.01.3202?")
```

### 2. JurisprudenciaAI - Analisador de Documentos

**Especialidade:** Análise profunda de peças processuais

**Capacidades:**
- Avaliação de coerência argumentativa
- Identificação de riscos jurídicos
- Verificação de formatação e estrutura
- Detecção de red flags críticas
- Cálculo de índice de risco

**Arquitetura:**
- LangChain com OpenAI GPT-4
- Structured Output para análise padronizada
- Prompt Engineering otimizado para contexto jurídico

**Output Estruturado:**
```python
class AnaliseResponse:
    indice_risco: int  # 0-100
    erros_coerencia: List[str]
    riscos_juridicos: List[str]
    problemas_formatacao: List[str]
    red_flags: List[str]
```

### 3. SecretariaAI - Assistente de Atendimento

**Especialidade:** Atendimento ao cliente e agendamento

**Capacidades:**
- Consulta à base de conhecimento da empresa
- Agendamento inteligente com Google Calendar
- Qualificação de leads
- Vendas consultivas
- Atendimento multicanal (WhatsApp)

**Restrições de Agendamento:**
- Horário: 13h às 18h (horário local)
- Verificação automática de disponibilidade
- Duração padrão: 1 hora
- Confirmação antes de criar evento

**Ferramentas:**
- `GoogleCalendarTools`: Gestão de agenda
- Knowledge Base: Informações da empresa
- Memory: Histórico de atendimentos por telefone

**Fluxo de Atendimento:**
1. Saudação cordial
2. Identificação da necessidade
3. Consulta à base de conhecimento
4. Direcionamento para produto/serviço
5. Agendamento de reunião (se aplicável)
6. Confirmação e despedida

---

## 🔗 Integrações

### 1. OpenAI API
- **Modelos:** GPT-4, GPT-4o-mini
- **Uso:** Chat, análise, embeddings
- **Configuração:** Variável `OPENAI_API_KEY`

### 2. Evolution API (WhatsApp)
- **Funcionalidade:** Envio/recebimento de mensagens
- **Webhook:** `/ai/webhook/whatsapp`
- **Instância:** Configurável via `EVOLUTION_INSTANCE_NAME`

### 3. Google Calendar API
- **Funcionalidade:** Agendamento de reuniões
- **Autenticação:** OAuth 2.0
- **Credenciais:** `client_secret.json`

### 4. DataJud API (CNJ)
- **Funcionalidade:** Consulta de processos judiciais
- **Tribunais:** STJ, TST, TRFs, TJs estaduais
- **Endpoint:** `https://api-publica.datajud.cnj.jus.br`

### 5. LanceDB (Vector Database)
- **Funcionalidade:** Armazenamento de embeddings
- **Tabelas:** `documentos`, `empresa`
- **Embedder:** OpenAI text-embedding-3-small

### 6. SQLite
- **Funcionalidade:** Memória de conversação
- **Tabelas:** `my_memory_table`, `secretaria_memory_table`

---

## 📁 Estrutura do Projeto

```
JURI.AI/
│
├── ai/                                 # App principal de IA
│   ├── migrations/                     # Migrações do banco
│   ├── templates/                      # Templates HTML
│   │   ├── chat.html                   # Interface de chat
│   │   ├── ver_referencias.html        # Visualização de contextos RAG
│   │   └── analise_jurisprudencia.html # Dashboard de análise
│   ├── __init__.py
│   ├── admin.py                        # Admin Django
│   ├── agent.py                        # ⭐ Agentes (JuriAI, SecretariaAI)
│   ├── agent_langchain.py              # ⭐ JurisprudenciaAI (LangChain)
│   ├── apps.py
│   ├── literals.py                     # Tipos literais (TribunalLiteral)
│   ├── models.py                       # Models (Pergunta, ContextRag, AnaliseJurisprudencia)
│   ├── tasks.py
│   ├── tests.py
│   ├── urls.py                         # Rotas do app AI
│   ├── views.py                        # ⭐ Views (chat, análise, webhook)
│   └── wrapper_evolution_api.py        # ⭐ Wrapper Evolution API
│
├── core/                               # Configurações do projeto
│   ├── __pycache__/
│   ├── __init__.py
│   ├── asgi.py
│   ├── settings.py                     # ⭐ Settings Django
│   ├── urls.py                         # URLs principais
│   └── wsgi.py
│
├── lancedb/                            # Banco vetorial LanceDB
│   ├── documentos.lance/               # Embeddings de documentos
│   └── empresa.lance/                  # Embeddings da empresa
│
├── media/documentos/                   # Uploads de documentos
│
├── static/                             # Arquivos estáticos
│
├── templates/                          # Templates globais
│   └── base.html
│
├── usuarios/                           # App de usuários
│   ├── migrations/
│   ├── static/
│   ├── templates/
│   ├── __init__.py
│   ├── admin.py
│   ├── apps.py
│   ├── models.py                       # Models (Cliente, Documentos)
│   ├── signals.py
│   ├── tests.py
│   ├── urls.py
│   └── views.py
│
├── venv/                               # Ambiente virtual Python
│
├── .env                                # ⚙️ Variáveis de ambiente
├── .env.example                        # Exemplo de configuração
├── .gitignore
├── client_secret.json                  # ⚙️ Credenciais Google OAuth
├── db.sqlite3                          # ⚙️ Banco de dados principal
├── manage.py                           # Django management
└── README.md                           # Este arquivo
```

### Arquivos Principais

| Arquivo | Descrição |
|---------|-----------|
| `ai/agent.py` | Define os agentes JuriAI e SecretariaAI |
| `ai/agent_langchain.py` | Implementa JurisprudenciaAI com LangChain |
| `ai/views.py` | Controllers para chat, análise e webhook |
| `ai/models.py` | Models de Pergunta, ContextRag e AnaliseJurisprudencia |
| `ai/wrapper_evolution_api.py` | Cliente HTTP para Evolution API |
| `usuarios/models.py` | Models de Cliente e Documentos |
| `core/settings.py` | Configurações do Django |

---

## 🛠️ Tecnologias Utilizadas

### Backend
- **Django 5.0+** - Framework web
- **Python 3.11+** - Linguagem principal
- **SQLite** - Banco de dados

### IA e Machine Learning
- **OpenAI GPT-4/4o-mini** - Modelos de linguagem
- **LangChain** - Framework para LLMs
- **Agno (Phidata)** - Framework para agentes autônomos
- **LanceDB** - Banco de dados vetorial
- **OpenAI Embeddings** - Vetorização de documentos

### Integrações
- **Evolution API** - WhatsApp Business
- **Google Calendar API** - Agendamento
- **DataJud API (CNJ)** - Processos judiciais

### Frontend
- **Tailwind CSS** - Framework CSS
- **JavaScript** - Interatividade
- **HTML5** - Estrutura

### Outras
- **python-dotenv** - Variáveis de ambiente
- **requests** - Cliente HTTP
- **tzlocal** - Fuso horário local

---

## 📦 Instalação

### Pré-requisitos

- Python 3.11 ou superior
- pip (gerenciador de pacotes Python)
- Git
- Conta OpenAI com API Key
- (Opcional) Conta Google Cloud para Calendar API
- (Opcional) Instância Evolution API para WhatsApp

### Passo a Passo

1. **Clone o repositório**
```bash
git clone https://github.com/seu-usuario/juri-ai.git
cd juri-ai
```

2. **Crie e ative o ambiente virtual**
```bash
python -m venv venv

# Windows
venv\Scripts\activate

# Linux/Mac
source venv/bin/activate
```

3. **Instale as dependências**
```bash
pip install -r requirements.txt
```

4. **Configure as variáveis de ambiente**
```bash
cp .env.example .env
# Edite o arquivo .env com suas credenciais
```

5. **Execute as migrações**
```bash
python manage.py migrate
```

6. **Crie um superusuário**
```bash
python manage.py createsuperuser
```

7. **Colete arquivos estáticos**
```bash
python manage.py collectstatic
```

8. **Inicie o servidor**
```bash
python manage.py runserver
```

9. **Acesse a aplicação**
```
http://localhost:8000
```

---

## ⚙️ Configuração

### Arquivo `.env`

```env
# OpenAI
OPENAI_API_KEY=sk-proj-...

# Evolution API (WhatsApp)
EVOLUTION_API_KEY=sua-api-key
EVOLUTION_API_BASE_URL=https://sua-instancia.railway.app

# Django
SECRET_KEY=sua-secret-key-django
DEBUG=True
ALLOWED_HOSTS=localhost,127.0.0.1

# Database (opcional, SQLite é padrão)
DATABASE_URL=sqlite:///db.sqlite3
```

### Google Calendar API

1. Acesse [Google Cloud Console](https://console.cloud.google.com)
2. Crie um novo projeto
3. Habilite a API do Google Calendar
4. Crie credenciais OAuth 2.0
5. Baixe o arquivo `client_secret.json`
6. Coloque na raiz do projeto

**URIs de redirecionamento autorizados:**
```
http://localhost:8000/oauth2callback
http://127.0.0.1:8000/oauth2callback
```

### Evolution API (WhatsApp)

1. Configure sua instância Evolution API
2. Obtenha a API Key
3. Configure o webhook apontando para: `http://seu-dominio.com/ai/webhook/whatsapp`

---

## 💡 Uso

### 1. Chat Jurídico

**URL:** `/ai/chat/<cliente_id>`

```python
# Exemplo de uso via API
import requests

response = requests.post(
    'http://localhost:8000/ai/chat/1',
    data={'pergunta': 'Qual o prazo para recurso de apelação?'}
)
```

### 2. Análise de Documento

**URL:** `/ai/analise/<documento_id>`

1. Faça upload do documento via admin ou API
2. Acesse a página de análise
3. Clique em "Analisar Documento"
4. Aguarde o processamento (pode levar 30-60 segundos)
5. Visualize os resultados

### 3. WhatsApp (via Webhook)

O webhook processa automaticamente mensagens recebidas:

```python
# Exemplo de payload recebido
{
    "data": {
        "key": {
            "remoteJid": "5511999999999@s.whatsapp.net"
        },
        "message": {
            "conversation": "Olá, gostaria de agendar uma reunião"
        }
    }
}
```

---

## 🌐 API Endpoints

### Chat e Análise

| Método | Endpoint | Descrição |
|--------|----------|-----------|
| GET/POST | `/ai/chat/<id>` | Interface de chat |
| POST | `/ai/stream_resposta/` | Stream de resposta do agente |
| GET | `/ai/ver_referencias/<id>` | Visualiza contextos RAG |
| GET | `/ai/analise/<id>` | Dashboard de análise |
| POST | `/ai/processar_analise/<id>` | Processa análise de documento |

### Webhook

| Método | Endpoint | Descrição |
|--------|----------|-----------|
| POST | `/ai/webhook/whatsapp` | Recebe mensagens do WhatsApp |

### Exemplo de Resposta - Análise

```json
{
    "indice_risco": 45,
    "classificacao": "Médio",
    "erros_coerencia": [
        "Contradição entre parágrafo 3 e 7 sobre data do fato",
        "Argumentação circular na fundamentação jurídica"
    ],
    "riscos_juridicos": [
        "Jurisprudência recente desfavorável (REsp 1234567)",
        "Possível incompetência do juízo"
    ],
    "problemas_formatacao": [
        "Ausência de sumário",
        "Numeração de páginas incorreta"
    ],
    "red_flags": [
        "Prazo prescricional próximo do vencimento"
    ],
    "tempo_processamento": 42
}
```

---

## 🧠 Arquitetura RAG

### Como Funciona

O sistema utiliza RAG (Retrieval-Augmented Generation) para fornecer respostas contextualizadas:

```
┌─────────────┐
│   Pergunta  │
└──────┬──────┘
       │
       ▼
┌─────────────────┐
│  Vetorização    │ (OpenAI Embeddings)
│  da Pergunta    │
└──────┬──────────┘
       │
       ▼
┌─────────────────┐
│  Busca Vetorial │ (LanceDB)
│  Similaridade   │
└──────┬──────────┘
       │
       ▼
┌─────────────────┐
│  Top-K Docs     │ (k=5 documentos mais relevantes)
│  Recuperados    │
└──────┬──────────┘
       │
       ▼
┌─────────────────┐
│  Contexto +     │
│  Pergunta →     │ → OpenAI GPT-4
│  LLM            │
└──────┬──────────┘
       │
       ▼
┌─────────────────┐
│  Resposta       │
│  Fundamentada   │
└─────────────────┘
```

### Fluxo de Dados

1. **Indexação** (ao fazer upload):
   ```python
   documento → OCR → chunks → embeddings → LanceDB
   ```

2. **Consulta** (ao fazer pergunta):
   ```python
   pergunta → embedding → busca vetorial → top-k docs → LLM → resposta
   ```

3. **Filtros**:
   - Por cliente: `knowledge_filters={'cliente_id': 1}`
   - Por tipo de documento
   - Por data

### Métricas

- **Similaridade:** Cosine similarity > 0.7
- **Top-K:** 5 documentos mais relevantes
- **Chunk Size:** 1000 tokens
- **Overlap:** 200 tokens

---

## 📊 Modelos de Dados

### Cliente
```python
class Cliente(models.Model):
    nome = CharField(max_length=100)
    email = EmailField()
    telefone = CharField(max_length=20)
    cpf_cnpj = CharField(max_length=18)
    endereco = TextField()
    data_cadastro = DateTimeField(auto_now_add=True)
```

### Documentos
```python
class Documentos(models.Model):
    cliente = ForeignKey(Cliente)
    tipo = CharField(choices=TIPO_CHOICES)
    arquivo = FileField(upload_to='documentos/')
    content = TextField()  # Texto extraído via OCR
    data_upload = DateTimeField(auto_now_add=True)
```

### Pergunta
```python
class Pergunta(models.Model):
    cliente = ForeignKey(Cliente)
    pergunta = TextField()
    data_criacao = DateTimeField(auto_now_add=True)
```

### ContextRag
```python
class ContextRag(models.Model):
    pergunta = ForeignKey(Pergunta)
    content = TextField()
    tool_name = CharField(max_length=100)
    tool_args = JSONField()
    data_criacao = DateTimeField(auto_now_add=True)
```

### AnaliseJurisprudencia
```python
class AnaliseJurisprudencia(models.Model):
    documento = OneToOneField(Documentos)
    indice_risco = IntegerField()
    classificacao = CharField(max_length=20)
    erros_coerencia = JSONField()
    riscos_juridicos = JSONField()
    problemas_formatacao = JSONField()
    red_flags = JSONField()
    tempo_processamento = IntegerField()
    data_criacao = DateTimeField(auto_now_add=True)
```

---

## 🔒 Segurança

- ✅ CSRF Protection habilitado
- ✅ API Keys em variáveis de ambiente
- ✅ Sanitização de inputs
- ✅ Autenticação OAuth 2.0 para Google
- ✅ Rate limiting na API Evolution
- ⚠️ Em produção: use HTTPS e `DEBUG=False`

---

## 🚦 Roadmap

- [ ] Suporte a múltiplos idiomas
- [ ] Integração com mais tribunais via API
- [ ] Dashboard analítico para métricas
- [ ] Exportação de relatórios em PDF
- [ ] App mobile (React Native)
- [ ] Integração com Telegram
- [ ] Sistema de templates de documentos
- [ ] OCR com correção ortográfica
- [ ] Fine-tuning de modelo específico para direito brasileiro

---

## 🤝 Contribuindo

Contribuições são bem-vindas! Por favor:

1. Fork o projeto
2. Crie uma branch para sua feature (`git checkout -b feature/MinhaFeature`)
3. Commit suas mudanças (`git commit -m 'Adiciona MinhaFeature'`)
4. Push para a branch (`git push origin feature/MinhaFeature`)
5. Abra um Pull Request

---

## 👥 Autores

- **Álvaro Veiga** - [GitHub](https://github.com/alvaro-veiga)

-----

## 📞 Suporte

- **Email:** alvarojoao17@gmail.com

---
