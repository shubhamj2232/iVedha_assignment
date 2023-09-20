# iVedha_assignment
----------------------------------------------------------------------------------------------------------------------------------------------------------------------------
#Problem 1.1 - Service Monitoring Script

This Python script is designed to monitor the status of specific services on a host machine and create a JSON report containing the application's status, service statuses, and host information.

## Usage

1. **Prerequisites**:
   - Python 3.x installed on your system.
   - The `psutil` library for process management. You can install it using `pip install psutil`.

2. **Customization**:
   - Open the script (`service_monitor.py`) in a text editor.
   - Modify the `application_name` variable to match your application's name.
   - Customize the `services_to_monitor` list to include the services you want to monitor.

3. **Running the Script**:
   - Open a terminal/command prompt.
   - Navigate to the directory containing the script.
   - Run the script using the following command:
     ```
     python service_monitor.py
     ```

4. **Output**:
   - The script will create a JSON file with a name like `application_name-application_status-timestamp.json` in the same directory as the script.
   - The JSON file will contain information about the application's status, service statuses, and the host name.

## Example

Suppose you want to monitor an application named "MyApp" that relies on the services "httpd," "rabbitMQ," and "postgreSQL." After customizing the script, run it to generate a JSON report file.

## JSON Report

Here is an example of the JSON report structure:

json
{
    "application_name": "MyApp",
    "application_status": "UP",
    "host_name": "your_host_name",
    "httpd": "UP",
    "rabbitMQ": "DOWN",
    "postgreSQL": "UP"
}

----------------------------------------------------------------------------------------------------------------------------------------------------------------------------
#Problem 1.2 - Elasticsearch Health Monitoring with Flask

This Python Flask application allows you to add and query application health status data in Elasticsearch. It provides endpoints for adding data and checking the overall health status of applications or specific services.

## Prerequisites

Before running the application, ensure you have the following:

1. **Python and Flask**:
   - Python installed on your system.
   - Flask installed. You can install it using `pip install Flask`.

2. **Elasticsearch**:
   - Elasticsearch installed and running. Make sure to configure the Elasticsearch server's address in the `app.py` file.

## Usage

1. **Configuration**:
   - Open the `app.py` file in a text editor.
   - Modify the Elasticsearch server's address in the `es = Elasticsearch(hosts=["http://localhost:9200"])` line to match your Elasticsearch server's address.

2. **Running the Flask Application**:
   - Open a terminal or command prompt.
   - Navigate to the directory containing `app.py`.
   - Run the Flask application using the following command:
     ```
     python app.py
     ```

3. **Endpoints**:

   - **Add Application Status**:
     - URL: `/add`
     - Method: POST
     - Example Request Body:
       ```json
       {
           "application_name": "MyApp",
           "application_status": "UP",
           "service_name": "ServiceA"
       }
       ```
     - This endpoint allows you to add application status data to Elasticsearch.

   - **Check Overall Health**:
     - URL: `/healthcheck`
     - Method: GET
     - Returns "UP" if all application statuses are "UP," or "DOWN" if any application is "DOWN."

   - **Check Service Health**:
     - URL: `/healthcheck/<service_name>`
     - Method: GET
     - Replace `<service_name>` with the name of the service you want to check.
     - Returns "UP" if the specified service is "UP," or "DOWN" if it's "DOWN."

4. **Response**:
   - Successful requests return status codes 200 (OK) or 201 (Created), along with appropriate messages.
   - Errors return status code 500 (Internal Server Error) along with an error message.

5. **Example**:
   - You can use tools like `curl` or Postman to make POST and GET requests to the endpoints defined in the Flask application.
  
----------------------------------------------------------------------------------------------------------------------------------------------------------------------------
#Problem 2.1 - Ansible Inventory Configuration

This Ansible inventory configuration defines groups of servers for managing and orchestrating tasks using Ansible. Ansible uses this inventory to understand which servers to work with and how to categorize them.

## Inventory Structure

The inventory is divided into groups, each representing a specific category of servers. Here's an explanation of the groups defined in this inventory:

### [web_servers]

This group contains servers that are designated as web servers. These servers are responsible for hosting web applications or websites. The inventory lists one example server with its hostname and IP address.

