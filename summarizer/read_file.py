import pathlib
import time

from PyPDF2 import PdfReader
from summarizer.custom_errors import NotRequiredFile, DataTooBig


class FileReader:
    """
    This class reads the .pdf or .text file and extract texts from it
    """
    def __init__(self,
                 path: str or pathlib.Path,
                 max_words: int = 1048) -> None:
        """
        :param path: (str or pathlib.Path) path to the pdf or text file
        """
        self.__max_words = max_words
        print("File Read operation initiated")
        t1 = time.perf_counter()
        self.__read_file(path)
        t2 = time.perf_counter()
        print(f"File Read operation Done in {t2 - t1:.4} seconds")

    def __read_file(self, path: str or pathlib.Path) -> None:
        if not isinstance(path, (pathlib.Path, str)):
            raise TypeError("path should be string or pathlib.Path object")
        self.__path = pathlib.Path(path)

        self.__text = ""

        if self.__path.suffix == ".pdf":
            self.__file = PdfReader(self.__path)

            for page in self.__file.pages:
                self.__text += page.extract_text()
                self.__text += "\n"

        elif self.__path.suffix == ".txt":
            with open(self.__path, "r", encoding="utf8") as F:
                self.__text = F.read()
        else:
            raise NotRequiredFile("Given path's extension is not .pdf or .txt")

        if self.total_words > self.__max_words:
            raise DataTooBig(f"More than {self.__max_words} passed!")

        # txt = ""
        # for line in self.__text.split("."):
        #     txt += f" {txt}."

        # self.__text = txt

    @property
    def text(self) -> str:
        """
        :return: Extracted text from the pdf
        """
        return self.__text

    @property
    def total_words(self) -> int:
        """
        :return: Total number of words (approx.) in the extracted text
        """
        return len(self.__text.split(" "))

    @property
    def total_characters(self) -> int:
        """
        :return: Total number of characters in the pdf
        """
        return len(self.__text)
