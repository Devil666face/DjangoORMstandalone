from db.models import Task

if __name__=='__main__':
    task = Task(title='Проверка ОРМ Джанго')
    task.save()