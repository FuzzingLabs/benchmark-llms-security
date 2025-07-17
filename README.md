# Benchmarking LLMs for vulnerability research

A comprehensive benchmark evaluating different Large Language Models on their ability to identify and analyze security vulnerabilities in code.
Blogpost link : 

## Usage

```bash
python3 llm-audit-tool/vulnerability_scanner.py --openrouter [openrouter/openai] --model [model]
```

## Project Structure

- **`llm-audit-tool/`** - Core vulnerability research agent implementation
- **`model_stats/`** - Individual performance statistics for each tested model
- **`statistics/`** - Aggregated benchmark results in JSON and CSV format
- **`vuln-app/`** - Reference vulnerable application containing test cases
- **`benchmark.png`** - Final benchmark visualization and results

## Quick Start

1. Install dependencies
2. Define your openrouter or openai key in llm-audit-tool/llm_service.py
3. Run the audit tool with your preferred model provider and model
4. View results in the new folder created at the root with the name of the model. (you don't need to do it as the results are already in models_stats/ or final_statistics/

## Results

[image](benchmark.png)
