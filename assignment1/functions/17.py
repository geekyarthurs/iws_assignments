from typing import Callable
str_checker: Callable[ [str, str], bool ] = lambda string, char: string.startswith(char)