Todos = []
while True:
    User_Action = input("Type add, show, edit, complete or exit : ")
    User_Action = User_Action.strip()
    match User_Action:
        case 'add':
            todo = input("enter a todo : ")
            Todos.append(todo)
        case 'show':
            for idx, items in enumerate(Todos):
                print(idx + 1, items)
        case 'edit' :
            number = int(input("Enter the number of todo to edit : "))
            number = number - 1
            new_todo = input("Enter new todo : ")
            Todos[number] = new_todo
        case 'complete':
            number = int(input("Enter the number of todo to remove : "))
            Todos.pop(number - 1)
        case 'exit':
            break
        