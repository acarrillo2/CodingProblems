"""
You are asked to design a file system which provides two functions:

createPath(path, value): Creates a new path and associates a value to it if possible and returns True. Returns False 
if the path already exists or its parent path doesn't exist.

get(path): Returns the value associated with a path or returns -1 if the path doesn't exist.

The format of a path is one or more concatenated strings of the form: / followed by one or more lowercase English 
letters. For example, /leetcode and /leetcode/problems are valid paths while an empty string and / are not.

Example:
Input:
["FileSystem","createPath","createPath","get","createPath","get"]
[[],["/leet",1],["/leet/code",2],["/leet/code"],["/c/d",1],["/c"]]

Output:
[null,true,true,2,false,-1]

Explanation:
FileSystem fileSystem = new FileSystem();

fileSystem.createPath("/leet", 1); // return true
fileSystem.createPath("/leet/code", 2); // return true
fileSystem.get("/leet/code"); // return 2
fileSystem.createPath("/c/d", 1); // return false because the parent path "/c" doesn't exist.
fileSystem.get("/c"); // return -1 because this path doesn't exist.


https://leetcode.ca/all/1166.html
"""

class DirectoryNode:
    def __init__(self, folder_name, value):
        self.folder_name = folder_name
        self.value = value
        self.children = {}

class FileSystem:
    def __init__(self):
        self.root_node = DirectoryNode("", None)
    
    def createPath(self, path, value):
        args = self._validate_path_and_retreive_args(path)
        if args is None:
            return False
        current_node = self.root_node
        for i in range(len(args)):
            current_directory = args[i]
            if i+1 == len(args):
                node = DirectoryNode(current_directory, value)
                current_node.children[current_directory] = node
                return True
            if current_directory not in current_node.children:
                return False
            current_node = current_node.children[current_directory]
        return False
    
    def get(self, path):
        args = self._validate_path_and_retreive_args(path)
        if args is None:
            return -1
        current_node = self.root_node
        for i in range(len(args)):
            current_directory = args[i]
            if i+1 == len(args):
                try:
                    return current_node.children[current_directory].value
                except:
                    return -1
            if current_directory not in current_node.children:
                return -1
            current_node = current_node.children[current_directory]
        return -1
    
    def _validate_path_and_retreive_args(self, path):
        if path[0] != "/":
            return None
        path = path[1:]
        return path.split("/")

def main():
    file_system = FileSystem()
    print(file_system.createPath("/leet", 1))
    print(file_system.createPath("/leet/code", 2))
    print(file_system.get("/leet/code"))
    print(file_system.createPath("/c/d", 1))
    print(file_system.get("/c"))

main()

"""
Go through directories when there is one arg left then you do the creation


"""

