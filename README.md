# Student Task Manager (Python CLI)

## Overview

A command-line based task management application built using Python.
This project demonstrates clean code structure, modular design, file handling, and input validation.

---

## Features

* Add tasks with title, priority, and due date
* View tasks with sorting:

  * Incomplete tasks first
  * Priority-based ordering (High → Low)
  * Due date sorting
* Mark tasks as completed
* Delete tasks
* Persistent storage using JSON
* Input validation and error handling

---

## Project Structure

```
student_task_manager/
│
├── main.py        # CLI + application logic
├── task.py        # Task model (data structure)
├── storage.py     # JSON read/write operations
├── tasks.json     # Data storage
└── README.md
```

---

## How It Works

### 1. Task Model

Each task contains:

* ID
* Title
* Completion status
* Priority (Low / Medium / High)
* Due Date (optional)

---

### 2. Storage

* Tasks are stored in a JSON file
* Data is converted between Python objects and dictionaries

---

### 3. CLI Interaction

* Menu-driven interface
* Continuous loop for user interaction
* Input validation for robustness

---

## Installation & Setup

### 1. Clone Repository

```
git clone <your-repo-link>
cd student_task_manager
```

### 2. Run Application

```
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
* File Handling (JSON)
* Modular Code Design
* Input Validation
* Error Handling
* Sorting with Custom Logic

---

## Future Improvements

* Task editing feature
* Search/filter tasks
* GUI version (Tkinter / Web)
* Database integration (SQLite)

---

## Author

[Your Name]
