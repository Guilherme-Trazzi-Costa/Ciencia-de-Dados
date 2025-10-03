from google import genai
from google.genai.errors import APIError
import json
import matplotlib.pyplot as plt

MINHA_CHAVE_GEMINI = "AIzaSyCIRpzOo9phSB6i1vLSUeH2Cd1BrLez0RE"
minhas_praias = {}

def fazer_pergunta_gemini(pergunta: str, chave_api: str):
    """
    Conecta-se à API Gemini, enviando a chave diretamente ao construtor Client.
    """
    try:
        client = genai.Client(api_key=chave_api)
        model_name = 'gemini-2.5-flash'
        print(f"Enviando pergunta para o modelo {model_name}...")

        response = client.models.generate_content(
            model=model_name,
            contents=pergunta,
        )

        return response.text

    except APIError as e:
        print(f"Ocorreu um erro na API: {e}")
        print("\nVerifique se a chave API fornecida está correta e ativa.")
    except Exception as e:
        print(f"Ocorreu um erro inesperado: {e}")

# Lista de praias
praias = ['Cala Mariolu – Itália', 'Normandia – França', 'Ubatuba – Brasil']

# Executar a função e formatar resposta
for praia in praias:
    pergunta = (f'no formato json resposta direta com os valores para os paramentros: '
                f'temperatura(só numeros), umidade(só numeros), qualidade_ar, da praia {praia}, '
                'resposta sem observação e sem notas')
    print(praia)

    resposta = fazer_pergunta_gemini(pergunta, MINHA_CHAVE_GEMINI)[7:-3]
    resposta = resposta.replace("\n", "").strip()
    resposta = json.loads(resposta)
    minhas_praias[praia] = resposta
    print(resposta)

# --- Preparar os dados ---
praias = list(minhas_praias.keys())
temperaturas = [int(v["temperatura"]) for v in minhas_praias.values()]
umidades = [int(v["umidade"]) for v in minhas_praias.values()]
qualidade_ar = [v["qualidade_ar"] for v in minhas_praias.values()]  # só texto

# --- Plotar os gráficos ---
plt.figure(figsize=(10,8))

# Temperatura
plt.subplot(3,1,1)
plt.bar(praias, temperaturas, color="orange")
plt.title("Comparação das Praias")
plt.ylabel("Temperatura (°C)")

# Umidade
plt.subplot(3,1,2)
plt.bar(praias, umidades, color="blue")
plt.ylabel("Umidade (%)")

# Qualidade do Ar (texto)
plt.subplot(3,1,3)
bars = plt.bar(praias, [1]*len(qualidade_ar), color="gray")  # dummy values
plt.ylabel("Qualidade do Ar")
plt.ylim(0, 1.5)  # limit y-axis for spacing

# Remove numeric labels from y-axis
plt.yticks([])

for bar, label in zip(bars, qualidade_ar):
    plt.text(bar.get_x() + bar.get_width()/2, 1.05, label,
             ha="center", va="bottom", fontsize=10, fontweight="bold")


# Adicionar texto em cada barra
for bar, label in zip(bars, qualidade_ar):
    plt.text(bar.get_x() + bar.get_width()/2, 0.5, label, ha='center', va='center', color='white', fontsize=12)

plt.xlabel("Praias")
plt.tight_layout()
plt.show()
