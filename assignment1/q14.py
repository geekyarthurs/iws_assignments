def add_tags(tag: str, textContext: str) -> str:
    element = "<{tag}>{content}</{tag}>".format(tag=tag, content=textContext)
    return element