import json
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
import time

# Caminho do driver do navegador
driver_path = "chromedriver-win64/chromedriver.exe"  # Atualize conforme seu sistema

def load_config(config_path="config.json"):
    """
    Carrega as configurações de ajuste visual de um arquivo JSON.

    Args:
        config_path (str): Caminho para o arquivo de configuração.

    Returns:
        dict: Configurações carregadas.
    """
    try:
        with open(config_path, "r") as f:
            config = json.load(f)
        print(f"Configurações carregadas de {config_path}")
        return config
    except FileNotFoundError:
        print("Arquivo de configuração não encontrado. Usando padrões.")
        return {
            "level": "high",  # Nível mais alto para ajustes visuais fortes
            "dark_mode": True,  # Modo escuro para reduzir a luz excessiva
            "remove_videos": True,  # Remover vídeos que são distrações visuais
            "remove_images": True,  # Remover imagens
            "custom_css": "",
            "font_size": "18px",  # Tamanho maior de fonte
            "high_contrast": True,  # Ativar o alto contraste
            "animations_disabled": True  # Desabilitar animações e transições
        }

def generate_css(config):
    """
    Gera o CSS baseado no nível de ajuste especificado.

    Args:
        config (dict): Configurações para gerar o CSS.

    Returns:
        str: CSS gerado.
    """
    level = config.get("level", "high")
    dark_mode = config.get("dark_mode", False)
    remove_videos = config.get("remove_videos", False)
    remove_images = config.get("remove_images", False)
    custom_css = config.get("custom_css", "")
    font_size = config.get("font_size", "18px")  # Tamanho de fonte
    high_contrast = config.get("high_contrast", False)  # Contraste alto
    animations_disabled = config.get("animations_disabled", True)  # Desabilitar animações

    # CSS base
    base_css = "* { animation: none !important; transition: none !important; box-shadow: none !important; }" if animations_disabled else ""
    body_css = f"body {{ background-color: #ffffff !important; color: #000000 !important; font-size: {font_size} !important; }}"

    # Se o alto contraste for ativado
    if high_contrast:
        base_css += " body { background-color: #000000 !important; color: #FFFFFF !important; }"  # Fundo preto e texto branco
        body_css += " * { color: #FFFFFF !important; background-color: #000000 !important; }"  # Garantir que todos os elementos sigam a regra

    if remove_images:
        base_css += " img { display: none !important; }"  # Remover imagens
    if remove_videos:
        base_css += " video { display: none !important; }"  # Remover vídeos
    
    if dark_mode:
        body_css = "body { background-color: #222222 !important; color: #E0E0E0 !important; }"
    
    if level == "high":
        base_css += " * { font-family: Arial, sans-serif !important; }"  # Fonte simples e sem distrações
    
    return f"{base_css}\n{body_css}\n{custom_css}"

def apply_visual_adjustments(url, config):
    """
    Reduz os efeitos visuais de um site com base nas configurações fornecidas.

    Args:
        url (str): URL do site a ser ajustado.
        config (dict): Configurações para os ajustes visuais.
    """
    print(f"Iniciando ajustes visuais para o site: {url}")
    print(f"Nível de ajustes: {config.get('level', 'high').upper()}")

    # Inicializar o driver
    service = Service(driver_path)
    driver = webdriver.Chrome(service=service)

    # Abrir o site
    driver.get(url)

    # Gera o CSS e injeta no site
    css = generate_css(config)
    script = f"""
    var css = `{css}`;
    var style = document.createElement('style');
    style.type = 'text/css';
    style.appendChild(document.createTextNode(css));
    document.head.appendChild(style);
    """
    driver.execute_script(script)
    print("Ajustes visuais aplicados.")

    # Manter o navegador aberto até o usuário pressionar uma tecla para sair
    while True:
        user_input = input("Digite 's' para sair e fechar o navegador: ").strip().lower()
        if user_input == 's':
            print("Fechando o navegador...")
            driver.quit()
            break
        else:
            print("Comando não reconhecido. O navegador continuará aberto.")

# Carregar configurações
config = load_config()

# Aplicar ajustes visuais
apply_visual_adjustments("https://msn.com", config)
