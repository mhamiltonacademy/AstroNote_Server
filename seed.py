from models import db, Engineer, Project, Task


def test():
    ranffi = Engineer(
        name = 'ranffi',
        password = 'password'
    )
    jasmine = Engineer(
        name = 'jasmine',
        password = 'password'
    )

    quiyet = Engineer(
        name = 'quiyet',
        password = 'password'
    )
    jonathan = Engineer(
        name = 'jonathan',
        password = 'password'
    )
    project = Project(
        name = "Frontend",
        description = "Create a UI for Astronote",
        is_complete = False
    )
    
    task1 = Task(
        name = 'fix bug',
        description = 'small bug on the landing page',
        deadline = None,
        priority = 3,
        progress = 2,
        engineer = ranffi,
        project = project
    )
    task2 = Task(
        name = 'Mock ups',
        description = 'Create mock ups',
        deadline = None,
        priority = 2,
        progress = 1,
        engineer = jasmine,
        project = project
    )
    task3 = Task(
        name = 'Research Angular',
        description = 'Do some research on Angular',
        deadline = None,
        priority = 1,
        progress = 0,
        engineer = quiyet,
        project = project
    )
 
    db.session.add_all([ranffi,jasmine,quiyet,jonathan,project,task1,task2,task3])
    ranffi.projects.append(project)
    jasmine.projects.append(project)
    quiyet.projects.append(project)
    jonathan.projects.append(project)
    db.session.commit()

    # print(ranffi.my_projects)
    # print(project.engineers)


test()