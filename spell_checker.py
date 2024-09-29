from spellchecker import SpellChecker

class spellcheckerapp:
    def __init__(self):
        self.spell = SpellChecker()

    def corrent_text(self,text):
        words = text.split()
        corrected_words = []

        for word in words:
            corrected_word = self.spell.correction(word.lower())
            if corrected_word != word.lower():
                print (f"Correcting {word} to {corrected_word}")
                corrected_words.append(corrected_word)


        return ' '.join(corrected_word)
        
    def run(self):
        print("\n---spell checker---")

        while True:
            text = input('Enter text to check (or type "exit" to quit): ')  

            if text.lower() == "exit":
                print("closing program...")
                break

            # corrected_text = self.corrent_text(text)
            # print(f"corrected text : {corrected_text}")

            try:
                corrected_text = self.corrent_text(text)
                print(f"Corrected text: {corrected_text}")
            except Exception as e:
                print(f"Error: {str(e)}")  


    

if __name__ == "__main__":
    spellcheckerapp().run()         



class SpellCheckerApp:
    def __init__(self):
        self.spell = SpellChecker()

    def correct_text(self, text):
        words = text.split()
        corrected_words = []
        
        for word in words:
            corrected_word = self.spell.correction(word.lower())
            
            if corrected_word != word.lower():
                print(f"Correcting {word} to {corrected_word}")
            
            corrected_words.append(corrected_word)
        
        return ' '.join(corrected_words)

    def run(self):
        print("\n--- Spell Checker ---")
        
        while True:
            text = input('Enter text to check (or type "exit" to quit): ')
            
            if text.lower() == "exit":
                print("Closing program...")
                break
            
            try:
                corrected_text = self.correct_text(text)
                print(f"Corrected text: {corrected_text}")
            except Exception as e:
                print(f"Error: {str(e)}")

if __name__ == "__main__":
    SpellCheckerApp().run()









