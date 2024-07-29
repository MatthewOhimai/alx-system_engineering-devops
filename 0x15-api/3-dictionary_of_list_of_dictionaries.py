#!/usr/bin/python3
"""
Module to export data in the JSON format
"""

import json
import requests

def fetch_data(url):
	"""
	Fetches data from the given URL and returns it as a JSON object.
	"""
	response = requests.get(url)
	return response.json()

def main():
	"""
	Fetches data from the JSONPlaceholder API and exports it to a JSON file.
	"""
	# Base URLs
	user_url = 'https://jsonplaceholder.typicode.com/users'
	todo_url = 'https://jsonplaceholder.typicode.com/todos'

	# Fetch users and todos
	users = fetch_data(user_url)
	todos = fetch_data(todo_url)

	# Dictionary to hold user tasks
	user_tasks = {}

	for user in users:
		user_id = user.get('id')
		username = user.get('username')
		user_tasks[user_id] = []
		for task in todos:
			if task.get('userId') == user_id:
				task_info = {
					"username": username,
					"task": task.get('title'),
					"completed": task.get('completed')
				}
				user_tasks[user_id].append(task_info)

	# Write to JSON file
	with open('todo_all_employees.json', 'w') as json_file:
		json.dump(user_tasks, json_file)

if __name__ == "__main__":
	main()#!/usr/bin/python3
"""
Module to export data in the JSON format
"""

import json
import requests

def fetch_data(url):
	"""
	Fetches data from the given URL and returns it as a JSON object.
	"""
	response = requests.get(url)
	return response.json()

def main():
	"""
	Fetches data from the JSONPlaceholder API and exports it to a JSON file.
	"""
	# Base URLs
	user_url = 'https://jsonplaceholder.typicode.com/users'
	todo_url = 'https://jsonplaceholder.typicode.com/todos'

	# Fetch users and todos
	users = fetch_data(user_url)
	todos = fetch_data(todo_url)

	# Dictionary to hold user tasks
	user_tasks = {}

	for user in users:
		user_id = user.get('id')
		username = user.get('username')
		user_tasks[user_id] = []
		for task in todos:
			if task.get('userId') == user_id:
				task_info = {
					"username": username,
					"task": task.get('title'),
					"completed": task.get('completed')
				}
				user_tasks[user_id].append(task_info)

	# Write to JSON file
	with open('todo_all_employees.json', 'w') as json_file:
		json.dump(user_tasks, json_file)

if __name__ == "__main__":
	main()
