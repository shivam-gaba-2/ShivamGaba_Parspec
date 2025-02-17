from fastapi import APIRouter
from app.database import get_db_connection
from app.queries import Queries

router = APIRouter(prefix="/metrics", tags=["metrics"])

@router.get("/")
def get_metrics():
    conn = get_db_connection()
    cursor = conn.cursor()
    
    cursor.execute(Queries.GET_TOTAL_ORDERS)
    total_orders = cursor.fetchone()[0]
    
    cursor.execute(Queries.GET_PENDING_ORDERS)
    pending_orders = cursor.fetchone()[0]
    
    cursor.execute(Queries.GET_PROCESSING_ORDERS)
    processing_orders = cursor.fetchone()[0]
    
    cursor.execute(Queries.GET_COMPLETED_ORDERS)
    completed_orders = cursor.fetchone()[0]
    
    cursor.execute(Queries.GET_AVG_PROCESSING_TIME)
    avg_processing_time = cursor.fetchone()[0]
    
    conn.close()
    
    return {
        "total_orders": total_orders,
        "pending_orders": pending_orders,
        "processing_orders": processing_orders,
        "completed_orders": completed_orders,
        "average_processing_time": avg_processing_time if avg_processing_time else 0
    }
