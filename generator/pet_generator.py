from generator.base_generator import BaseGenerator
from data.pet_data_class import PetDataClass


class PetGenerator(BaseGenerator):
    
    def generate_pet(
            self,
            uid=None,
            category_value=None,
            name=None,
            photo_urls=None,
            tags_value=None,
            status=None,
            urls_count=1,
            tags_count=1
        ):
        yield PetDataClass(
            uid=self.get_id(uid=uid),
            category=self.create_category(category_value=category_value),
            name=self.get_name(name=name),
            photoUrls=self.get_photo_urls(photo_urls=photo_urls, urls_count=urls_count),
            tags=self.get_tags(tags_value=tags_value, tags_count=tags_count),
            status=self.get_status(status=status)
        )       
