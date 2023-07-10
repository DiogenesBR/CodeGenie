import subprocess

class GitHandler:
    def run_command(self, command):
        process = subprocess.Popen(command, stdout=subprocess.PIPE, shell=True)
        output, error = process.communicate()

        if error:
            print(f'Error: {error}')
        else:
            print(output)

    def clone(self, url, dir):
        self.run_command(f'git clone {url} {dir}')

    def init_repo(self, dir):
        self.run_command(f'git init {dir}')

    def add_file(self, repo, file):
        self.run_command(f'git -C {repo} add {file}')

    def commit(self, repo, message):
        self.run_command(f'git -C {repo} commit -m "{message}"')
