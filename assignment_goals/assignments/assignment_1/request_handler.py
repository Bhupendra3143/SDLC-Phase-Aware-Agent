from datetime import datetime
from dataclasses import dataclass, asdict

from storage import load_requests, save_requests

@dataclass
class RequestClass:
    id: int
    description: str
    client: str
    project: str
    timestamp: str
    
    def description_validation(self, description: str) -> None:
        if not (10 <= len(description) <= 500):
            raise ValueError("Description must be in between 10 - 500 characters")
    
    def create_request(self):
        try:
            self.description_validation(self.description)
            data = load_requests()
            data.append(asdict(self))
            save_requests(data)
        
        except Exception as e:
            print(f"Couldn't save the request: {e}")