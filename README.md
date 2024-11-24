# **Flare**
**Flare** é um script Python utilizando Selenium para reduzir a carga sensorial de sites. Este projeto foi projetado para ajudar neurodivergentes a navegarem na web de forma mais confortável, ajustando elementos visuais como animações, transições, cores e outros aspectos visuais potencialmente sobrecarregantes.

---

## **Recursos**
- Desativação de animações, transições e sombras.
- Habilitação de modo escuro para reduzir o brilho.
- Remoção de vídeos ou imagens em níveis mais altos.
- Suporte a níveis de ajuste configuráveis: `low`, `medium`, e `high`.
- Personalização adicional via arquivo `config.json`.

---

## **Exemplo de Resultado**
- Antes: Site com animações, transições, imagens piscantes.
- Depois: Site estático com menos distrações visuais e um layout mais acessível.

---

## **Instalação**

### **Pré-requisitos**
1. **Python 3.8 ou superior** instalado.
2. **Google Chrome** instalado no sistema.
3. **ChromeDriver** compatível com sua versão do Chrome.
   - [Baixe aqui](https://chromedriver.chromium.org/downloads).

### **Passos de instalação**
1. Clone este repositório:
   ```bash
   git clone https://github.com/DuxAlex/flare.git
   cd flare
   Instale as dependências:
   ```

```bash
pip install selenium

```
2. Baixe o ChromeDriver:
Coloque o executável do ChromeDriver no caminho chromedriver-win64/chromedriver.exe ou ajuste o driver_path no script.
(Opcional) Personalize o arquivo config.json com suas preferências.

3. Execute o script para aplicar os ajustes visuais ao site desejado.
Execução com configurações padrão.
No terminal, rode:


```bash
python reduce_effects.py
```

O script carregará o site configurado e aplicará os ajustes baseados no arquivo config.json.

Configuração via config.json
Personalize os ajustes criando ou editando o arquivo config.json:

Exemplo:

```json
{
    "level": "high",
    "dark_mode": true,
    "remove_videos": true,
    "custom_css": "* { border: 1px solid red !important; }"
}
```

### **Opções Disponíveis**
level: Define o nível de ajuste (low, medium, high).
dark_mode: Ativa/desativa o modo escuro (booleano).
remove_videos: Remove vídeos das páginas (booleano).
custom_css: Adiciona estilos personalizados (string).
Contribuindo
Contribuições são bem-vindas! Sinta-se à vontade para abrir issues, sugerir melhorias ou enviar pull requests.





