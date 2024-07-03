# %%
from pathlib import Path

import jinja2
from jinja2_ansible_filters import AnsibleCoreFiltersExtension

# %%
env = jinja2.Environment(extensions=[AnsibleCoreFiltersExtension], autoescape=True)

# %%
# extract image name from name:tag
image = "mcr.microsoft.com/azure-functions/python:4-python3.10"
expected = "mcr.microsoft.com/azure-functions/python"

result = env.from_string(r"{{ image | regex_replace('^(.*):(.*)$', '\\1') }}").render(image=image)
print(f"{result=}")
print(f"{expected=}")
assert Path(result) == Path(expected)

# %%
# extract image tag from name:tag
image = "mcr.microsoft.com/azure-functions/python:4-python3.10"
expected = "4-python3.10"

result = env.from_string(r"{{ image | regex_replace('^(.*):(.*)$', '\\2') }}").render(image=image)
print(f"{result=}")
print(f"{expected=}")
assert Path(result) == Path(expected)

# %%
# replace left text up to rightmost "-
project_name = "dana-dtsc-package-utilities"
expected = "utilities"

result = env.from_string(r"{{ project_name | regex_replace('^.*(?<=-)', '') }}").render(
    project_name=project_name
)
print(f"{result=}")
print(f"{expected=}")
assert Path(result) == Path(expected)

# %%
# get path to parent directory
dockerfile_path = "./docker/deep/nested/test.Dockerfile"
expected = str(Path(dockerfile_path).parent)

result = env.from_string(r"{{ dockerfile_path | dirname }}").render(dockerfile_path=dockerfile_path)
print(f"{result=}")
print(f"{expected=}")
assert Path(result) == Path(expected)

# %%
