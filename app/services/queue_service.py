import queue
import threading
from app.database import get_db_connection
from app.queries import Queries

class OrderQueueService:
    def __init__(self):
        self.order_queue = queue.Queue()
        self.processing_thread = threading.Thread(target=self.process_orders, daemon=True)
        self.processing_thread.start()

    def add_order_to_queue(self, order_id):
        self.order_queue.put(order_id)

    def process_orders(self):
        while True:
            order_id = self.order_queue.get()
            try:
                conn = get_db_connection()
                cursor = conn.cursor()
                cursor.execute(Queries.UPDATE_ORDER_STATUS, ("Completed", order_id))
                conn.commit()
                conn.close()
                self.order_queue.task_done()
            except Exception as e:
                print(f"Error processing order {order_id}: {e}")
