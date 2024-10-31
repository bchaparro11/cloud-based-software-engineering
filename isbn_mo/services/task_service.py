from repositories.task_repository import TaskRepository

class TaskService:

    @staticmethod
    def create_task(name, description):
        return TaskRepository.create_task(name, description)
    
    @staticmethod
    def get_all_tasks_service():
        return TaskRepository.get_all_tasks()
    
    @staticmethod
    def update_task_service(task_id, new_name, new_description):
        return TaskRepository.update_task(task_id, new_name, new_description)