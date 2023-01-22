import sys
import json
import re
import mmap


TOKENS_REGEX = ".git/hooks/regexes.json"


class TokenFoundException(BaseException):

    def __init__(self, token_type, filename, *args):
        self.token_type = token_type
        self.filename = filename

    def __str__(self):

        return self.token_type + " found in " + self.filename


if __name__ == "__main__":
    
    with open(TOKENS_REGEX, "r") as f:
        data = json.load(f).items()

    for i in range(1, len(sys.argv)):
        filename = sys.argv[i]

        with open(filename, mode="r") as file_obj:
            with mmap.mmap(file_obj.fileno(), length=0, access=mmap.ACCESS_READ) as mmap_obj:

                for token in data:
                    if re.search(token[1].encode(), mmap_obj):

                        raise TokenFoundException(token[0], filename=filename)
