from setuptools import setup, find_packages
from typing import List


HYPEN_E_DOT = "-e ."

# Read the long description from README.md if available
with open("README.md", "r", encoding="utf-8") as f:
    long_description = f.read()


def get_requirements(file_path: str) -> List[str]:
    """
    Reads a requirements.txt file and returns a list of dependencies.

    Args:
        file_path (str): Path to the requirements file.

    Returns:
        List[str]: A list of dependency strings.
    """
    get_requirements = []
    with open(file_path) as file_obj:
        requirements = file_obj.readlines()
        requirements = [req.replace("\n", "") for req in requirements]

        if HYPEN_E_DOT in requirements:
            requirements.remove(HYPEN_E_DOT)

    return requirements


# Define the setup configuration
setup(
    name="ML_MLOps_MLFlow_Pipeline",
    version="0.0.1",  # Initial release version (Semantic Versioning)
    author="Swapnil Khot",  # Your name or organization
    author_email="Swapnil2Khot@gmail.com",  # Your contact email
    description="ML Pipeline Framework with MLFlow",  # A one-line description
    long_description=long_description,  # Detailed project description
    long_description_content_type="text/markdown",
    # Project URL (e.g., GitHub)
    url="https://github.com/mobndash/E2E-ML-Pipeline-MLOps-MLFlow.git",
    # find_packages() is a utility from setuptools that automatically finds all Python packages and sub-packages in your project directory
    # Looks for any directory containing an __init__.py file
    packages=find_packages(),
    # External dependencies required for your project
    install_requires=get_requirements("requirements.txt")
)
