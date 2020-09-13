class Word(object):
    def __init__(self, word, pronunciation, definitions):
        self.word = word
        self.pronunciation = pronunciation
        self.definitions = [
            {
                "type": definitions.type,
                "definition": definitions.definition,
                "example": definitions.example,
                "image_url": definitions.image_url,
                "emoji": definitions.emoji
            }
        ]

class CodeFile(object):
    def __init__(self, name, content):
        self.name = name
        self.content = content

    def get_name(self):
        return self.name
    def get_content(self):
        return self.content