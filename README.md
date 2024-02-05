## Summarizer ##
This module intends to summarize any input given to it. It can have text file or pdf as input or direct text as well.
For training or fine-tuning, run the abstractive summarizer training pipe example.

### FileReader Class ###
One can use FileReader class to read the .pdf or .txt file
```python
from summarizer import FileReader

data = FileReader("any_pdf-or-text_file.pdf",
                  max_words=512)
print(data.text)
print(data.total_words)
print(data.total_characters)
```

### Example ###
1. Use summarizer module directly
```python
from summarizer import AbstractiveSummarizer, FileReader

if __name__ == "__main__":
    summerize = AbstractiveSummarizer()
    data_reader = FileReader("data/thermodynamics.txt")
    print(data_reader.total_words)
    print(data_reader.total_characters)
    output = summerize.inference(data_reader.text)

    print(output)
```

2. Run the summarizer module in CMD
Run the following command in the command line
```bash
foo@bar:~$ python run_in_cmd.py
```
It will give the following output
```bash
> Type either text of file: File
> .txt or .pdf file path: data/thermodynamics.txt
File Read operation initiated
File Read operation Done in 0.01279 seconds

SUMMARY: Thermodynamics is a branch of physics that deals with heat, work, and temperature. The behavior of these quantities is governed by the four laws of thermodynamics. Thermodynamics applies to a wide variety of topics in science and engineering.
```
