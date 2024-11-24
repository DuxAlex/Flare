import json
from selenium import webdriver
from selenium.webdriver.common.by import By
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
            "level": "medium",
            "dark_mode": False,
            "remove_videos": False,
            "custom_css": ""
        }

def generate_css(config):
    """
    Gera o CSS baseado no nível de ajuste especificado.

    Args:
        config (dict): Configurações para gerar o CSS.

    Returns:
        str: CSS gerado.
    """
    level = config.get("level", "medium")
    dark_mode = config.get("dark_mode", False)
    remove_videos = config.get("remove_videos", False)
    custom_css = config.get("custom_css", "")

    base_css = "* { animation: none !important; transition: none !important; box-shadow: none !important; }"
    body_css = "body { background-color: #ffffff !important; color: #000000 !important; }"

    if level == "high":
        base_css += " img, video { display: none !important; }"
        if dark_mode:
            body_css = "body { background-color: #222222 !important; color: #E0E0E0 !important; }"
    elif level == "medium" and dark_mode:
        body_css = "body { background-color: #333333 !important; color: #E0E0E0 !important; }"
    
    if remove_videos:
        base_css += " video { display: none !important; }"

    return f"{base_css}\n{body_css}\n{custom_css}"

def apply_visual_adjustments(url, config):
    """
    Reduz os efeitos visuais de um site com base nas configurações fornecidas.

    Args:
        url (str): URL do site a ser ajustado.
        config (dict): Configurações para os ajustes visuais.
    """
    print(f"Iniciando ajustes visuais para o site: {url}")
    print(f"Nível de ajustes: {config.get('level', 'medium').upper()}")

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

    # Aguarda visualização
    time.sleep(10)

    # para fechar o navegador basta descomentar as duas linhas abaixo
    #driver.quit()
    #print("Navegador fechado.")

# Carregar configurações
config = load_config()

# Aplicar ajustes visuais
apply_visual_adjustments("https://msn.com", config)
