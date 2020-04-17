import subprocess

from executors.executorinterface import ExecutorInterface


class PHPExecutor(ExecutorInterface):
    def execute(self, stdin):
        process = subprocess.Popen(['php', self.dir + '/main.php'], stdin=subprocess.PIPE, stdout=subprocess.PIPE)
        result, _ = process.communicate(input=stdin.encode())

        return result
