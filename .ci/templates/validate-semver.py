# %%
import argparse
import json
import logging
import sys

import semver

# %%
# set up logging
FORMAT = "%(asctime)s - %(levelname)-8s - %(name)s - %(funcName)s:%(lineno)d - %(message)s"
logging.basicConfig(format=FORMAT)
logging.captureWarnings(True)
logger = logging.getLogger(__name__)
logger.setLevel(logging.DEBUG)

# %%
parser = argparse.ArgumentParser()
parser.add_argument("--current", type=str, required=True)
parser.add_argument("--new", type=str, required=True)
args = parser.parse_args()


# %%
def parse(inputstr: str):
    """Parse json."""
    try:
        return json.loads(inputstr)
    except Exception as e:  # NOQA: F841
        # logger.debug(e)
        return inputstr


def get_max_ver(versions: list):
    """Get max semver version from list."""
    # NOTE: VersionInfo -> Version in semver3
    return max(versions, key=semver.Version.parse)


# %%
if __name__ == "__main__":
    logger.debug(f"{args.current=}")
    logger.debug(f"{args.new=}")

    current = parse(args.current)
    new = parse(args.new)
    logger.debug(f"{current=}")
    logger.debug(f"{new=}")

    if current == "":
        logger.info("No current version found; validation not required")
        sys.exit(0)

    if isinstance(current, list):
        current = get_max_ver(current)

    if isinstance(new, list):
        new = get_max_ver(new)

    logger.info(f"{new=}; {current=}")
    if not semver.Version.is_valid(current):
        raise ValueError(f"Error: {current} is not valid semver format")
    if not semver.Version.is_valid(new):
        raise ValueError(f"Error: {new} is not valid semver format")
    if semver.compare(new, current) != 1:
        raise ValueError(f"Error: New Version {new} is not > Current Version {current}")
    logger.info(f"Successfully validated -- new semver ({new}) > current")
    sys.exit(0)
