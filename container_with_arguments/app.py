"""
Script to display following arguments -
1. Command line arguments.
2. Environment variables pass during Dockerfile.
3. Environment variables pass during command.
"""
import os
import sys
import argparse


# Command line arguments.
# Non keyword(Positional) and keyword arguments.
print("All arguments pass to scipt-")
print(sys.argv)

parser = argparse.ArgumentParser()
# Add keyword arguments.
parser.add_argument(
    "-name",
    "--name",
    required=False,
    default="NA",
    help="Name of programer who ran container."
)
parser.add_argument(
    "-surname",
    "--surname",
    required=True,
    help="surname is mandatory"
)
# Add a catch-all for positional arguments.
parser.add_argument(
    "args",
    nargs="*",
    help="Positional arguments."
)
args = parser.parse_args()

print("\n\nKeyword Argument:", getattr(args, "name", "NA"), getattr(args, "surname", "NA"))

# Environment Variables.
print(
    "Dockerfile environment IMAGE_NAME:",
    os.getenv("IMAGE_NAME", "NA")
)
print(
    "Dockerfile environment MY_DOCKERFILE_ENV_01:",
    os.getenv("MY_DOCKERFILE_ENV_01", "NA")
)
print(
    "Dockerfile environment MY_DOCKERFILE_ENV_02 is overwrite:",
    os.getenv("MY_DOCKERFILE_ENV_02", "NA")
)
print(
    "Environment arguments pass during image run language:",
    os.getenv("SCRIPT_LANG", "NA")
)
print(
    "Inbuild Environment arguments USERNAME:",
    os.getenv("HOME", "NA")
)
