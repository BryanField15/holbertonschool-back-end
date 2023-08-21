## Gather Data from an API

This repository covers a Python script that fetches and displays an employee's TODO list progress from a REST API.

### Task 0 - Employee TODO Progress
- **Filename:** `0-gather_data_from_an_API.py`

- **Description:**
The script fetches data for a given employee ID and shows their TODO list progress. It utilizes either `urllib` or `requests` modules. The output is formatted as:

### Task 1 - Export to CSV
- **Filename:** `1-export_to_CSV.py`

- **Description:**
Extending the script from Task #0, this script exports data related to an employee's TODO list progress into the CSV format.

- **Requirements:**
    - Records all tasks that are owned by the specified employee.
    - Format: `"USER_ID","USERNAME","TASK_COMPLETED_STATUS","TASK_TITLE"`
    - File name format: `USER_ID.csv`


### Task 2 - Export to JSON
- **Filename:** `2-export_to_JSON.py`

- **Description:**
Building upon Task #0, this script exports the employee's TODO list progress data into the JSON format.

- **Requirements:**
    - Records all tasks associated with the specified employee.
    - Format:
    ```json
    {
      "USER_ID": [
        {
          "task": "TASK_TITLE",
          "completed": TASK_COMPLETED_STATUS,
          "username": "USERNAME"
        },
        ...
      ]
    }
    ```
    - File name format: `USER_ID.json`

### Task 3 - Dictionary of List of Dictionaries
- **Filename:** `3-dictionary_of_list_of_dictionaries.py`

- **Description:**
Building upon Task #0, this script exports data for all employees and their associated tasks into the JSON format.

- **Requirements:**
    - Records tasks for all employees.
    - Format:
    ```json
    {
      "USER_ID": [
        {
          "username": "USERNAME",
          "task": "TASK_TITLE",
          "completed": TASK_COMPLETED_STATUS
        },
        ...
      ],
      "USER_ID": [
        {
          "username": "USERNAME",
          "task": "TASK_TITLE",
          "completed": TASK_COMPLETED_STATUS
        },
        ...
      ],
      ...
    }
    ```
    - File name must be: `todo_all_employees.json`

**Example Output:**
```json
{
  "1": [
    {"username": "Bret", "task": "delectus aut autem", "completed": false},
    {"username": "Bret", "task": "quis ut nam facilis et officia qui", "completed": false},
    {"username": "Bret", "task": "fugiat veniam minus", "completed": false}
    ...
  ]
}
