# Pipeline de Dados

O pipeline de dados é uma parte essencial do projeto, sendo responsável por transformar os dados brutos em informações valiosas para análise. O processo é dividido em várias camadas, cada uma com um propósito específico:

## Camadas do Pipeline
1. **Landing**: Recebe os dados brutos, geralmente de fontes externas ou de ingestão inicial.
2. **Bronze**: Limpeza dos dados brutos, removendo erros ou inconsistências.
3. **Silver**: Dados organizados e enriquecidos, prontos para análise preliminar.
4. **Gold**: Dados otimizados e estruturados para a criação de KPIs e visualizações.

## Fluxo de Dados
O fluxo de dados é automatizado e garante a integridade e a qualidade das informações, seguindo este caminho:

- **Ingestão de Dados**: Importação dos dados dos sistemas de saúde.
- **Processamento e Limpeza**: Tratamento e limpeza dos dados.
- **Transformações**: Enriquecimento e organização dos dados para análise.

## Ferramentas Utilizadas
- **Apache Spark**: Para transformação de grandes volumes de dados.
- **MySQL/PostgreSQL**: Banco de dados utilizado para armazenar os dados processados.
