# prodigy-partition.py
from prodigy.components.db import connect
import typer
from pathlib import Path
import srsly
import random
import shutil


def main(prodigy_data: str, out_dir: Path, fraction: float = 0.2, seed: int = 0):
    """Partition the data into train/test/dev split."""
    random.seed(seed)
    db = connect()
    examples = db.get_dataset(prodigy_data)
    random.shuffle(examples)
    dev_size = int(fraction * len(examples))
    test_size = int(fraction * len(examples))
    train_size = (len(examples) - dev_size) - test_size
    if out_dir.exists():
        shutil.rmtree(out_dir)

    out_dir.mkdir(parents=True)
    srsly.write_jsonl(out_dir / "train.jsonl", examples[:train_size])
    srsly.write_jsonl(out_dir / "dev.jsonl", examples[train_size : train_size + dev_size])
    srsly.write_jsonl(out_dir / "test.jsonl", examples[train_size + dev_size :])


if __name__ == "__main__":
    typer.run(main)