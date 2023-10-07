import os


def create_file(filename):
    with open(filename, "w") as file:
        print(f"Created file: {filename}")

def add_content(filename, content):
    with open(filename, "a") as file:
        file.write(f"\n{content}")
        
def replace_content(filename, old_string, new_string):
    if os.path.exists(filename):
        with open(filename, "r+") as file:
            old_content = file.readlines()
            
            for line in old_content:
                if old_string in line:
                    line = line.replace(old_string, new_string)
                    
                file.write(line)
            
def delete_file(filename):
    if os.path.exists(filename):
        os.remove(filename)
    else:
        print("File not found!")
            
            
functions = {
    "Create": create_file,
    "Add": add_content,
    "Replace": replace_content,
    "Delete": delete_file,
}

while True:
    command_args = input().split("-")
    operation = command_args[0]
    
    if operation == "End":
        print("Goodbye!")
        break
    
    file_name = command_args[1]
    
    root_dir = os.path.dirname(os.path.abspath(__file__))
    file_path = os.path.join(root_dir, file_name)
    
    if operation == "Create":
        functions[operation](file_path)
    elif operation == "Add":
        content = command_args[2]
        functions[operation](file_path, content)
    elif operation == "Replace":
        old_string, new_string = command_args[2], command_args[3]
        functions[operation](file_path, old_string, new_string)
    elif operation == "Delete":
        functions[operation](file_path)