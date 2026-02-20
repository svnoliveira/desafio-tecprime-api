# API TecPrime

## Pré-requisitos
- [Docker](https://www.docker.com/get-started) e [Docker Compose](https://docs.docker.com/compose/install/) instalados

---

## Instalação

1. **Clone o repositório**
```bash
git clone <repositorio>
cd desafio-tecprime-api
```

2. **Configure as variáveis de ambiente**
```bash
cp .env.example .env
```
Edite o arquivo `.env` com suas configurações. Siga o exemplo do `.env.example`.

3. **Inicie os containers**
```bash
docker compose up --build
```

A API estará disponível em [http://localhost:8000](http://localhost:8000)

---

## Parar os containers

```bash
docker compose down        # para os containers (banco de dados preservado)
docker compose down -v     # para os containers e apaga o banco de dados
```

---

## Rotas disponíveis

> A documentação interativa completa com payloads e responses está disponível em:
> [http://localhost:8000/api/docs/](http://localhost:8000/api/docs/) *(requer servidor rodando)*

---

### 👤 Usuários

| Método | Rota | Descrição | Auth |
|--------|------|-----------|------|
| `POST` | [/api/register/](http://localhost:8000/api/register/) | Criação de usuário | ❌ |
| `POST` | [/api/login/](http://localhost:8000/api/login/) | Login | ❌ |
| `GET` | [/api/me/](http://localhost:8000/api/me/) | Busca usuário logado | ✅ |
| `GET` `POST` `PUT` `DELETE` | [/api/users/](http://localhost:8000/api/users/) | Gerenciamento de usuários | ✅ Admin |

---

### 🛍️ Produtos *(integração com [FakeStore API](https://fakestoreapi.com/products))*

| Método | Rota | Descrição | Auth |
|--------|------|-----------|------|
| `GET` | [/api/products/](http://localhost:8000/api/products/) | Lista todos os produtos | ❌ |
| `GET` | [/api/products/{id}/](http://localhost:8000/api/products/{id}/) | Busca produto por ID | ❌ |

Exemplo de retorno:
```json
[
  {
    "id": 1,
    "name": "Fjallraven - Foldsack No. 1 Backpack, Fits 15 Laptops",
    "price": 109.95,
    "image": "https://fakestoreapi.com/img/81fPKd-2AYL._AC_SL1500_t.png",
    "stock": 66
  }
]
```

> `stock` é um valor aleatório gerado pelo servidor (0–150), não vem da API externa.

---

### 🧾 Ordens de Compra

| Método | Rota | Descrição | Auth |
|--------|------|-----------|------|
| `GET` `POST` | [/api/orders/](http://localhost:8000/api/orders/) | Lista e cria ordens do usuário logado | ✅ |
| `GET` `PUT` `DELETE` | [/api/orders/{id}/](http://localhost:8000/api/orders/{id}/) | Detalha, edita ou deleta uma ordem | ✅ |



###  Decisões e comentários
> Escolha pelo Python Django se deu pela rapidez de desenvolvimento e maior familiaridade com a estrutura, optei por adicionar autenticação e utilizar os padrões mais atuais de validação, principalmente a questão dos tokens, que para maior segurança, foram desenvolvidos para receber, validar e retornar cookies, altamente compatível com autenticação no front-end NEXT.js, com isso não há trasnsmissão insegura de tokens e grande parte da requisição chega automáticamente, como o usuário. Tambem optei por não desenvolver uma rota com refresh, apenas por questão de tempo, apenas aumentando a vida do token e do cookie de autenticação, tambem excluí a validação de estoque, pois os dados não são reais e tambem por uma questão de tempo. A decisão pela build com docker foi pela maior facilidade em utilizar o Python, que não estava na lista de tecnologias frequentemente utilizada pela empresa, mas traria um ótimo resultado, um ponto a melhorar se houvessse mais tempo seria adicionar campo de valor no objeto de "order", par facilitar a listagem no front-end, rota de refresh para tokens e validação de estoque como mencionado anteriormente.
