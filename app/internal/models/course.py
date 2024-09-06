from beanie import Document

class Course(Document):
    name : str
    description : str
    category  : str
    tags : list[str]
    autor : str
    class Settings:
        name = 'courses'