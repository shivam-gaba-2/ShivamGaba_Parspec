class Queries:
    CREATE_ORDERS_TABLE = """
        CREATE TABLE IF NOT EXISTS orders (
            order_id TEXT PRIMARY KEY,
            user_id TEXT,
            item_ids TEXT,
            total_amount REAL,
            status TEXT,
            created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
            processed_at TIMESTAMP
        )
    """
    INSERT_ORDER = "INSERT INTO orders (order_id, user_id, item_ids, total_amount, status) VALUES (?, ?, ?, ?, ?)"
    CHECK_ORDER_EXISTS = "SELECT 1 FROM orders WHERE order_id=?"
    GET_ORDER_STATUS = "SELECT status FROM orders WHERE order_id=?"
    UPDATE_ORDER_STATUS = "UPDATE orders SET status=?, processed_at=CURRENT_TIMESTAMP WHERE order_id=?"
    GET_TOTAL_ORDERS = "SELECT COUNT(*) FROM orders"
    GET_PENDING_ORDERS = "SELECT COUNT(*) FROM orders WHERE status='Pending'"
    GET_PROCESSING_ORDERS = "SELECT COUNT(*) FROM orders WHERE status='Processing'"
    GET_COMPLETED_ORDERS = "SELECT COUNT(*) FROM orders WHERE status='Completed'"
    GET_AVG_PROCESSING_TIME = """
        SELECT AVG((julianday(processed_at) - julianday(created_at)) * 86400) FROM orders WHERE processed_at IS NOT NULL
    """
