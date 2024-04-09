# Muhammad Sohaib Zafar P200574 Assignment 01

#Sentences Counter
def count_sentences(text):
    sentence_terminators = ['.', ':', ';', '?', '!']
    count = 0
    for char in text:
        if char in sentence_terminators:
            count += 1
    return max(1, count)  

#Words Counter
def count_words(text):
    return len(text.split())

#Characters Counters
def count_characters(text):
    alphanumeric_chars = sum(c.isalnum() for c in text)
    return alphanumeric_chars

#Formula for ARI
def calculate_ARI(characters, words, sentences):
    ARI = 4.71 * (characters / words) + 0.5 * (words / sentences) - 21.43
    return round(ARI)

#Text file handling
def process_text_file(file_path):
    with open(file_path, 'r') as file:
        text = file.read()
        sentences = count_sentences(text)
        words = count_words(text)
        characters = count_characters(text)
        ARI = calculate_ARI(characters, words, sentences)
        return sentences, words, characters, ARI

def main(directory):
    for filename in os.listdir(directory):
        if filename.endswith('.txt'):
            file_path = os.path.join(directory, filename)
            sentences, words, characters, ARI = process_text_file(file_path)
            print(f"Text File: {filename}")
            print(f"Number of sentences: {sentences}")
            print(f"Number of words: {words}")
            print(f"Number of characters: {characters}")
            print(f"Readability index: {ARI}")
            print()

if __name__ == "__main__":
    directory = "/content/drive/MyDrive/ai"
    main(directory)
