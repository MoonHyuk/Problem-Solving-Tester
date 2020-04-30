import subprocess

from executors.executorinterface import ExecutorInterface


class CppExecutor(ExecutorInterface):
    def execute(self, stdin):
        subprocess.run(['g++', self.dir + '/main.cpp', '-o', 'main', '-O2', '-Wall', '-lm', '-static', '-std=gnu++14', '-DONLINE_JUDGE'])
        process = subprocess.Popen(['./main'], stdin=subprocess.PIPE, stdout=subprocess.PIPE)
        result, _ = process.communicate(input=stdin.encode())

        return result
