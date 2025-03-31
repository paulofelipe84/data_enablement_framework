# Data Enablement Framework

## Overview
The **Data Enablement Framework** provides a structured, scalable approach to ingest, transform, govern, and consume data. It integrates tools like Databricks, dbt, AutomateDV, MetricFlow, Unity Catalog, and Flow GenAI to empower users across your organisation.

## Features
- **YAML-driven Configurations** for defining data pipelines, contracts, and transformations.
- Supports both **SQL and Natural Language transformations**.
- Automated **Data Vault modeling** using AutomateDV.
- Metadata governance via **Unity Catalog**.
- Comprehensive **data governance** using Open Data Contracts.
- Metrics handling through **MetricFlow**.

## Project Structure
data-enablement-framework/ 
├── .github/ # CI/CD workflows 
├── config/ # YAML configuration files 
├── docs/ # Architecture diagrams and setup documentation 
├── src/ # Source code of the framework 
│ ├── config_parser/ # YAML parsing and validation 
│ ├── contracts/ # Data contract enforcement logic 
│ ├── orchestrator/ # Workflow orchestration logic 
│ └── transformations/ # Data transformation logic 
├── tests/ # Unit and integration tests 
├── LICENSE # Project license 
├── README.md # Project documentation 
└── requirements.txt # Python dependencies

## Quick Start

### Setup Environment
```bash
python -m venv venv
source venv/bin/activate
pip install -r requirements.txt
```

### Example YAML Configuration
Located in config/pipeline_example.yaml

### Running Tests
```bash
pytest tests/
```

## Contributing
Contributions and improvements are welcome. Please submit pull requests following best coding practices and include relevant tests.

## License
See [LICENSE](LICENSE) file.