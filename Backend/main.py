from fastapi import FastAPI
import psutil

app =   FastAPI()

@app.get("/stats")

def get_stats():
    return {
        "cpu_percent": psutil.cpu_percent(interval=1),
        "ram": psutil.virtual_memory()._asdict(),
        "disk": psutil.disk_usage("/")._asdict(),
        "net_io": psutil.net_io_counters()._asdict()
    }