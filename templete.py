import os
from pathlib import Path
import logging

# Set up logging configuration
# This will help log messages with timestamps and custom formatting
logging.basicConfig(level=logging.INFO, format='[%(asctime)s] : %(message)s :')

# Define the project name to be used in file paths
project_name = "TextSummarizer"

# List of file paths to be created for the project structure
list_of_files = [
    ".github/workflows/.gitkeep",                             # GitHub Actions workflow placeholder
    f"src/{project_name}/__init__.py",                        # Package initializer for the main module
    f"src/{project_name}/components/__init__.py",             # Package initializer for components submodule
    f"src/{project_name}/utils/__init__.py",                  # Package initializer for utils submodule
    f"src/{project_name}/utils/common.py",                   # Common utility functions
    f"src/{project_name}/logging/__init__.py",                # Custom logging setup (if needed)
    f"src/{project_name}/config/__init__.py",                 # Config package initializer
    f"src/{project_name}/config/configuration.py",           # Configuration settings
    f"src/{project_name}/pipeline/__init__.py",               # Pipeline logic initializer
    f"src/{project_name}/entity/__init__.py",                 # Entities or data models
    f"src/{project_name}/constants/__init__.py",              # Constants used throughout the project
    "config/config.yaml",                                     # YAML config file for project parameters
    "params.yaml",                                            # Hyperparameters or global settings
    "app.py",                                                 # FastAPI/Flask app or main app logic
    "main.py",                                                # Entry point for running the project
    "Dockerfile",                                             # Dockerfile for containerizing the app
    "requirements.txt",                                       # Python dependencies
    "setup.py",                                               # Setup script for packaging
    "research/trials.ipynb",                                   # Jupyter notebook for experimentation

]

# Loop through each file path and convert it into a Path object
# (You can add logic here to actually create files/directories if needed)
for filepath in list_of_files:
    filepath = Path(filepath)
    filedir ,filename = os.path.split(filepath)
    if filedir != "":
        os.makedirs(filedir, exist_ok=True)  # Create directories if they don't exist
        logging.info(f"Creating directory: {filedir} for the file: {filename}")
    
    
    if (not os.path.exists(filepath)) or (os.path.getsize(filepath) == 0):
        with open(filepath, 'w') as f:
            pass
        logging.info(f"Creating empty file: {filepath}")
        
    else:
        logging.info(f"{filename} is already exists")
