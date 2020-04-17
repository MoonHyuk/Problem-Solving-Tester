import subprocess

from executors.executorinterface import ExecutorInterface


class PythonExecutor(ExecutorInterface):
    def execute(self, stdin):
        process = subprocess.Popen(['python', self.dir + '/main.py'], stdin=subprocess.PIPE, stdout=subprocess.PIPE)
        result, _ = process.communicate(input=stdin.encode())

        return result
