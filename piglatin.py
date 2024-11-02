class PigLatin:

    def __init__(self, phrase: str):
        self.phrase = phrase
        self.vowels = tuple("aeiou")

    def retrieve_phrase(self) -> str:
        return self.phrase

    def convert(self) -> str:
        if not self.phrase:
            return "nil"
        punctuation = ""
        if self.phrase.endswith(tuple(".,;:'?!()")):
            punctuation = self.phrase[-1]
            self.phrase = self.phrase[:-1]

        separator = "-" if "-" in self.phrase else " "
        words = self.phrase.split(separator)
        translated = []

        for word in words:
            upper = word.isupper()
            title = word.istitle()

            word = word.lower()
            while not word.startswith(self.vowels):
                word = f"{word[1:]}{word[0]}"

            if word.endswith("y"):
                translation = f"{word}nay"
            elif word.endswith(self.vowels):
                translation = f"{word}yay"
            else:
                translation = f"{word}ay"

            if upper:
                translation = translation.upper()
            elif title:
                translation = translation.capitalize()

            translated.append(translation)

        return separator.join(translated) + punctuation
