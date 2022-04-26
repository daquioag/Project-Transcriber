import re


def convert_URL_to_ID(youtube_URL):
    m = re.compile("((?<=(v|V)/)|(?<=be/)|(?<=(\?|\&)v=)|(?<=embed/))([\w-]+)")
    matchResult = m.search(youtube_URL)
    if matchResult:
        return matchResult.group(0)