# Projeto: Sustainability Scan

Este projeto é uma API desenvolvida em Python que consome a biblioteca **Gemini**. A API foi projetada para fornecer dados e métricas relacionadas à sustentabilidade, fornecidos pela IA.

- [Sobre o Projeto](#sobre-o-projeto)
- [Pré-requisitos](#pré-requisitos)
- [Instalação](#instalação)
- [Endpoints da API](#endpoints-da-api)

## Sobre o Projeto

Este projeto foi feito para um trabalho acadêmico da matéria "Fundamentos de Sistemas de Informação" na Pontifícia Universidade Católica de Minas Gerais. O trabalho consistia em soluções de software relacionadas ao tema **Sustentabilidade**.

## Pré-requisitos

Antes de começar, certifique-se de ter instalado as seguintes ferramentas:

- Python 3.7 ou superior
- `pip` - gerenciador de pacotes do Python

## Instalação

1. Clone este repositório:

    ```bash
    git clone https://github.com/ArthurRezendee/Projeto-Sustentabilidade.git
    cd Projeto-Sustentabilidade
    ```

2. Crie e ative um ambiente virtual (opcional, mas recomendado):

    ```bash
    python -m venv venv
    # Para Windows
    .\venv\Scripts\activate
    # Para Unix ou MacOS
    source venv/bin/activate
    ```

3. Instale as dependências:

    ```bash
    pip install -r requirements.txt
    ```

4. Crie um arquivo `.env` e adicione sua chave de API Gemini:

    ```env
    API_KEY=SUA_CHAVE_API
    ```

Após seguir esses passos, o código fonte estará configurado e pronto para ser editado! Agora, veja as instruções para consumir nossa API de forma independente, sem a necessidade de clonar o repositório.

## Sustainability Scan API

A API "Sustainability Scan" é composta até então por um único endpoint, responsável por trazer uma série de dados sobre sustentabilidade a partir de um produto passado.

### 1. **POST /sustainability/**
   - **Descrição**: Retorna um resumo das métricas de sustentabilidade para um determinado produto.
   - **Parâmetros de Consulta**:
     - `produto`: O produto de interesse (exemplo: "Smartphone").
   - **Corpo da Requisição**:
     ```json
     {
        "produto": "Smartphone",
     }
     ```
   - **Exemplo de Resposta**:
     ```json
     {
        "data": {
            "decomposicao": "Entre 100 e 200 anos",
            "impacto_social": "**Impacto Social Positivo:**\n* **Comunicação e Acesso à Informação:** Smartphones permitem comunicação instantânea e acesso à informação global, facilitando a conectividade e o conhecimento. \n* **Educação e Aprendizagem:**  Os smartphones são ferramentas educacionais poderosas, com acesso a cursos online, livros digitais e aplicativos de aprendizado.\n* **Empreendedorismo e Economia:**  Criação de novos negócios, plataformas de venda online e oportunidades de trabalho impulsionadas pelo uso de smartphones. \n* **Saúde e Bem-Estar:**  Aplicações de saúde, monitoramento de condições médicas e acesso a informações sobre saúde contribuem para o bem-estar.\n* **Segurança Pública:** Smartphones podem ser utilizados para comunicação com autoridades, rastreamento de localização e denúncias, auxiliando na segurança pública.\n\n**Impacto Social Negativo:**\n* **Dependência e Adição:**  Uso excessivo pode levar à dependência, isolamento social e problemas de saúde mental.\n* **Distrações e Falta de Concentração:** Smartphones podem ser uma fonte de distração constante, afetando a concentração e o desempenho em tarefas importantes.\n* **Privacidade e Segurança:**  Violação de dados, espionagem e rastreamento de informações podem comprometer a privacidade dos usuários.\n* **Desigualdade Digital:**  Acesso desigual à tecnologia e falta de conhecimento podem criar uma lacuna digital entre diferentes grupos sociais.\n* **Impacto Ambiental:**  Produção e descarte inadequado de smartphones geram resíduos eletrônicos e impactos ambientais.\n\n**Percepção Pública:**\n* **Obsessão por Tecnologia:**  A cultura do \"smartphone\" é vista por alguns como uma obsessão por tecnologia, com consequências negativas para a vida social e mental.\n* **Cultura do \"Selfie\" e Compartilhamento Excessivo:**  O uso de smartphones para registrar a vida pessoal e compartilhá-la nas redes sociais gera debate sobre privacidade e o culto à imagem.\n* **Bullying Online:**  Aumento de casos de bullying online, assédio e intimidação, impulsionado pelas plataformas de comunicação online.\n\n**Dados e Tendências:**\n* Estudos mostram o aumento do uso de smartphones em todas as faixas etárias, impacto na saúde mental, dependência digital e desafios para a educação.\n* Dados sobre o consumo excessivo de mídias sociais e o impacto na atenção, concentração e relacionamentos interpessoais.\n* Relatórios sobre a crescente produção de resíduos eletrônicos e impacto ambiental do descarte inadequado de smartphones.",
            "pegada_carbono": "Entre 100 e 200 kg CO2",
            "reciclavel": true
        },
        "message": "Dados coletados com sucesso!",
        "status": true
     }
     ```


