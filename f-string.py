Todos = []
while True:
    User_Action = input("Type add, show, edit or exit : ")
    User_Action = User_Action.strip()
    match User_Action:
        case 'add':
            todo = input("enter a todo : ")
            Todos.append(todo)
        case 'show':
            for idx, items in enumerate(Todos):
                row = f"{idx}-{items}"
                print(row)
        case 'edit' :
            number = int(input("Enter the number of todo to edit : "))
            number = number - 1
            new_todo = input("Enter new todo : ")
            Todos[number] = new_todo
        case 'exit':
            break
        