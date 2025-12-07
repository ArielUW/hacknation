import spacy
from spacy.tokens import DocBin
from tqdm import tqdm
import json
import pandas as pd
from spacy import displacy
from pathlib import Path
from multiprocessing import Pool
import typer
from loguru import logger
from typing_extensions import Annotated
from huggingface_hub import login

def anonymize():
    nlp = spacy.load('./content/output/model-best')

def main(
        source: Annotated[Path, typer.Option(help="Path to the text (txt format) that is supposed to be anonymized.")],
        model: Annotated[Path, typer.Option(help="Optional – path to the model you want to use. Default model location: ./content/output/model-best")] = "./content/output/model-best",
        output: Annotated[Path, typer.Option(help="Optional – path to the location where the output shoul be exported.")] = None,
):
    if source.endswith(".txt"):
        anonymize()
    else:
        logger.warning(f"Unexpected filename: {f}. Input file is skipped. Please input a .txt file.")

if __name__ == "__main__":
    typer.run(main)
    #python3 anonymizer.py --source