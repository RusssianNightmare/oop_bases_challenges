"""
У нас есть класс TextProcessor, который содержит в себе методы для работы с текстом.

Задания:
    1. Создайте класс AdvancedTextProcessor, который будет наследником TextProcessor.
    2. Переопределите метод summarize у класса AdvancedTextProcessor таким образом, чтобы он возвращал еще и количество слов в тексте.
       Например: Total text length: 67, total number of words in the text: 10
    3. Создайте экземпляры каждого из двух классов и у каждого экземпляра вызовите все возможные методы.
"""


class TextProcessor:
    def __init__(self, text):
        self.text = text

    def to_upper(self):
        return self.text.upper()

    def summarize(self):
        return f'Total text length: {len(self.text)}'


class AdvancedTextProcessor(TextProcessor):
    def __init__(self, text):
        super().__init__(text)
    def to_upper(self):
        return super().to_upper()
    def summarize(self):
        words = self.text.split()
        count = len(words)
        return f'Total text length: {len(self.text)}, total number of words in the text: {count}'

if __name__ == '__main__':
    texts = TextProcessor('Total text length: 67, total number of words in the text: 10')
    print(texts.to_upper())
    print(texts.summarize())

    advance = AdvancedTextProcessor('Total text length: 67, total number of words in the text: 10')
    print(advance.to_upper())
    print(advance.summarize())
