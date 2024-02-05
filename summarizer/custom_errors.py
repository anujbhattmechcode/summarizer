class NotRequiredFile(Exception):

    def __init__(self, message="Not a PDF FIle"):
        self.message = message

    def __str__(self):
        return self.message

    def __repr__(self):
        return self.message


class ModelLoadingError(Exception):

    def __init__(self, message="Failed to load the model!"):
        self.message = message

    def __str__(self):
        return self.message

    def __repr__(self):
        return self.message


class DataTooBig(Exception):

    def __init__(self, message="Given data is too big!"):
        self.message = message

    def __str__(self):
        return self.message

    def __repr__(self):
        return self.message


class InferenceError(Exception):

    def __init__(self, message="Problem during model inference"):
        self.message = message

    def __str__(self):
        return self.message

    def __repr__(self):
        return self.message
