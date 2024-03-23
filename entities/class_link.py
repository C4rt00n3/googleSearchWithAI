class Link:
    def __init__(self, id: int, link_recived: str, topic_id: int) -> None:
        self.id = id
        self.link = link_recived
        self.topic_id = topic_id