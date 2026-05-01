class Task:
    def __init__(self, task_id, title, completed=False, priority="Low", due_date=None):
        self.id = task_id
        self.title = title
        self.completed = completed
        self.priority = priority
        self.due_date = due_date
    
    def to_dict(self):
        return {
            "id": self.id,
            "title": self.title,
            "completed": self.completed,
            "priority": self.priority,
            "due_date": self.due_date
        }
    
    @staticmethod
    def from_dict(data):
        return Task(
            task_id=data["id"],
            title=data["title"],
            completed=data["completed"],
            priority=data.get("priority", "Low"),
            due_date=data.get("due_date", None)
        )