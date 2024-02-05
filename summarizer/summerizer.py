from typing import Optional
from transformers import pipeline
from summarizer.custom_errors import ModelLoadingError, InferenceError


class AbstractiveSummarizer:
    """
    This class uses manually trained abstractive summarizer
    """
    def __init__(self, model_path: Optional[str] = "facebook/bart-large-cnn") -> None:
        """
        :param model_path: Either pretrained model path, trained using .ipynb file given in training folder, or Any valid
        name of model, default is bert-base-uncased, look https://huggingface.co/models for more details
        """
        self.__load_model(model_path)

    def __load_model(self, model_name):
        if not isinstance(model_name, str):
            raise TypeError("model_name should be string")

        try:
            self.__pipeline = pipeline("summarization",
                                       model=model_name,
                                       max_length=150,
                                       min_length=50)

        except Exception as E:
            raise ModelLoadingError(f"Type: {E.__class__}\nError: {E.__str__()}")

    def inference(self, text: str) -> str:
        """
        Main inference method, summarizes based on the input
        :param text: (str) Question to be asked
        :return: answer based on context
        """
        try:
            output = self.__pipeline(text)[0]
            output = output['summary_text']
        except Exception as E:
            raise InferenceError(f"Problem during inference:\n{E.__class__}: {E.__str__()}")

        return output
