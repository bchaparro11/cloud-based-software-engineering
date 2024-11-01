from models.task import Task, db

class TaskRepository:

    @staticmethod
    def create_task(name, description):
        task = Task(name=name, description=description)
        db.session.add(task)
        db.session.commit()
        return task
    
    @staticmethod
    def get_all_tasks():
        try:
            tasks = Task.query.all()
            return tasks
        except Exception as e:
            print(f"An error occurred: {e}")
            return None
        
    @staticmethod
    def update_task(task_id, new_name=None, new_description=None):
        try:
            task = Task.query.get(task_id)
            
            if not task:
                return f"Task with id {task_id} not found."

            if new_name:
                task.name = new_name
            
            if new_description:
                task.description = new_description

            db.session.commit()
            return f"Task with id {task_id} has been updated successfully."
        except Exception as e:
            db.session.rollback()
            return f"An error occurred: {e}"