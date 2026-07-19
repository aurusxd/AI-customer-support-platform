# AI Customer Support Platform

**AI Customer Support Platform** — проект интеллектуального ассистента для клиентской поддержки, который умеет не только отвечать на вопросы по базе знаний, но и выполнять реальные действия с помощью Tool Calling.


---

## О проекте

Обычный AI-бот чаще всего может только сформировать текстовый ответ.

Этот проект расширяет стандартную механику AI-поддержки:

```text
Сообщение пользователя
        │
        ▼
     AI-агент
        │
        ├── Ответ по базе знаний
        │
        └── Вызов инструмента
                │
                ▼
        База данных / API
                │
                ▼
        Результат действия
                │
                ▼
        Ответ пользователю
```

Например, ассистент может:

- ответить на вопрос по документации;
- проверить статус заказа;
- найти заказ пользователя;
- создать обращение в поддержку;
- изменить адрес доставки;
- оформить запрос на возврат;
- передать диалог оператору.

---

## Основные возможности

- AI-ассистент для клиентской поддержки;
- ответы по внутренней базе знаний;
- RAG-поиск по документам;
- Tool Calling;
- работа с заказами;
- создание обращений;
- история диалогов;
- сохранение контекста;
- REST API;
- авторизация пользователей;
- поддержка нескольких AI-моделей;
- запуск через Docker.

---

## Пример работы

### Ответ по базе знаний

```text
Пользователь:

Какие условия возврата товара?

AI-ассистент:

Товар можно вернуть в течение 14 дней после получения,
если сохранены его товарный вид и комплектация.
```

Для ответа агент находит нужную информацию во внутренней базе знаний.

---

### Проверка заказа

```text
Пользователь:

Где мой заказ №4821?
```

AI-агент определяет, что для ответа недостаточно базы знаний, и вызывает инструмент:

```python
get_order_status(order_id=4821)
```

Инструмент получает данные из системы заказов:

```json
{
  "order_id": 4821,
  "status": "Передан в службу доставки",
  "delivery_date": "2026-07-21"
}
```

После этого агент формирует естественный ответ:

```text
Ваш заказ №4821 передан в службу доставки.
Ориентировочная дата получения — 21 июля.
```

---

### Создание обращения

```text
Пользователь:

Мне пришёл повреждённый товар.
```

AI-агент может вызвать инструмент:

```python
create_support_ticket(
    category="damaged_product",
    description="Пользователь сообщил о повреждённом товаре"
)
```

После создания заявки пользователь получает подтверждение:

```text
Я создал обращение №1538.

Специалист поддержки свяжется с вами в ближайшее время.
```

---

## Доступные инструменты

В проекте планируется реализовать следующие инструменты:

```text
get_order_status
search_customer_orders
create_support_ticket
change_delivery_address
change_delivery_date
create_refund_request
get_customer_information
search_products
transfer_to_operator
```

Каждый инструмент представляет собой отдельный компонент с единым интерфейсом.

Пример базового класса:

```python
from abc import ABC, abstractmethod
from typing import Any


class BaseTool(ABC):
    name: str
    description: str

    @abstractmethod
    async def execute(self, **kwargs: Any) -> dict:
        pass
```

Благодаря этому новые действия можно добавлять без изменения основной логики AI-агента.

---

## RAG и база знаний

Для ответов на информационные вопросы используется подход RAG — Retrieval-Augmented Generation.

Система выполняет следующие шаги:

1. Получает сообщение пользователя.
2. Создаёт векторное представление запроса.
3. Находит подходящие фрагменты в базе знаний.
4. Передаёт найденный контекст AI-модели.
5. Формирует ответ на основе документов.

Поддерживаемые источники:

- PDF;
- TXT;
- Markdown;
- инструкции;
- FAQ;
- правила компании;
- документация;
- внутренние регламенты.

---

## Tool Calling

Tool Calling позволяет AI-модели выбирать и вызывать доступные функции.

Упрощённый пример:

```python
tools = [
    get_order_status,
    create_support_ticket,
    change_delivery_address,
]

response = await agent.process_message(
    message=user_message,
    tools=tools,
)
```

AI-агент сам определяет:

- достаточно ли обычного текстового ответа;
- нужен ли поиск по базе знаний;
- требуется ли вызов инструмента;
- какие аргументы необходимо передать;
- как объяснить результат пользователю.

---

## Архитектура

```text
Клиент
  │
  ▼
Frontend / Telegram Bot
  │
  ▼
FastAPI
  │
  ▼
AI Agent
  │
  ├── Conversation Memory
  │
  ├── RAG Service
  │      │
  │      ▼
  │   Vector Database
  │
  └── Tool Registry
         │
         ├── Orders Service
         ├── Support Service
         ├── Customer Service
         └── External APIs
                  │
                  ▼
              PostgreSQL
```

---

## Стек технологий

### Backend

- Python;
- FastAPI;
- SQLAlchemy;
- Alembic;
- PostgreSQL;
- Pydantic;
- Redis.

### Искусственный интеллект

- OpenAI API или другая совместимая LLM;
- Tool Calling;
- RAG;
- LangChain или собственная реализация;
- LangGraph;
- Qdrant или ChromaDB.

### Инфраструктура

- Docker;
- Docker Compose;
- Uvicorn;
- GitHub Actions.

### Интерфейс

В качестве клиентского интерфейса может использоваться:

- веб-приложение;
- Telegram-бот;
- REST API;
- виджет для сайта.

