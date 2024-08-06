from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
import shutil
import tempfile
import os

def create_temp_profile(original_profile):
    temp_dir = tempfile.mkdtemp()
    temp_profile = os.path.join(temp_dir, 'temp_profile')
    shutil.copytree(original_profile, temp_profile, dirs_exist_ok=True)
    return temp_profile

# Caminho para o perfil do Chrome
user_data_dir = r'C:\Users\Danilo\AppData\Local\Google\Chrome\User Data'

profile_directory = 'Profile 5'
original_profile = os.path.join(user_data_dir, profile_directory)

# Criar uma cópia temporária do perfil
temp_profile = create_temp_profile(original_profile)

# Configurar as opções do Chrome
chrome_options = Options()
chrome_options.add_argument(f'user-data-dir={temp_profile}')
chrome_options.add_argument('--no-first-run')
chrome_options.add_argument('--no-default-browser-check')
chrome_options.add_argument('--no-service-autorun')
chrome_options.add_argument('--password-store=basic')

# Inicializar o driver do Chrome com as opções configuradas
service = Service(ChromeDriverManager().install())
driver = webdriver.Chrome(service=service, options=chrome_options)

try:
    # Exemplo: abrir um site
    driver.get('https://chatgpt.com/')
    
    # Seu código adicional aqui
    input("Pressione Enter para fechar o navegador...")
    
finally:
    # Fechar o navegador
    driver.quit()
    # Limpar o perfil temporário
    shutil.rmtree(temp_profile, ignore_errors=True)