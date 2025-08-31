import json
import os
from datetime import datetime

class TodoList:
    def __init__(self, filename="todo_list.json"):
        self.filename = filename
        self.tasks = self.load_tasks()
    
    def load_tasks(self):
        """Load tasks from JSON file"""
        if os.path.exists(self.filename):
            try:
                with open(self.filename, 'r') as file:
                    return json.load(file)
            except json.JSONDecodeError:
                print("Error reading todo file. Starting with empty list.")
                return []
        return []
    
    def save_tasks(self):
        """Save tasks to JSON file"""
        with open(self.filename, 'w') as file:
            json.dump(self.tasks, file, indent=2)
    
    def add_task(self, title, description="", priority="medium"):
        """Add a new task"""
        task = {
            "id": len(self.tasks) + 1,
            "title": title,
            "description": description,
            "priority": priority,
            "completed": False,
            "created_at": datetime.now().strftime("%Y-%m-%d %H:%M:%S"),
            "completed_at": None
        }
        self.tasks.append(task)
        self.save_tasks()
        print(f"✅ Task '{title}' added successfully!")
    
    def view_tasks(self, show_completed=True):
        """Display all tasks"""
        if not self.tasks:
            print("📝 No tasks found!")
            return
        
        print("\n📋 YOUR TODO LIST")
        print("=" * 50)
        
        for task in self.tasks:
            if not show_completed and task["completed"]:
                continue
                
            status = "✅" if task["completed"] else "⏳"
            priority_icon = {
                "high": "🔴",
                "medium": "🟡", 
                "low": "🟢"
            }.get(task["priority"], "🟡")
            
            print(f"{status} {priority_icon} Task #{task['id']}: {task['title']}")
            if task["description"]:
                print(f"   📄 Description: {task['description']}")
            print(f"   📅 Created: {task['created_at']}")
            if task["completed"] and task["completed_at"]:
                print(f"   ✅ Completed: {task['completed_at']}")
            print("-" * 30)
    
    def complete_task(self, task_id):
        """Mark a task as completed"""
        for task in self.tasks:
            if task["id"] == task_id:
                if task["completed"]:
                    print(f"❌ Task '{task['title']}' is already completed!")
                else:
                    task["completed"] = True
                    task["completed_at"] = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
                    self.save_tasks()
                    print(f"🎉 Task '{task['title']}' marked as completed!")
                return
        print(f"❌ Task with ID {task_id} not found!")
    
    def delete_task(self, task_id):
        """Delete a task"""
        for i, task in enumerate(self.tasks):
            if task["id"] == task_id:
                deleted_task = self.tasks.pop(i)
                # Update IDs for remaining tasks
                for j in range(i, len(self.tasks)):
                    self.tasks[j]["id"] = j + 1
                self.save_tasks()
                print(f"🗑️ Task '{deleted_task['title']}' deleted successfully!")
                return
        print(f"❌ Task with ID {task_id} not found!")
    
    def edit_task(self, task_id, new_title=None, new_description=None, new_priority=None):
        """Edit a task"""
        for task in self.tasks:
            if task["id"] == task_id:
                if new_title:
                    task["title"] = new_title
                if new_description:
                    task["description"] = new_description
                if new_priority:
                    task["priority"] = new_priority
                self.save_tasks()
                print(f"✏️ Task updated successfully!")
                return
        print(f"❌ Task with ID {task_id} not found!")
    
    def get_stats(self):
        """Get statistics about tasks"""
        total = len(self.tasks)
        completed = sum(1 for task in self.tasks if task["completed"])
        pending = total - completed
        
        print("\n📊 TASK STATISTICS")
        print("=" * 30)
        print(f"📋 Total Tasks: {total}")
        print(f"✅ Completed: {completed}")
        print(f"⏳ Pending: {pending}")
        if total > 0:
            completion_rate = (completed / total) * 100
            print(f"📈 Completion Rate: {completion_rate:.1f}%")

def display_menu():
    """Display the main menu"""
    print("\n🎯 TODO LIST MANAGER")
    print("=" * 30)
    print("1. Add Task")
    print("2. View Tasks")
    print("3. Complete Task")
    print("4. Delete Task")
    print("5. Edit Task")
    print("6. View Statistics")
    print("7. Exit")
    print("-" * 30)

def get_priority():
    """Get priority from user"""
    while True:
        priority = input("Priority (high/medium/low) [default: medium]: ").lower()
        if priority in ["high", "medium", "low"] or priority == "":
            return priority if priority else "medium"
        print("❌ Please enter 'high', 'medium', or 'low'")

def main():
    """Main function"""
    todo = TodoList()
    
    print("🎉 Welcome to Todo List Manager!")
    print("Manage your tasks efficiently!")
    
    while True:
        display_menu()
        choice = input("Enter your choice (1-7): ")
        
        if choice == "1":
            title = input("Enter task title: ")
            if not title.strip():
                print("❌ Task title cannot be empty!")
                continue
            description = input("Enter task description (optional): ")
            priority = get_priority()
            todo.add_task(title, description, priority)
            
        elif choice == "2":
            show_completed = input("Show completed tasks? (y/n) [default: y]: ").lower()
            show_completed = show_completed != "n"
            todo.view_tasks(show_completed)
            
        elif choice == "3":
            todo.view_tasks(show_completed=False)
            try:
                task_id = int(input("Enter task ID to complete: "))
                todo.complete_task(task_id)
            except ValueError:
                print("❌ Please enter a valid task ID!")
                
        elif choice == "4":
            todo.view_tasks()
            try:
                task_id = int(input("Enter task ID to delete: "))
                confirm = input("Are you sure? (y/n): ").lower()
                if confirm == "y":
                    todo.delete_task(task_id)
            except ValueError:
                print("❌ Please enter a valid task ID!")
                
        elif choice == "5":
            todo.view_tasks()
            try:
                task_id = int(input("Enter task ID to edit: "))
                new_title = input("New title (press Enter to skip): ")
                new_description = input("New description (press Enter to skip): ")
                new_priority = input("New priority (high/medium/low, press Enter to skip): ")
                
                if new_priority and new_priority not in ["high", "medium", "low"]:
                    print("❌ Invalid priority!")
                    continue
                    
                todo.edit_task(task_id, 
                              new_title if new_title else None,
                              new_description if new_description else None,
                              new_priority if new_priority else None)
            except ValueError:
                print("❌ Please enter a valid task ID!")
                
        elif choice == "6":
            todo.get_stats()
            
        elif choice == "7":
            print("👋 Thank you for using Todo List Manager!")
            break
            
        else:
            print("❌ Invalid choice! Please enter a number between 1 and 7.")

if __name__ == "__main__":
    main()
