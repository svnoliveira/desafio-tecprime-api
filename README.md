# API TecPrime

### Pré-requisitos

- Docker e Docker Compose instalados

### Instalação

1. **Clone o repositório**

```bash
git clone <repositorio>
cd desafio-tecprime-api
```

2. **Configure as variáveis de ambiente**

```bash
cp .env.example .env
```

Edite o arquivo `.env` com suas configurações necessárias. (Siga o exemplo do arquivo .env.example)

3. **Inicie os containers**

```bash
docker compose up --build
```

A API estará disponível em `http://localhost:8000/`

### Parar os containers

```bash
docker compose down
```

### Rotas disponíveis

Documentação de rotas, formatos de payload e response:
(apenas com servidor rodando)

```bash
http://localhost:8000/api/docs/
```

Lista simplificada de rotas:

```bash
//POST - Rota de criação de usuário padrão.
http://localhost:8000/api/register/

//POST - Rota de login.
http://localhost:8000/api/login/

//GET - Rota de busca de usuário logado.
http://localhost:8000/api/me/



//POST/GET/PUT/DELETE - Rota de criação, listagem, edição e delete de usuário autenticado/administrador.
http://localhost:8000/api/users/

//GET - Rota integrada com API externa, https://fakestoreapi.com/products
http://localhost:8000/api/products/
exemplo de retorno (não contém em api/docs/):
[
	{
		"id": 1,
		"name": "Fjallraven - Foldsack No. 1 Backpack, Fits 15 Laptops",
		"price": 109.95,
		"image": "https://fakestoreapi.com/img/81fPKd-2AYL._AC_SL1500_t.png",
		"stock": 66
	},
]
//GET - pesquisa de produto externo por ID
/api/products/{product_id}/

//POST/GET/PUT/DELETE - Rota de criação, listagem, edição e delete de ordens de compra para usuários autenticados/administrador.
http://localhost:8000/api/orders/


```

---