Example:
```ini
[web_servers]
host1 ansible_host=host1.example.com
```
**Usage** 
**Ansible Configuration:** 
- Ensure that you have Ansible installed on your control machine. 
- Create an Ansible playbook or role to perform tasks on the defined server groups. 

**Inventory File**
- Save the inventory configuration into a separate inventory file, e.g., inventory.ini. Update the hostname and IP addresses in the inventory to match your actual server infrastructure. 

**Running Ansible Playbook** 
- You can use this inventory with Ansible playbooks to automate tasks on the defined server groups.

**Command**
 - ansible-playbook -i inventory.ini your_playbook.yml
----------------------------------------------------------------------------------------------------------------------------------------------------------------------------
#Problem 2.2 - **Ansible Playbook for Performing Actions**

This Ansible playbook is designed to perform various actions on a group of hosts based on the value of the provided variable "action." Depending on the action, it can verify and install an HTTPD service, check disk space, send an email alert, check the status of an application, and display the results.

## Usage

1. **Prerequisites**:
   - Ensure that Ansible is installed on your control machine.

2. **Inventory**:
   - Make sure you have an Ansible inventory file (`hosts.ini`) that defines the hosts on which you want to perform these actions. You can adjust the inventory file to include the target hosts.

3. **Customization**:
   - Edit the playbook (`perform_actions.yml`) as needed.
   - Customize the `hosts` line in the playbook to specify the hosts or host groups on which you want to perform these actions.
   - Modify the tasks to suit your specific use case.

4. **Action Variable**:
   - You need to provide the `action` variable when running the playbook to specify which action to perform. For example:
     ```
     ansible-playbook -i hosts.ini perform_actions.yml -e "action=verify_install"
     ```

5. **Actions**:

   - **Verify and Install HTTPD Service**:
     - This action verifies and installs the HTTPD service on the specified host (`host1`) if the `action` variable is set to "verify_install."

   - **Check Disk Space and Send Alert**:
     - This action checks the disk space on all hosts (`all`), registers the output, and sends an email alert if disk usage is above 80%. Use `action=check-disk` to trigger this action.

   - **Check Application Status**:
     - This action checks the status of an application ("rbcapp1") by sending an HTTP request and displays the results. Use `action=check-status` to trigger this action.

6. **Running the Playbook**:
   - Open a terminal or command prompt.
   - Run the playbook with the desired action, as shown in the examples above.

7. **Results**:
   - Depending on the action, the playbook will execute specific tasks and provide relevant output on the terminal.

8. **Customization**:
   - You can extend and modify the playbook tasks to perform other actions or interact with different services based on your needs.

## Example

Suppose you have a group of servers where you need to monitor disk space, verify the installation of HTTPD, check the status of an application, and perform related actions. You can use this playbook with the respective action variable to automate these tasks.

----------------------------------------------------------------------------------------------------------------------------------------------------------------------------
#Problem 3 - **CSV Data Filtering Script**

This Python script reads data from a CSV file, calculates the average price per square foot, filters the data based on a condition, and saves the filtered data to a new CSV file.

## Usage

1. **Input Data**:
   - Ensure you have the input CSV file (`assignment data.csv`) containing data with columns `price` and `sq_ft`. Modify the script to match your input data file if needed.

2. **Running the Script**:
   - Open a terminal or command prompt.
   - Navigate to the directory containing the script.
   - Run the script using the following command:
     ```
     python script.py
     ```

3. **Output Data**:
   - The script will calculate the average price per square foot for the valid data points in the input file.
   - It will then filter the data and retain only the rows where the price per square foot is less than the calculated average.
   - The filtered data will be saved to a new CSV file named `output.csv` in the same directory.

4. **Customization**:
   - You can modify the input file path (`input_file`) and the output file path (`output_file`) in the script to match your file locations.
   - Adjust the script if your CSV file has different column names or data types.

5. **CSV File Format**:
   - Ensure that the input CSV file has the following columns: `price` (numeric) and `sq__ft` (numeric).
   - Rows with invalid or missing values for these columns will be skipped.

## Example

Suppose you have a CSV file containing real estate data with property prices and square footage. You can use this script to filter out properties with a price per square foot below the calculated average, helping you identify potential outliers or anomalies in the dataset.
