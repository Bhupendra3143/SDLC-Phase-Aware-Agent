from analytics import analyze_requests
from request_handler import RequestClass
from storage import get_requests_number, load_requests
from datetime import datetime
from zoneinfo import ZoneInfo

def main():
    while True:
        choice = int(
            input(
"""
--------------------------------------------
            WELCOME TO THE AGENT
--------------------------------------------
What would you like to do??
1) Add request
2) View requests
3) Exit
4) Analyze requests

Enter your choice : 
"""
            )
        )
        match choice:
            case 1:
                try:
                    length = get_requests_number()
                    id = length + 1
                    description = input("Enter description: ")
                    client = input("Enter client: ")
                    project = input("Enter project: ")
                    timestamp = datetime.now(ZoneInfo("Asia/Kolkata")).isoformat()
                    request = RequestClass(
                        id = id,
                        description=description,
                        client=client,
                        project=project,
                        timestamp=timestamp
                    )
                    request.create_request()
                    print("\nRequest added successfully...")
                
                except:
                    print("An error occured...")
                    break
            case 2:
                data = load_requests()
                for info in data:
                    print(f"""
------------------------------------------------------------------------
   Description - {info["description"]} Project - {info["project"]}    
________________________________________________________________________
""")
            
            case 3:
                break
            
            case 4:
                analyze_requests()
            
                
                

if __name__ == "__main__":
    main()