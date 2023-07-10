from services.git_handler import GitHandler
from services.file_io import FileIO
# from services.tree_sitter_handler import TreeSitterHandler
from tree_sitter import Language, Parser

def main():
    git = GitHandler()
    file_io = FileIO()
    # tree_sitter_handler = TreeSitterHandler()

    # 1. Clone the languages specification"
    git.clone('https://github.com/tree-sitter/tree-sitter-c-sharp', 'services/tree-sitter/tree-sitter-c-sharp')
    git.clone('https://github.com/tree-sitter/tree-sitter-javascript', 'services/tree-sitter/tree-sitter-javascript')
    git.clone('https://github.com/tree-sitter/tree-sitter-python', 'services/tree-sitter/tree-sitter-python')
    

    Language.build_library(
    # Store the library in the `build` directory
    'services/tree-sitter/build/my-languages.so',
    # Include one or more languages
    [
        'services/tree-sitter/tree-sitter-python'
    ]
    )

    PY_LANGUAGE = Language('build/my-languages.so', 'python')

    parser = Parser()
    parser.set_language(PY_LANGUAGE)


    tree = parser.parse(bytes("""
import os

class FileIO:
    def create_directory(self, dir):
        os.makedirs(dir, exist_ok=True)

    def create_file(self, path):
        with open(path, 'w') as file:
            file.write('')
            
    def read_file(self, path):
        with open(path, 'r') as file:
            return file.read()

    def list_files(self, dir, extensions=None):
        return [os.path.join(root, file) for root, dirs, files in os.walk(dir) for file in files if extensions is None or file.endswith(tuple(extensions))]
""", "utf8"))

"""
Desired output:
nodes:
-   name: FileIO
    type: class
    signature: \"class FileIO:\"
    children:
    -   name: create_directory
        type: method
        signature: \"def create_directory(self, dir):\"        
    -   name: create_file
        type: method
        signature: \"def create_file(self, path):\"
    -   name: read_file
        type: method
        signature: \"def read_file(self, path):\"
    -   name: list_files
        type: method
        signature: \"def list_files(self, dir, extensions=None):\"        
"""


if __name__ == '__main__':
    main()
