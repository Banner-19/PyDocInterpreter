# Code Executer
def execute_code(code, globals_dict=None, locals_dict=None):
    globals_dict = globals_dict or {}
    locals_dict = locals_dict or {}
    exec(code, globals_dict, locals_dict)
    return locals_dict