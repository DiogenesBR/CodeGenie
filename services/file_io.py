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
