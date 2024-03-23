import unittest
from unittest.mock import MagicMock
from database import Database

class TestDatabase(unittest.TestCase):
    def setUp(self):
        self.db = Database()

    def tearDown(self):
        self.db.mydb.close()

    def test_topic_create(self):
        topic_db = self.db.TopicDatabase(self.db.mydb)
        topic = topic_db.create_topic("Test Topic")
        self.assertIsNotNone(topic)

    def test_topic_find_many(self):
        topic_db = self.db.TopicDatabase(self.db.mydb)
        topics = topic_db.find_many()
        self.assertIsInstance(topics, list)

    def test_topic_update(self):
        topic_db = self.db.TopicDatabase(self.db.mydb)
        topic = topic_db.create_topic("Test Topic")
        updated_topic = topic_db.update_topic(topic.id, "Updated Test Topic")
        self.assertEqual(updated_topic.name, "Updated Test Topic")

    def test_topic_delete(self):
        topic_db = self.db.TopicDatabase(self.db.mydb)
        topic = topic_db.create_topic("Test Topic")
        topic_db.delete_topic(topic.id)
        self.assertIsNone(topic_db.find_one(topic.id))

    def test_content_create(self):
        content_db = self.db.ContentDatabase(self.db.mydb)
        content = content_db.create_data("Test Title", "Test Content", 1)
        self.assertIsNotNone(content)

    def test_content_find_many(self):
        content_db = self.db.ContentDatabase(self.db.mydb)
        contents = content_db.find_many()
        self.assertIsInstance(contents, list)

    def test_content_update(self):
        content_db = self.db.ContentDatabase(self.db.mydb)
        content = content_db.create_data("Test Title", "Test Content", 1)
        updated_content = content_db.update_data(content.id, "Updated Test Title", "Updated Test Content", 2)
        self.assertEqual(updated_content.title, "Updated Test Title")
        self.assertEqual(updated_content.content, "Updated Test Content")
        self.assertEqual(updated_content.link_id, 2)

    def test_content_delete(self):
        content_db = self.db.ContentDatabase(self.db.mydb)
        content = content_db.create_data("Test Title", "Test Content", 1)
        content_db.delete_data(content.id)
        self.assertIsNone(content_db.find_one(content.id))

    def test_link_create(self):
        link_db = self.db.LinkDatabase(self.db.mydb)
        link = link_db.create_link("http://example.com", 1)
        self.assertIsNotNone(link)

    def test_link_find_many(self):
        link_db = self.db.LinkDatabase(self.db.mydb)
        links = link_db.find_many()
        self.assertIsInstance(links, list)

    def test_link_update(self):
        link_db = self.db.LinkDatabase(self.db.mydb)
        link = link_db.create_link("http://example.com", 1)
        updated_link = link_db.update_link(link.id, "http://updated-example.com", 2)
        self.assertEqual(updated_link.link, "http://updated-example.com")
        self.assertEqual(updated_link.topic_id, 2)

    def test_link_delete(self):
        link_db = self.db.LinkDatabase(self.db.mydb)
        link = link_db.create_link("http://example.com", 1)
        link_db.delete_link(link.id)
        self.assertIsNone(link_db.find_one(link.id))

