def get_todos(filepath="todos.txt"):
    """ Read a text newlocation and return the
    list of to items.
    """
    with open(filepath, 'r') as file_local:
        """Write the todo item list in the text newlocation.
        """
        todos_local = file_local.readlines()
    return todos_local


def write_todos(todos_arg,filepath="todos.txt"):
    with open('todos.txt', 'w') as file:
        file.writelines(todos_arg)

if  __name__=='__main__':
    print("Hello from functions")