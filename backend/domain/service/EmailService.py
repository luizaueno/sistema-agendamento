import json
import os
import requests
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from dotenv import load_dotenv

# Carrega o arquivo .env voltando uma pasta (raiz do projeto)
load_dotenv(dotenv_path="../.env")

# O .strip() limpa qualquer caractere invisível
MAILTRAP_HOST = os.getenv("MAILTRAP_HOST", "").strip()
MAILTRAP_PORT = os.getenv("MAILTRAP_PORT", "").strip()
MAILTRAP_USER = os.getenv("MAILTRAP_USER", "").strip()  
API_TOKEN = os.getenv("API_TOKEN", "").strip()



def email_convite( email_destinatario, token_jwt):
    # Envia o e-mail de convite utilizando as credenciais do Mailtrap configuradas no sistema
    msg = MIMEMultipart("alternative")
    msg["Subject"] = "Defina sua senha e acesse o sistema"
    msg["From"] = "bruna.rmendes@email.com"
    msg["To"] = email_destinatario
    url = f"http://localhost:5173/definir-senha?token={token_jwt}"
    texto_puro = f"Olá! Acesse o link para criar sua senha: {url}"
    
    html = f"""
    <html>
      <body>
        <h2>Acesse o sistema e faça parte da equipe</h2>
        <p>Clique no botão abaixo para concluir o seu cadastro e definir sua senha:</p>
        <a href="{url}" target="_blank">
            Criar Minha Senha
        </a>
      </body>
    </html>
    """

    msg.attach(MIMEText(texto_puro, "plain"))
    msg.attach(MIMEText(html, "html"))

    try:
        url_api = "https://sandbox.api.mailtrap.io/api/send/4895353"

        # 3. ALTERAÇÃO NOS HEADERS: Agora injetamos a variável 'api_token' aqui
        headers = {
            "Authorization": f"Bearer {API_TOKEN}",
            "Content-Type": "application/json",
        }

        payload = {
            "from": {"email": "no-reply@sistema_fake.com", "name": "Sistema"},
            "to": [{"email": email_destinatario}],
            "subject": msg["Subject"],
            "html": html,
            "text": texto_puro,
        }

        print("Enviando requisição HTTP para a API do Mailtrap...")
        
        response = requests.post(
            url_api, headers=headers, data=json.dumps(payload)
        )

        if response.status_code in [200, 201]:
            return True
        else:
            print(f"Erro na API do Mailtrap: {response.text}")
            return False
            
    except Exception as e:
        print(f"Falha ao enviar e-mail via API: {e}")
        return False


if __name__ == "__main__":
    print("Tentando enviar o e-mail de teste para o Mailtrap...")

    email_da_profissional = "profissional_teste@exemplo.com"
    token_ficticio = "abc123xyz456_token_de_teste"

    sucesso = email_convite(
        email_da_profissional, token_ficticio
    )

    if sucesso:
        print(
            "\n🎉 SUCESSO! O e-mail foi enviado via API HTTP e interceptado pelo Mailtrap."
        )
        print("Abra o painel do Mailtrap no seu navegador para ver o resultado!")
    else:
        print("\n❌ Não enviou. Ocorreu o erro listado acima.")