#!/usr/bin/python3
"""
Exports TODO list data for a given employee ID to a CSV file using a REST API.
"""

import csv
import requests
import sys

def export_to_csv(employee_id):
    """
    Fetches TODO list data for a given employee ID and exports it to a CSV file.

    :param employee_id: The ID of the employee.
    :type employee_id: int
    :return: None
    """
    base_url = "https://jsonplaceholder.typicode.com"

    # Fetch employee details
    user_response = requests.get(f"{base_url}/users/{employee_id}")
    user_data = user_response.json()
    username = user_data.get("username")

    # Fetch employee's TODO list
    todos_response = requests.get(f"{base_url}/todos", params={"userId": employee_id})
    todos_data = todos_response.json()

    # Define CSV file name
    csv_file_name = f"{employee_id}.csv"

    # Write data to CSV file
    with open(csv_file_name, mode="w", newline='', encoding='utf-8') as csv_file:
        writer = csv.writer(csv_file, quoting=csv.QUOTE_ALL)
        for task in todos_data:
            user_id = employee_id
            task_title = task.get("title")
            task_completed = task.get("completed")
            writer.writerow([user_id, username, task_completed, task_title])

    print(f"Data exported to {csv_file_name}")

if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: ./1-export_to_CSV.py <employee_id>")
    else:
        try:
            employee_id = int(sys.argv[1])
            export_to_csv(employee_id)
        except ValueError:
            print("Please provide a valid integer as employee ID.")#!/usr/bin/python3
"""
Exports TODO list data for a given employee ID to a CSV file using a REST API.
"""

import csv
import requests
import sys

def export_to_csv(employee_id):
    """
    Fetches TODO list data for a given employee ID and exports it to a CSV file.

    :param employee_id: The ID of the employee.
    :type employee_id: int
    :return: None
    """
    base_url = "https://jsonplaceholder.typicode.com"

    # Fetch employee details
    user_response = requests.get(f"{base_url}/users/{employee_id}")
    user_data = user_response.json()
    username = user_data.get("username")

    # Fetch employee's TODO list
    todos_response = requests.get(f"{base_url}/todos", params={"userId": employee_id})
    todos_data = todos_response.json()

    # Define CSV file name
    csv_file_name = f"{employee_id}.csv"

    # Write data to CSV file
    with open(csv_file_name, mode="w", newline='', encoding='utf-8') as csv_file:
        writer = csv.writer(csv_file, quoting=csv.QUOTE_ALL)
        for task in todos_data:
            user_id = employee_id
            task_title = task.get("title")
            task_completed = task.get("completed")
            writer.writerow([user_id, username, task_completed, task_title])

    print(f"Data exported to {csv_file_name}")

if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: ./1-export_to_CSV.py <employee_id>")
    else:
        try:
            employee_id = int(sys.argv[1])
            export_to_csv(employee_id)
        except ValueError:
            print("Please provide a valid integer as employee ID.")
