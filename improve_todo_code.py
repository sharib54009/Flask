while True:
    User_Action = input("Type add, show, edit, complete or exit : ")
    User_Action = User_Action.strip()
    match User_Action:
        case 'add':
            Todo = input("enter a todo : ")
            with open('todos.txt', 'r') as file:
                Todos = file.readlines()
            Todos.append(Todo + '\n')
            with open('todos.txt', 'w') as file:
                file.writelines(Todos)
        case 'show':
            with open('todos.txt', 'r') as file:
                Todos = file.readlines()
            for idx, items in enumerate(Todos):
                items = items.strip('\n')
                print(idx + 1, items)
        case 'edit' :
            number = int(input("Enter the number of todo to edit : "))
            number = number - 1
            new_todo = input("Enter new todo : ")
            Todos[number] = new_todo + '\n'
            with open('todos.txt', 'w') as file:
                file.writelines(Todos)
        case 'complete':
            number = int(input("Enter the number of todo to remove : "))    
            Todos.pop(number - 1)
            with open('todos.txt', 'w') as file:                
                file.writelines(Todos)
        case 'exit':            
            break