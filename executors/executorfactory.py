from executors import executorinterface, phpexecutor, pythonexecutor


def get_executor(lang) -> executorinterface:
    if lang == 'python3':
        return pythonexecutor.PythonExecutor()
    if lang == 'php7':
        return phpexecutor.PHPExecutor()

    raise NotImplementedError('Language {} is not supported'.format(lang))
