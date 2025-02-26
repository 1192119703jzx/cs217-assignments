import json

class NoteBook:
    def __init__(self, json_file):
        self.json_file = json_file
        with open(json_file, 'r') as file:
            self.book = json.load(file)

    def create_note(self, name, content):
        self.book[name] = content
        self.save_to_json()

    def show_all_notes(self):
        return self.book.keys()

    def search_string(self, string):
        result = []
        for note_name, note_content in self.book.items():
            if string in note_content:
                result.append(note_name)
        return result
    
    def search_name(self, name):
        if name in self.book:
            return self.book[name]
        return None
    
    def save_to_json(self):
        with open(self.json_file, 'w') as file:
            json.dump(self.book, file, indent=4)

    def name_exists(self, name):
        if name in self.book:
            return name
        return None
    
    def string_string_in_name(self, string):
        return [name for name in self.book if string in name]
        