import os
import glob

from executors import executorfactory

lang = os.getenv('LANG')

executor = executorfactory.get_executor(lang)

inputs = []

for filename in glob.iglob('io/*.in', recursive=True):
    inputs.append(filename)

for i in inputs:
    with open(i) as f:
        stdin = f.read()

    result = executor.execute(stdin)

    result = result.decode().strip()

    output = i.replace('.in', '.out')
    with open(output) as f:
        expected = f.read().strip()

    if result == expected:
        print(i + ' passed')
    else:
        print(i + ' failed')
        print('expected:\n' + expected)
        print('actual:\n' + result)
