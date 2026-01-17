import json
from pathlib import Path
import os

DATA_FILE = Path("data/requests.json")

def load_requests():
    if not os.path.exists(DATA_FILE) or os.path.getsize(DATA_FILE) == 0:
        DATA_FILE.parent.mkdir(exist_ok=True, parents=True)
        DATA_FILE.write_text("[]")
    return json.loads(DATA_FILE.read_text())

def save_requests(data):
    DATA_FILE.write_text(json.dumps(data, indent=4))
    
def get_requests_number():
    if not os.path.exists(DATA_FILE) or os.path.getsize(DATA_FILE) == 0:
        return 0
    data = json.load(open(DATA_FILE, 'r'))
    return len(data)