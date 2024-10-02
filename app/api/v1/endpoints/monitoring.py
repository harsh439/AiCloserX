from fastapi import APIRouter, HTTPException
from typing import List, Optional
from datetime import datetime

router = APIRouter()

# In-memory storage for error logs, system metrics, and alerts
error_logs = []
active_alerts = []

# Endpoint 1: Get System Metrics (e.g., CPU, memory, response times)
@router.get("/system-metrics", response_model=dict)
async def get_system_metrics():
    """
    Retrieves key system performance metrics such as CPU usage, memory usage, and response times.
    """
    # Simulated system metrics
    system_metrics = {
        "cpu_usage": "60%",
        "memory_usage": "2.5 GB",
        "response_time": {
            "avg_response_time": "1.2s",
            "max_response_time": "3.5s",
            "min_response_time": "0.5s"
        },
        "uptime": "99.98%"
    }
    return system_metrics

# Endpoint 2: Get AI Model Metrics
@router.get("/ai-metrics", response_model=dict)
async def get_ai_metrics():
    """
    Retrieves performance metrics specific to the AI model, such as accuracy, confidence scores, and latency.
    """
    # Simulated AI model metrics
    ai_metrics = {
        "avg_response_time": "1.1s",
        "max_response_time": "2.8s",
        "min_response_time": "0.7s",
        "avg_confidence_score": 0.87,
        "accuracy": 0.92,
        "inference_errors": 5
    }
    return ai_metrics

# Endpoint 3: Get Historical Model Performance
@router.get("/model-performance", response_model=dict)
async def get_model_performance(start_time: str, end_time: str):
    """
    Retrieves historical performance data of the AI model, including accuracy, confidence scores, and response time.
    """
    # Simulated model performance metrics for the given time window
    historical_metrics = {
        "model_version": "v1.4",
        "metrics": [
            {
                "timestamp": "2023-09-21T12:00:00Z",
                "accuracy": 0.93,
                "confidence_score": 0.88,
                "response_time": "1.0s"
            },
            {
                "timestamp": "2023-09-21T13:00:00Z",
                "accuracy": 0.91,
                "confidence_score": 0.86,
                "response_time": "1.1s"
            }
        ]
    }
    return historical_metrics

# Endpoint 4: Report an Error
@router.post("/error/report", response_model=dict)
async def report_error(error_type: str, session_id: str, component: str, error_message: str):
    """
    Reports an error from any component of the system, including details about what went wrong.
    """
    error_id = f"error_{len(error_logs) + 1}"
    timestamp = datetime.utcnow().isoformat()
    error_entry = {
        "error_id": error_id,
        "error_type": error_type,
        "session_id": session_id,
        "component": component,
        "error_message": error_message,
        "timestamp": timestamp
    }
    error_logs.append(error_entry)
    return {
        "status": "error_reported",
        "error_id": error_id,
        "timestamp": timestamp
    }

# Endpoint 5: Get Error Logs
@router.get("/error/logs", response_model=dict)
async def get_error_logs(start_time: Optional[str] = None, end_time: Optional[str] = None, error_type: Optional[str] = None):
    """
    Retrieves error logs filtered by time period, error type, or component.
    """
    # Filter error logs by time range and error type
    filtered_logs = [log for log in error_logs]
    return {
        "error_logs": filtered_logs
    }

# Endpoint 6: Create an Alert
@router.post("/error/alert", response_model=dict)
async def create_alert(alert_name: str, metric: str, threshold: float, notification_method: str, email: Optional[str] = None):
    """
    Creates an alert when certain thresholds (e.g., high CPU usage) are exceeded.
    """
    alert_id = f"alert_{len(active_alerts) + 1}"
    alert_entry = {
        "alert_id": alert_id,
        "alert_name": alert_name,
        "metric": metric,
        "threshold": threshold,
        "notification_method": notification_method,
        "email": email
    }
    active_alerts.append(alert_entry)
    return {
        "status": "alert_created",
        "alert_id": alert_id
    }

# Endpoint 7: Get Active Alerts
@router.get("/monitoring/alerts", response_model=dict)
async def get_active_alerts():
    """
    Retrieves a list of active alerts, including performance metrics or errors that have crossed predefined thresholds.
    """
    return {
        "active_alerts": active_alerts
    }

# Endpoint 8: Get Resource Usage (e.g., disk space, network bandwidth)
@router.get("/resource-usage", response_model=dict)
async def get_resource_usage():
    """
    Tracks resource usage such as disk space, network bandwidth, and database query rates.
    """
    # Simulated resource usage
    resource_usage = {
        "disk_space_used": "120 GB",
        "network_bandwidth": "450 Mbps",
        "database_query_rate": "50 queries/sec"
    }
    return resource_usage
