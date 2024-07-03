# %%
import platform


# %%
def get_sysinfo():
    """Print system information."""
    print(platform.machine())
    print(platform.system())
    print(platform.version())
    print(platform.processor())


def get_python_info():
    """Print python version."""
    print(platform.python_version)


def return2():
    """Return 2."""
    return 2


def hello_world():
    """Return 'Hello world!'."""
    return "Hello world!"
