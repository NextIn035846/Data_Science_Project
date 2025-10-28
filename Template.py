import os 
from pathlib import Path
import logging

logging.basicConfig(level=logging.INFO, format='[%(asctime)s]: %(message)s:')


list_of_files = [
  # ".github/workflows/.gitkeep", This Is use when You Want to Push Empty Directories
   ".github/workflows/ci.yaml",
   "config/__init__.py",
   "config/logging_config.yaml",
   "config/model_config.yaml",
   "config/prompt_template.yaml",
   "ai_data_science_team/multiagents/pandas_data_analyst.py",
   "ai_data_science_team/multiagents/__init__.py",
   "ai_data_science_team/templates/__init__.py",
   "ai_data_science_team/templates/agent_templates.py",
   "ai_data_science_team/agents/data_wrangling_agent.py",
   "ai_data_science_team/agents/__init__.py",
   "ai_data_science_team/parsers/parsers.py",
   "ai_data_science_team/parsers/__init__.py",
   "ai_data_science_team/utils/__init__.py",
   "ai_data_science_team/utils/regex.py",
   "ai_data_science_team/utils/logging.py",
   "ai_data_science_team/utils/plotly.py",
   "ai_data_science_team/tools/dataframe.py",
   "ai_data_science_team/tools/__init__.py",
   "init_setup.sh",
   "requirements.txt", 
   "requirements_dev.txt",
   "setup.py",
   "setup.cfg",
   "app.py"
   "pyproject.toml",
   "tox.ini",
]


for filepath in list_of_files:
    filepath = Path(filepath)
    filedir, filename = os.path.split(filepath)

    if filedir != "":
        os.makedirs(filedir, exist_ok=True)
        logging.info(f"Creating directory:{filedir} for the file {filename}")

    
    if (not os.path.exists(filepath)) or (os.path.getsize(filepath) == 0):
        with open(filepath,'w') as f:
            pass
            logging.info(f"Creating empty file: {filepath}")


    
    else:
        logging.info(f"{filename} is already exists")
