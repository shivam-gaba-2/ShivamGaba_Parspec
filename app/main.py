from fastapi import FastAPI
from app.api import metrics, orders
from app.services.queue_service import OrderQueueService
from app.database import init_db

app = FastAPI(title="Order Processing API")

order_queue_service = OrderQueueService()

@app.on_event("startup")
def startup_event():
    init_db()

app.include_router(orders.router)
app.include_router(metrics.router)
