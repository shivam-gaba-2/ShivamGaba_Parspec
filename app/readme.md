# Order Processing Backend System

This is a backend system designed to manage and process orders for an e-commerce platform. It provides APIs for order management, processing, and reporting key metrics.

## Features
- **Create Orders**: Accepts orders with fields such as `order_id`, `user_id`, `item_ids`, and `total_amount`.
- **Order Status**: Allows querying the status of an order (`Pending`, `Processing`, `Completed`).
- **Metrics**: Provides key metrics like the total number of orders, average processing time, and the count of orders in each status.

## Run the application

   Start the FastAPI application:
   ```bash
   uvicorn app.main:app --reload
   ```
   This will start the app at `http://127.0.0.1:8000`.

### Example API Requests and Responses

#### 1. Create an Order (POST /orders/)
Create a new order with the following details:

**Request**:
```bash
curl -X 'POST' \
  'http://127.0.0.1:8000/orders/' \
  -H 'Content-Type: application/json' \
  -d '{
  "order_id": "12345",
  "user_id": "user_1",
  "item_ids": ["item_1", "item_2"],
  "total_amount": 29.99
}'
```

**Response**:
```json
{
  "message": "Order received",
  "order_id": "12345"
}
```

#### 2. Get Order Status (GET /orders/{order_id})
Retrieve the status of an order by its `order_id`.

**Request**:
```bash
curl -X 'GET' 'http://127.0.0.1:8000/orders/12345'
```

**Response**:
```json
{
  "order_id": "12345",
  "status": "Pending"
}
```

#### 3. Get Metrics (GET /metrics/)
Fetch key metrics about the orders in the system.

**Request**:
```bash
curl -X 'GET' 'http://127.0.0.1:8000/metrics/'
```

**Response**:
```json
{
  "total_orders": 100,
  "pending_orders": 50,
  "processing_orders": 30,
  "completed_orders": 20,
  "average_processing_time": 12.5
}
```

## Design Decisions and Trade-offs

### 1. **Queue Handling**:
   - We use an in-memory `queue.Queue` to simulate asynchronous order processing. This is a simple solution that works well for the current scope but may need to be replaced with a more scalable solution like Redis or RabbitMQ in a production setting for handling high volumes of requests.

### 2. **Database**:
   - The system uses SQLite for simplicity and ease of setup. SQLite is appropriate for development and low to moderate traffic systems. However, for higher concurrency and scalability, switching to PostgreSQL or MySQL would be ideal.

### 3. **Concurrency**:
   - The order processing uses Python’s `threading` module. While this is sufficient for simulating concurrent order processing in a single machine, it’s important to note that this approach may not scale well for a highly concurrent distributed system. For better scalability, a distributed task queue like Celery could be used.

## Assumptions Made During Development
- **SQLite as a Database**: The use of SQLite is chosen for simplicity. In a production environment, a more robust database like PostgreSQL or MySQL would be recommended.
- **Thread-based Queue Processing**: For simulating order processing, the system uses Python's `threading` library. While this is adequate for the assignment’s scope, for high concurrency, a more advanced queuing mechanism (like Redis) or an asynchronous task queue (e.g., Celery)