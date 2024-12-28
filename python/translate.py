# from googletrans import Translator

# translator= Translator()

# bangla_text = "আমি বাংলায় কথা বলি"

# translated = translator.translate(bangla_text,src='bn',dest='en')

# print("Translated text: ",translated.text)


from deep_translator import GoogleTranslator

# Bangla text to translate
bangla_text = "Si"#"আমি বাংলায় কথা বলি"

# Translate from Bangla to English
translated = GoogleTranslator(source='es', target='en').translate(bangla_text)

# Print the translated text
print("Translated Text:", translated)