import psutil, socket, json
from datetime import datetime

def check_service_status(service_name):
    for process in psutil.process_iter(attrs=['name']):
        if service_name in process.info['name']:
            return "UP"
    return "DOWN"

def create_json_file(json_payload):
    # Get the current timestamp
    timestamp = datetime.now().strftime("%Y-%m-%d_%H-%M")

    # Define the file name
    file_name = f"{json_payload['application_name']}-{json_payload['application_status']}-{timestamp}.json"

    # Write the JSON payload to the file
    with open(file_name, 'w') as json_file:
        json.dump(json_payload, json_file, indent=4)

def main():
    # Define the list of services to monitor
    application_name = "rbcapp1"
    services_to_monitor = ["httpd", "rabbitMQ", "postgreSQL"]

    # Get the host name
    host_name = socket.gethostname()

    # Create a dictionary to store the service statuses
    service_statuses = {}

    # Check the status of each service
    for service_name in services_to_monitor:
        service_status = check_service_status(service_name)
        service_statuses[service_name] = service_status

    # Determine the application status
    application_status = "UP" if all(status == "UP" for status in service_statuses.values()) else "DOWN"

    # Create a JSON object
    json_payload = {
        "application_name": application_name,
        "application_status": application_status,
        "host_name": host_name
    }

    # Store the json contents in a json format file
    create_json_file(json_payload)

if __name__ == "__main__":
    main()
