## Tech Stack

- Python
- Flask
- SQLAlchemy

## Setup Instructions

### Prerequisites
- Python 3.8+
- pip

### Installation

1. Clone the repository:
```bash
git clone https://github.com/frenemy17/cold-case-rag-project.git
cd cold-case-rag-project
```

2. Create a virtual environment:
```bash
python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate
```

3. Install dependencies:
```bash
pip install -r requirements.txt
```

4. Set up environment variables:
```bash
export GOOGLE_API_KEY="your-api-key-here"  # On Windows: set GOOGLE_API_KEY=your-api-key-here
```

5. Add evidence files:
Place your evidence files (`.txt` format) in the `data/` directory.

### Running the Project

- **Embed evidence**: `python embed.py` - Processes evidence and builds the vector index
- **Query the system**: Import `ask_rag` from `rag.py` and call `ask_rag("your question")
