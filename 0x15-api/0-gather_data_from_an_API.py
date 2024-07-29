#!/usr/bin/python3
"""
Fetches and displays TODO list progress
 for a given employee ID using a REST API.
"""

import requests
import sys

def get_employee_info(employee_id):
	"""
	Gets the employee information and their TODO list progress.

	:param employee_id: The ID of the employee.
	:type employee_id: int
	:return: None
	"""
	base_url = "https://jsonplaceholder.typicode.com"

	# Fetch employee details
	user_response = requests.get(f"{base_url}/users/{employee_id}")
	user_data = user_response.json()

	# Fetch employee's TODO list
	todos_response = requests.get(f"{base_url}/todos", params={"userId": employee_id})
	todos_data = todos_response.json()

	# Extract employee name
	employee_name = user_data.get("name")

	# Calculate TODO list progress
	total_tasks = len(todos_data)
	done_tasks = [task for task in todos_data if task.get("completed")]
	number_of_done_tasks = len(done_tasks)

	# Display the TODO list progress
	print(f"Employee {employee_name} is done with tasks({number_of_done_tasks}/{total_tasks}):")
	for task in done_tasks:
		print(f"\t {task.get('title')}")

if __name__ == "__main__":
	if len(sys.argv) != 2:
		print("Usage: ./0-gather_data_from_an_API.py <employee_id>")
	else:
		try:
			employee_id = int(sys.argv[1])
			get_employee_info(employee_id)
		except ValueError:
			print("Please provide a valid integer as employee ID.")
