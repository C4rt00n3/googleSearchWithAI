class Content:
    def __init__(self,id: int, title: str, content: str, link_id: int) -> None:
        self.title = title
        self.content = content
        self.link_id = link_id
        self.id = id