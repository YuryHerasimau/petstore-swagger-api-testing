from faker import Faker
import random


class BaseGenerator:

    faker = Faker("En")

    def get_id(self, uid):
        if uid is None:
            return random.randint(10000, 99999)
        return uid

    def create_category(self, category_value, uid=None, name=None):
        if category_value is None:
            category = {
                "id": self.get_id(uid),
                "name": self.get_name(name)
            }
            return category
        return category_value

    def get_name(self, name):
        if name is None:
            return self.faker.name().split()[0]
        return name

    def get_photo_urls(self, photo_urls):
        if photo_urls is None:
            return self.faker.image_url()
        return photo_urls

    def get_tags(self, tags_value, uid=None, name=None):
        lst = []
        if tags_value is None:
            tags = {
                "id": self.get_id(uid),
                "name": self.get_name(name)
            }
            lst.append(tags)
            return lst
        return tags_value

    def get_status(self, status):
        if status is None:
            return "available"
        return status