# Student Task Manager (Python CLI)

## Overview

A command-line task management application built using Python to efficiently create, organize, and track tasks. The system supports prioritization, due date management, and structured task handling using persistent storage.

---

## Features

* Add tasks with title, priority, and due date
* View tasks sorted by:

  * Incomplete tasks first
  * Priority (High → Low)
  * Due date
* Mark tasks as completed
* Delete tasks
* Persistent storage using JSON
* Input validation and error handling for robust execution

---

## Project Structure

```
student_task_manager/
│
├── main.py        # CLI interface and control flow
├── task.py        # Task model and structure
├── storage.py     # JSON data handling
├── tasks.json     # Persistent storage
└── README.md
```

---

## How It Works

### Task Model

Each task includes:

* ID
* Title
* Completion status
* Priority (Low / Medium / High)
* Due date

---

### Storage

* Tasks are stored in a JSON file
* Data is serialized/deserialized between Python objects and JSON

---

### CLI Interface

* Menu-driven interaction
* Continuous loop for user operations
* Input validation ensures stability

---

## How to Run

```
git clone <your-repo-link>
cd student_task_manager
python main.py
```

---

## Sample Output

```
--- Student Task Manager ---
1. Add Task
2. View Tasks
3. Mark Task as Completed
4. Delete Task
5. Exit
```

---

## Example Task Display

```
1. Study Python [✗] (Priority: High, Due: 2026-05-10)
2. Build Project [✓] (Priority: Medium, Due: No due date)
```

---

## Key Concepts Demonstrated

* Object-Oriented Programming (OOP)
* File Handling using JSON
* Modular Code Design
* Input Validation and Error Handling
* Custom Sorting Logic

---

## Future Improvements

* Task editing functionality
* Search and filtering options
* GUI version (Tkinter or Web-based)
* Database integration (SQLite)

---

## Author

Gautami Poojari
