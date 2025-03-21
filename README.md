# Car Management

## 🚗 Sobre o projeto
O **Car Management** é um sistema desenvolvido em **Python/Django** para gerenciar informações de carros, incluindo cadastro, edição e remoção de veículos.
Este projeto também integra a **API da OpenAI** para fornecer recursos avançados, como recomendações inteligentes e automação de tarefas administrativas.

O sistema foi desenvolvido com **HTML, CSS e JavaScript** para a interface do usuário e foi implantado na **AWS EC2** para garantir escalabilidade e desempenho.

## 📌 Funcionalidades
✅ Cadastro, edição e remoção de carros 
✅ Filtros e pesquisa de veículos
✅ Interface responsiva para melhor experiência do usuário

## 🛠 Tecnologias Utilizadas
- **Python 3.x**
- **Django**
- **SQLite / PostgreSQL
- **OpenAI API** (para funcionalidades de IA)
- **HTML, CSS e JavaScript** (para interface do usuário)
- **AWS EC2** (para deploy e hospedagem)

## 📦 Instalação e Configuração
### 1. Clone o repositório
```bash
git clone https://github.com/deivides/carros.git
```

### 2. Crie um ambiente virtual
```bash
python -m venv venv
source venv/bin/activate  # Linux/Mac
venv\Scripts\activate  # Windows
```

### 3. Instale as dependências
```bash
pip install -r requirements.txt
```

### 4. Configure a API da OpenAI
Crie um arquivo `.env` e adicione sua chave de API:
```bash
OPENAI_API_KEY="sua-chave-aqui"
```

### 5. Execute as migrações do banco de dados
```bash
python manage.py migrate
```

### 6. Inicie o servidor local
```bash
python manage.py runserver
```
Acesse o projeto em: [http://127.0.0.1:8000](http://127.0.0.1:8000)



