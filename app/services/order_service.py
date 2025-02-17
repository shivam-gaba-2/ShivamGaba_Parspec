from app.database import get_db_connection
from app.queries import Queries
from fastapi import HTTPException

class OrderService:
    @staticmethod
    def create_order(order):
        conn = get_db_connection()
        cursor = conn.cursor()

        # Check if order_id already exists
        cursor.execute(Queries.CHECK_ORDER_EXISTS, (order.order_id,))
        if cursor.fetchone():
            conn.close()
            raise HTTPException(status_code=400, detail="Order with this ID already exists")

        # Insert new order
        cursor.execute(Queries.INSERT_ORDER, (order.order_id, order.user_id, ",".join(order.item_ids), order.total_amount, "Pending"))
        conn.commit()
        conn.close()

        return {"message": "Order received", "order_id": order.order_id}

    @staticmethod
    def get_order_status(order_id):
        conn = get_db_connection()
        cursor = conn.cursor()
        cursor.execute(Queries.GET_ORDER_STATUS, (order_id,))
        order = cursor.fetchone()
        conn.close()

        if order:
            return {"order_id": order_id, "status": order[0]}
        else:
            raise HTTPException(status_code=404, detail="Order not found")
