Todos = []
while True:
    User_Action = input("Type, add, show, edit, complete or exit ")
    User_Action = User_Action.strip()

    match User_Action:
        case 'add':
            todo = (input("Enter a todo : ")) + "/n"
            
            Todos.append(todo)
            file = open('Todos.txt', 'w')
            file.writelines(Todos)
        case 'show':
            for idx, items in enumerate(Todos):
                row = f"{idx + 1}-{items}"
                print(row)
        case 'edit':
            number = int(input("Enter the number of todo to edit : "))
            number = number - 1
            new_todo = (input("Enter a new Todo :"))
            Todos[number] = new_todo 
        case 'complete':
            number = int(input("Enter the number of Todo to remove"))
            Todos.pop(number - 1)
        case 'exit':
            break