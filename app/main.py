from flask import Flask, jsonify, request
from flask_cors import CORS
from dotenv import load_dotenv
import os
load_dotenv()
import google.generativeai as genai

genai.configure(api_key=os.environ['API_KEY'])

app = Flask(__name__)
CORS(app)

@app.route('/ong/', methods=['POST'])
def dados_produto():
    dados = request.get_json()
    model = genai.GenerativeModel("gemini-1.5-flash")
    produto = dados["produto"]

    if produto.strip() == "":
        result = {
            "status": False,
            "message": "Informe um produto"
        }

        return jsonify(result)

    # Prompt único para obter todos os dados
    prompt = (f"Com base no nome do produto [{produto}], forneça as seguintes informações:\n"
              f"1. Uma estimativa direta do tempo médio de decomposição. Exemplo: 'Entre 20 e 30 anos.'. Considere o tipo de material geralmente associado a este tipo de produto e qualquer informação conhecida sobre a decomposição desse material. Se o produto é composto por mais de um material, forneça uma estimativa baseada no material mais predominante.\n"
              f"2. Responda 1 se o produto for reciclavel e 0 se não for.\n"
              f"3. Forneça uma estimativa da pegada de carbono do produto.\n"
              f"4. Uma análise abrangente do impacto social do produto, incluindo:\n"
              f"   - Impacto Social Positivo: Como o produto contribui para melhorias sociais, econômicas ou ambientais.\n"
              f"   - Impacto Social Negativo: Quais são os possíveis efeitos adversos que o produto pode ter sobre a sociedade.\n"
              f"   - Percepção Pública: Como o produto é percebido pelas pessoas e as possíveis controvérsias associadas a ele.\n"
              f"   - Dados e Tendências: Informações sobre estudos, pesquisas ou dados que ajudem a entender o impacto social do produto.\n"
              f"IMPORTANTE RESPONDER com as informações SEPARADAS POR UMA LINHA sendo a primeira linha a decomposição, a segunda se ele é ou não reciclavel e assim por diante. NÃO QUERO TÓPICOS QUERO A RESPOSTA DIRETA SEPARADA UMA POR LINHA. SEGUE ABAIXO UM EXEMPLO DE RESPOSTA:"
              f"""Entre 100 e 200 anos
              0,
              Entre 10 e 20 kg CO2
              [impacto social do produto]""")

    # Gerar conteúdo usando o modelo
    response = model.generate_content(prompt)
    response_data = response.to_dict()
    content = response_data["candidates"][0]["content"]["parts"][0]["text"]

    # Extrair dados da resposta
    lines = content.split("\n")
    decomposicao = lines[0].strip()
    reciclavel = lines[1].strip() == "1"
    pegada_carbono = lines[2].strip()
    impacto_social = "\n".join(lines[3:]).strip()

    # Objeto com todos os dados do produto
    dados_produto = {
        "decomposicao": decomposicao,
        "reciclavel": reciclavel,
        "impacto_social": impacto_social,
        "pegada_carbono": pegada_carbono
    }
    
    # Array resultado
    result = {
        "status": True,
        "message": "Dados coletados com sucesso!",
        "data": dados_produto
    }

    return jsonify(result)

if __name__ == '__main__':
    app.run(debug=True)
