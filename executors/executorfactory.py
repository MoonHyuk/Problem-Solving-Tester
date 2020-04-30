from executors import executorinterface, phpexecutor, pythonexecutor, cppexecutor


def get_executor(lang) -> executorinterface:
    if lang == 'cpp':
        return cppexecutor.CppExecutor()
    if lang == 'python3':
        return pythonexecutor.PythonExecutor()
    if lang == 'php7':
        return phpexecutor.PHPExecutor()

    raise NotImplementedError('Language {} is not supported'.format(lang))
