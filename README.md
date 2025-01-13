# Extrator de PDFs

Este projeto foi desenvolvido como parte de um teste técnico para a posição de Analista Desenvolvedor Back-End - Python. O sistema permite que usuários façam o upload de 5 documentos jurídicos (em formato PDF), processem seus dados através de uma fila de mensagens e gerem uma planilha consolidada com as informações extraídas.

## Requisitos

Python 3.11 ou superior.
Docker e Docker Compose.
RabbitMQ (configurado no docker-compose.yml).

## Configuração

### 1. Clonar o Repositório

```bash
git clone https://github.com/pradovncs/finch-teste-tecnico.git
```

### 2. Suba os serviços com Docker Compose de acordo com o seu sistema operacional

```bash
docker-compose -f .\docker-compose.windows.yml up --build
docker-compose -f /docker-compose.linux.yml up --build
```

### 3. Acesse a aplicação web: Abra seu navegador e acesse http://127.0.0.1:8000/.

### 4. Faça o upload dos arquivos PDFs.

### 5. O arquivo gerado estará na pasta de downloads do seu sistema com o nome processos.xlsx


## OBS
Durante o desenvolvimento do projeto, tive dificuldades em achar processos abertos fazendo buscas no google, encontrei um processo aberto contra a fazenda
pública do estado de são paulo e pedi auxilio ao chat GPT para formular mais um exemplo e testar o processamento de multiplos arquivos.
Deixo ambos os processos utilizados para o desenvolvimento no repositório do projeto na pasta /uploads