---

## Структура проекта

```text
ai-customer-support/
│
├── app/
│   ├── api/
│   │   ├── auth.py
│   │   ├── chat.py
│   │   ├── documents.py
│   │   └── orders.py
│   │
│   ├── agents/
│   │   ├── support_agent.py
│   │   ├── prompts.py
│   │   └── schemas.py
│   │
│   ├── tools/
│   │   ├── base.py
│   │   ├── registry.py
│   │   ├── orders.py
│   │   ├── tickets.py
│   │   └── customers.py
│   │
│   ├── rag/
│   │   ├── loader.py
│   │   ├── splitter.py
│   │   ├── embeddings.py
│   │   ├── retriever.py
│   │   └── vector_store.py
│   │
│   ├── memory/
│   │   └── conversation_memory.py
│   │
│   ├── services/
│   │   ├── order_service.py
│   │   ├── ticket_service.py
│   │   └── customer_service.py
│   │
│   ├── database/
│   │   ├── models/
│   │   ├── repositories/
│   │   ├── session.py
│   │   └── base.py
│   │
│   ├── core/
│   │   ├── config.py
│   │   ├── security.py
│   │   └── logging.py
│   │
│   └── main.py
│
├── documents/
├── migrations/
├── tests/
├── .env.example
├── docker-compose.yml
├── Dockerfile
├── requirements.txt
└── README.md
```

---

## Модели данных

Основные сущности проекта:

### User

```text
id
email
password_hash
created_at
```

### Customer

```text
id
name
email
phone
created_at
```

### Order

```text
id
customer_id
status
delivery_address
delivery_date
total_price
created_at
```

### Conversation

```text
id
customer_id
channel
created_at
updated_at
```

### Message

```text
id
conversation_id
role
content
created_at
```

### SupportTicket

```text
id
customer_id
conversation_id
category
description
status
created_at
```

### Document

```text
id
name
path
size
uploaded_at
```

---

## Установка

Клонируйте репозиторий:

```bash
git clone https://github.com/aurusxd/ai-customer-support.git
cd ai-customer-support
```

Создайте виртуальное окружение:

```bash
python -m venv .venv
```

Активируйте его.

Windows:

```bash
.venv\Scripts\activate
```

Linux или macOS:

```bash
source .venv/bin/activate
```

Установите зависимости:

```bash
pip install -r requirements.txt
```

---

## Настройка окружения

Создайте файл `.env` на основе примера:

```bash
cp .env.example .env
```

Пример конфигурации:

```env
APP_NAME=AI Customer Support Platform
DEBUG=true

DATABASE_URL=postgresql+asyncpg://postgres:postgres@localhost:5432/support_ai
REDIS_URL=redis://localhost:6379/0

LLM_API_KEY=your_api_key
LLM_MODEL=gpt-4.1-mini

VECTOR_DB_URL=http://localhost:6333
VECTOR_COLLECTION=support_documents

JWT_SECRET_KEY=change_me
JWT_ALGORITHM=HS256
```

---

## Запуск проекта

Запуск базы данных и дополнительных сервисов:

```bash
docker compose up -d
```

Применение миграций:

```bash
alembic upgrade head
```

Запуск API:

```bash
uvicorn app.main:app --reload
```

После запуска документация API будет доступна по адресу:

```text
http://localhost:8000/docs
```

---

## Запуск через Docker

```bash
docker compose up --build
```

---

## Тестирование

Для запуска тестов:

```bash
pytest
```

Для запуска с отображением покрытия:

```bash
pytest --cov=app
```

---

## API

Основные маршруты:

```text
POST   /api/auth/register
POST   /api/auth/login

POST   /api/chat/messages
GET    /api/conversations
GET    /api/conversations/{conversation_id}

POST   /api/documents
GET    /api/documents
DELETE /api/documents/{document_id}

GET    /api/orders/{order_id}
POST   /api/tickets
```

---

## Безопасность

Особое внимание необходимо уделить инструментам, которые изменяют данные.

AI-агент не должен бесконтрольно выполнять критические операции.

Для опасных действий рекомендуется использовать подтверждение:

```text
Пользователь:

Отмени заказ №4821.

Ассистент:

Заказ №4821 будет отменён.
Подтвердите выполнение операции.
```

Только после подтверждения вызывается соответствующий инструмент.

Также рекомендуется:

- проверять права пользователя;
- валидировать аргументы инструментов;
- ограничивать доступные функции;
- сохранять историю вызовов;
- вести журнал действий;
- разделять информационные и изменяющие операции.

## Планы по развитию

- [ ] Базовый AI-чат
- [ ] Интеграция с LLM
- [ ] RAG-поиск по документам
- [ ] Загрузка PDF, TXT и Markdown
- [ ] История диалогов
- [ ] Сохранение контекста
- [ ] Реестр инструментов
- [ ] Проверка статуса заказа
- [ ] Создание обращений
- [ ] Изменение адреса доставки
- [ ] Перенос даты доставки
- [ ] Оформление запроса на возврат
- [ ] Подтверждение критических действий
- [ ] Передача диалога оператору
- [ ] Telegram-бот
- [ ] Виджет для сайта
- [ ] Панель администратора
- [ ] Аналитика обращений
- [ ] Интеграция с CRM и внешними API


## Статус проекта

Проект находится в разработке.

Функциональность и архитектура могут изменяться по мере добавления новых возможностей.


## Лицензия

Проект распространяется под лицензией MIT.