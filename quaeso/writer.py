from typing import Union, Protocol


class Writeable(Protocol):
    def write(self, content: Union[str, bytes]):
        ...


def write(content: Union[str, bytes], to: Writeable, formatter=None, colorizer=None):
    if isinstance(content, str):
        content = formatter(content) if formatter else content
        content = colorizer(content) if colorizer else content
        content = "\n" + content + "\n"
    to.write(content)
