Todos = []
while True:
    User_Action = input("Type add, show or exit: ")

    match User_Action:
        case 'add':
            todo = input("enter a todo")
            Todos.append(todo)
        case 'show':
            print(Todos)
        case 'exit':
            break
        