class Storage:
    def __init__(self):
        self.categories = []
        self.topics = []
        self.documents = []

    def __repr__(self):
        _storage = []
        for _doc in self.documents:
            _storage.append(repr(_doc))
        return '\n'.join(_storage)

    @staticmethod
    def check_category(_category, _categories):
        return _category in _categories

    @staticmethod
    def check_topic(_topic, _topics):
        return _topic in _topics

    @staticmethod
    def check_document(_document, _documents):
        return _document in _documents

    @staticmethod
    def get_category(_id, _categories):
        return next(filter(lambda x: x.id == _id, _categories))

    @staticmethod
    def get_topic(_id, _topics):
        return next(filter(lambda x: x.id == _id, _topics))

    @staticmethod
    def get_documents(_id, _documents):
        return next(filter(lambda x: x.id == _id, _documents))

    def add_category(self, category):
        if not self.check_category(category, self.categories):
            self.categories.append(category)

    def add_topic(self, topic):
        if not self.check_topic(topic, self.topics):
            self.topics.append(topic)

    def add_document(self, document):
        if not self.check_document(document, self.documents):
            self.documents.append(document)

    def edit_category(self, category_id: int, new_name: str):
        _edit_category = self.get_category(category_id, self.categories)
        _edit_category.name = new_name

    def edit_topic(self, topic_id: int, new_topic: str, new_storage_folder: str):
        _edit_topic = self.get_topic(topic_id, self.topics)
        _edit_topic.topic = new_topic
        _edit_topic.storage_folder = new_storage_folder

    def edit_document(self, document_id: int, new_file_name: str):
        _edit_document = self.get_documents(document_id, self.documents)
        _edit_document.file_name = new_file_name

    def delete_category(self, category_id: int):
        _delete_category = self.get_category(category_id, self.categories)
        self.categories.remove(_delete_category)

    def delete_topic(self, topic_id: int):
        _delete_topic = self.get_topic(topic_id, self.topics)
        self.topics.remove(_delete_topic)

    def delete_document(self, document_id: int):
        _delete_document = self.get_documents(document_id, self.documents)
        self.documents.remove(_delete_document)

    def get_document(self, document_id: int):
        return self.get_documents(document_id, self.documents)
