from fastapi import APIRouter
from app.schema import OrderCreate
from app.services.order_service import OrderService
from app.services.queue_service import OrderQueueService

router = APIRouter(prefix="/orders", tags=["orders"])
queue_service = OrderQueueService()

@router.post("/")
def create_order(order: OrderCreate):
    response = OrderService.create_order(order)
    queue_service.add_order_to_queue(order.order_id)
    return response

@router.get("/{order_id}")
def get_order_status(order_id: str):
    return OrderService.get_order_status(order_id)
