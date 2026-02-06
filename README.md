# Near-Earth Object Monitoring (NASA)

Projeto em Python para coleta, processamento e monitoramento de Objetos Próximos à Terra (Near-Earth Objects – NEOs) utilizando dados públicos da NASA.

## Objetivo

Este projeto tem como objetivo demonstrar habilidades práticas em integração com APIs externas, organização de código em camadas, persistência de dados e visualização em console.
É um projeto voltado para nível Júnior, com foco em boas práticas e clareza do código.

## Funcionalidades

- Coleta de dados da API pública da NASA (NEO Feed)
- Processamento e classificação de risco dos objetos
- Armazenamento dos dados em banco SQLite
- Visualização dos dados em formato de tabela no terminal
- Geração de relatório CSV

## Arquitetura do Projeto

O projeto segue uma separação de responsabilidades em camadas:

- Collectors: Responsável por coletar dados da API da NASA
- Services: Contém as regras de negócio e orquestra o fluxo
- Processors: Realiza classificações e cálculos (ex: risco)
- Repositories: Responsável pela persistência dos dados
- Views: Exibição dos dados no terminal
- Reports: Geração de relatórios (CSV)

## Estrutura de Pastas

neo_monitoring/
├── app/
│   ├── collectors/
│   ├── models/
│   ├── processors/
│   ├── repositories/
│   ├── reports/
│   ├── services/
│   └── views/
├── main.py
├── requirements.txt
├── README.md
└── .gitignore

## Tecnologias Utilizadas

- Python 3
- Requests
- SQLite
- API pública da NASA

## Como Executar o Projeto

1. Clonar o repositório

git clone https://github.com/SEU_USUARIO/neo_monitoring.git
cd neo_monitoring

2. Instalar dependências

pip install -r requirements.txt

3. Executar o projeto

python main.py

Ao executar, o sistema irá:
- Buscar os dados mais recentes da NASA
- Processar e salvar os objetos no banco
- Exibir uma tabela com os NEOs processados
- Gerar um relatório CSV

## Fonte dos Dados

Os dados utilizados neste projeto são fornecidos pela NASA por meio de suas APIs públicas:
https://api.nasa.gov/

## Possíveis Evoluções

- Monitoramento contínuo com atualização automática
- Interface gráfica ou dashboard web
- Alertas para objetos classificados como risco elevado
- Integração com visualização astronômica

## Autor

Eduardo Costa
