from summarizer import (
    FileReader, AbstractiveSummarizer
)


class CommandLineApplication:
    """
    Command Line Application for the chatbot
    """
    def __init__(self) -> None:
        self.engine = AbstractiveSummarizer()

    def run_program(self) -> None:
        print("Summarizer: \n\n")
        q = str(input("> Type either text of file: "))

        if q.lower().strip() == 'file':
            Q = str(input("> .txt or .pdf file path: "))
            Q = FileReader(Q)
            Q = Q.text
        else:
            Q = str(input("> Text to summarize or .txt or .pdf file path: "))

        R = self.engine.inference(Q)
        print(f">>> SUMMARY: {R}")


if __name__ == "__main__":
    app = CommandLineApplication()
    app.run_program()
