import os
from pathlib import Path
import logging

# Configure logging
logging.basicConfig(level=logging.INFO, format='[%(asctime)s]: %(message)s:')

project_name = 'paper_summarizer'

list_of_files = [
    ".github/workflows/.gitkeep",
    # Main package structure
    f"src/{project_name}/__init__.py",
    f"src/{project_name}/models/__init__.py",
    f"src/{project_name}/models/model_handler.py",
    f"src/{project_name}/models/trainer.py",
    f"src/{project_name}/utils/__init__.py",
    f"src/{project_name}/utils/preprocessor.py",
    f"src/{project_name}/utils/text_utils.py",
    f"src/{project_name}/config/__init__.py",
    f"src/{project_name}/config/configuration.py",
    f"src/{project_name}/pipeline/__init__.py",
    f"src/{project_name}/pipeline/training_pipeline.py",
    f"src/{project_name}/pipeline/prediction_pipeline.py",
    f"src/{project_name}/schema/__init__.py",
    f"src/{project_name}/schema/paper_schema.py",
    f"src/{project_name}/constants/__init__.py",
    
    # Configuration files
    "config/config.yaml",
    "config/model_config.yaml",
    "params.yaml",
    
    # Data directories
    "data/raw/.gitkeep",
    "data/processed/.gitkeep",
    "data/model_outputs/.gitkeep",
    
    # Model artifacts
    "models/.gitkeep",
    
    # API related
    "api/__init__.py",
    "api/main.py",
    "api/endpoints.py",
    
    # Docker related
    "Dockerfile",
    "docker-compose.yml",
    
    # Project files
    "requirements.txt",
    "setup.py",
    "README.md",
    
    # Research and notebooks
    "research/model_experiments.ipynb",
    "research/data_analysis.ipynb",
    
    # Testing
    "tests/__init__.py",
    "tests/test_model.py",
    "tests/test_api.py",
    "tests/test_utils.py"
]

def create_project_structure():
    for filepath in list_of_files:
        filepath = Path(filepath)
        filedir, filename = os.path.split(filepath)

        if filedir != "":
            os.makedirs(filedir, exist_ok=True)
            logging.info(f"Creating directory: {filedir} for the file: {filename}")

        if (not os.path.exists(filepath)) or (os.path.getsize(filepath) == 0):
            with open(filepath, "w") as f:
                # Add default content for certain files
                if filename == "README.md":
                    f.write("# Research Paper Summarizer\n\nAI-powered tool for simplifying research papers.")
                elif filename == "requirements.txt":
                    f.write("fastapi\nuvicorn\ntransformers\ntorch\npydantic\npython-multipart\ntyping-extensions\ntqdm\npyYAML")
                elif filename == "__init__.py":
                    pass
                elif filename == "Dockerfile":
                    f.write("FROM python:3.9-slim\nWORKDIR /app\nCOPY requirements.txt .\nRUN pip install -r requirements.txt\nCOPY . .\nCMD [\"uvicorn\", \"api.main:app\", \"--host\", \"0.0.0.0\", \"--port\", \"8000\"]")
                
            logging.info(f"Creating file: {filepath}")
        else:
            logging.info(f"{filename} already exists")

if __name__ == "__main__":
    create_project_structure()