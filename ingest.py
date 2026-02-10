# ingest.py
from pathlib import Path
from dataclasses import dataclass
import uuid

@dataclass
class EvidenceChunk:
    id: str
    title: str
    content: str
    section: str
    source: str


def parse_file(path: Path):
    text = path.read_text(encoding="utf-8").splitlines()

    chunks = []
    section, title, buf = None, None, []

    for line in text:
        line = line.strip()

        if line.startswith("# "):
            section = line[2:]

        elif line.startswith("## "):
            if title:
                chunks.append(EvidenceChunk(
                    id=str(uuid.uuid4()),
                    title=title,
                    content="\n".join(buf),
                    section=section,
                    source=path.name
                ))
            title = line[3:]
            buf = []

        elif line:
            buf.append(line)

    if title:
        chunks.append(EvidenceChunk(
            id=str(uuid.uuid4()),
            title=title,
            content="\n".join(buf),
            section=section,
            source=path.name
        ))

    return chunks


def load_dataset(folder="data"):
    return [
        chunk
        for file in Path(folder).glob("*.txt")
        for chunk in parse_file(file)
    ]
