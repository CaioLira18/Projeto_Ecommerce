# Projeto_Ecommerce

- Bem-vindo ao repositório do projeto eCommerce! Este projeto é uma aplicação web desenvolvida utilizando Django e Python, que implementa um sistema de comércio eletrônico completo com diversas funcionalidades.

# Funcionalidades
## Autenticação de Usuário:
- Login: Os usuários podem fazer login em suas contas utilizando um nome de usuário e senha.
- Logout: Os usuários podem fazer logout de suas contas.
- Criar Conta: Os usuários podem criar novas contas fornecendo os detalhes necessários.
  
## Carrinho de Compras:
- Adicionar Itens: Os usuários podem adicionar itens de diferentes tipos e modelos ao carrinho de compras.
- Remover Itens: Os usuários podem retirar itens do carrinho de compras.

## Pedidos
- Consultar Pedidos: Os usuários podem consultar seus pedidos, visualizando detalhes como valor unitário, variação, quantidade e valor total.
  
## Gerenciamento de Perfil
- Atualizar Informações do Usuário: Os usuários podem atualizar suas informações de perfil, como nome, endereço e outros detalhes pessoais.
  
## Validação de CPF
- CPF Único e Válido: O sistema valida se o CPF fornecido é único e válido dentro do banco de dados.

# Uso
## Após iniciar o servidor, você pode acessar a aplicação no navegador através do endereço http://127.0.0.1:8000/. A partir daí, você poderá:
- Criar uma nova conta ou fazer login em uma conta existente.
- Adicionar itens ao carrinho de compras.
- Consultar e gerenciar seus pedidos.
- Atualizar suas informações de perfil.
- Utilizar a funcionalidade de validação de CPF ao criar ou atualizar uma conta.

  
# Estrutura do Projeto
loja/: Aplicação responsável pelo gerenciamento da estrutura da loja.
midia/: Pasta com as Imagens dos Produtos
pedidos/: Aplicação responsável pelo gerenciamento de pedidos.
produtos/: Aplicação responsável pelo gerenciamento de pedidos.
perfil/: Aplicação responsável pela autenticação e gerenciamento de usuários.
templates/: Diretório contendo os templates HTML.
utils/: Diretório contendo os arquivos de validação/formatação
static/: Diretório contendo arquivos estáticos (CSS, JavaScript, imagens).

# Como Configurar o Projeto:
Abaixo uma lista de comandos para clonar e configurar este projeto na sua 
máquina local:

- Instalar git (Windows, Linux e Mac) e depois:

```
git clone https://github.com/luizomf/django-simple-ecommerce.git
```

- Para **Windows**:

```
cd django-simple-ecommerce
python -m venv venv
venv\Scripts\activate.bat
python -m pip install --upgrade pip setuptools wheel --user
python -m pip install django django-debug-toolbar django-crispy-forms pillow
python manage.py migrate
```

- Para **Linux**:

```
cd django-simple-ecommerce
python3.7 -m venv venv
. venv/bin/activate
pip install django django-debug-toolbar django-crispy-forms pillow
python manage.py migrate
```

- Para **Mac**

```
cd django-simple-ecommerce
python -m venv venv
. venv/bin/activate
pip install django django-debug-toolbar django-crispy-forms pillow
python manage.py migrate
```
