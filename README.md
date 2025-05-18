# Backup Brain Project

A comparative study for the best system for knowledge management and analysis for RAG applications. The end goal of the comparative study is to create a hyper personal AI assistants. The methods compared are llm based knowledge graph construction and vector database construction with multiple chunking strategies.

## Project Structure

### 1. Auto Knowledge Graph (`auto_kg/`)
- **Purpose**: Automatically constructs and manages knowledge graphs from text documents. The AutoKG system is an implementation which combines llm based mehods for knowledge graph creation and improves it with unsupervised machine learning algorithms.
- **Key Components**:
  - `autoKG_full.py`: Core implementation of the AutoKG system
  - `utils.py`: Utility functions for knowledge graph operations
  - `raw_data/`: Contains source documents and research papers
  - `requirements.txt`: Python dependencies

### 2. Book Analysis (`book_analysis/`)
- **Purpose**: Knowledge graph and vector database creation with multiple chunking strategies for a book input
- **Key Components**:
  - Jupyter notebooks for different analysis approaches:
    - `kg_analysis.ipynb`: Knowledge graph-based analysis
    - `vec_llm.ipynb`: Vector-based LLM analysis
    - `chunk_test_*.ipynb`: Text chunking experiments
  - Supporting directories:
    - `input/`: Source documents
    - `output/`: Analysis results
    - `prompts/`: LLM prompt templates
    - `cache/`: Cached computations and results
    - `logs/`: Analysis logs

### 3. Chat Analysis 1 & 2 (`chat_analysis_1/` and `chat_analysis_2/`)
- **Purpose**: Experiment to try and see if knowledge graph could model text conversations. Inputs are empty as 
- **Key Components**:
  - `chat_kg.ipynb`: Chat-specific knowledge graph construction and analysis
  - `kg_llm.ipynb`: LLM integration for chat analysis
  - Supporting infrastructure similar to book analysis

## Key Features

1. **Automated Knowledge Graph Construction**
   - Embedding-based text analysis
   - Clustering and keyword extraction
   - Graph-based text segmentation
   - Semantic search capabilities

2. **Advanced Text Analysis**
   - Multiple chunking strategies
   - LLM-powered text understanding
   - Knowledge graph visualization
   - Cached computations for efficiency

## Technologies Used

- OpenAI API for embeddings and LLM capabilities
- NetworkX for graph operations
- ChromaDB for vector database
- GraphRag for knowledge graph
- Scikit-learn for clustering and nearest neighbors
- LangChain for LLM interactions
- Jupyter notebooks for interactive analysis

## Getting Started

1. Install dependencies:
   ```bash
   pip install -r auto_kg/requirements.txt
   ```

2. Set up your OpenAI API key in the appropriate configuration files

3. Follow the example usage in the main scripts or notebooks

## License

See the [LICENSE](LICENSE) file for details.