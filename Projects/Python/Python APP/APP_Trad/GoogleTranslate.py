import PyQt5
from PyQt5 import uic
from PyQt5.QtWidgets import *
import googletrans
import textblob


class GoogleTranslateUI(QMainWindow):
    def __init__(self):
        super(GoogleTranslateUI, self).__init__()
        uic.loadUi("translate.ui", self)
        self.fill_combo_boxes()
        self.connect_button()
        self.show()

    def fill_combo_boxes(self):
        list_of_languages = list(googletrans.LANGUAGES.values())
        self.input_language_combo_box.addItems(list_of_languages)
        self.output_language_combo_box.addItems(list_of_languages)

    def connect_button(self):
        self.translate_button.clicked.connect(self.translate)
        self.clear_button.clicked.connect(self.clear)

    def translate(self):
        for key, value in googletrans.LANGUAGES.items():
            if value == self.input_language_combo_box.currentText():
                from_lang_key = key

        for key, value in googletrans.LANGUAGES.items():
            if value == self.input_language_combo_box.currentText():
                from_lang_key = key

        text = textblob.TextBlob(self.input_text_edit.toPlainText())
        text = text.translate(from_lang = )

    def clear(self):
        self.input_text_edit.setText("")
        self.output_text_edit.setText("")
