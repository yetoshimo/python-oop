class Topic:
    def __init__(self, id: int, topic: str, storage_folder: str):
        self.storage_folder = storage_folder
        self.topic = topic
        self.id = id

    def __repr__(self):
        return f"Topic {self.id}: {self.topic} in {self.storage_folder}"

    def edit(self, new_topic: str, new_storage_folder: str):
        self.topic = new_topic
        self.storage_folder = new_storage_folder
