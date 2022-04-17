"""Rewrite README.md without <script> ... </script> tags."""

import re


def main() -> None:
    with open("README.md", "r") as f:
        README = f.read()

    README_no_script_tag = re.sub("<style scoped>(.|\n)*?<\/style>", "", README)
    README_no_script_tag = re.sub("<style type=\"text/css\">(.|\n)*?<\/style>", "", README)

    with open("README.md", "w") as f:
        f.write(README_no_script_tag)


if __name__ == "__main__":
    main()
