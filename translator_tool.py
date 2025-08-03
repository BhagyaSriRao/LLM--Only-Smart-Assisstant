from googletrans import Translator

def translate_to_german(text):
    translator = Translator()
    try:
        result = translator.translate(text, dest='de')
        return result.text
    except Exception as e:
        return f"Translation error: {str(e)}"
