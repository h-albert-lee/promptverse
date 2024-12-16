# Promptverse

## This project is on develop

## Overview
Promptverse is a streamlined application designed for managing prompts, applications, datasets, and evaluations in large language model (LLM) workflows. This tool simplifies prompt versioning, YAML deployment, API evaluation, and result management through a user-friendly interface.

## Features
- **Authentication**: Secure access with admin credentials (`admin/admin`).
- **Prompt Management**:
  - Create and version prompts.
  - Activate specific prompt versions.
  - Track prompt history with timestamps.
- **Application Management**:
  - Associate prompts with specific model options.
  - Manage and retrieve application configurations.
- **Dataset Management**:
  - Upload and manage datasets for evaluation.
- **Evaluation**:
  - Perform API calls for prompt evaluations.
  - Display and analyze evaluation results.
- **YAML Integration**:
  - Export prompts to YAML files.
  - Load YAML configurations into the tool.

## Directory Structure
```
llmops_tool/
├── app.py                  # Main Streamlit application
├── backend/
│   ├── __init__.py
│   ├── auth.py             # User authentication module
│   ├── database.py         # Database schema and utility functions
│   ├── prompt_manager.py   # Prompt management functions
│   ├── application_manager.py # Application management functions
│   ├── dataset_manager.py  # Dataset management functions
│   ├── evaluation.py       # API evaluation functions
│   ├── yaml_manager.py     # YAML read/write operations
├── tests/
│   ├── test_database.py    # Unit tests for database module
│   ├── test_prompt.py      # Unit tests for prompt logic
│   ├── test_application.py # Unit tests for application management
│   ├── test_dataset.py     # Unit tests for dataset management
│   ├── test_evaluation.py  # Unit tests for API evaluation logic
│   ├── test_yaml.py        # Unit tests for YAML operations
```

## Prerequisites
- Python 3.8 or higher
- Required libraries (listed in `requirements.txt`):
  - Streamlit
  - SQLite3
  - PyYAML
  - Requests

## Installation
1. Clone the repository:
   ```bash
   git clone https://github.com/your-repo/llmops-tool.git
   cd llmops-tool
   ```
2. Install the required dependencies:
   ```bash
   pip install -r requirements.txt
   ```
3. Initialize the database (if not already set up):
   ```bash
   python -c "from backend.database import initialize_database; initialize_database()"
   ```
4. Run the application:
   ```bash
   streamlit run app.py
   ```

## Usage
1. Open the application in your web browser (default: `http://localhost:8501`).
2. Log in using the admin credentials (`admin/admin`).
3. Use the sidebar menu to navigate between the following features:
   - **Prompts**: Manage prompt creation, versioning, and history.
   - **Applications**: Define and manage LLM applications.
   - **Datasets**: Upload and manage datasets for evaluation.
   - **Evaluation**: Perform and review API evaluations.
   - **YAML Management**: Export prompts to YAML files or load them from existing YAML configurations.

## Future Enhancements
- Add user role management for multi-user environments.
- Support advanced metrics for evaluation.
- Enable more flexible dataset formats.


## Contributions
Contributions are welcome! Please fork the repository and create a pull request for any changes or enhancements.

