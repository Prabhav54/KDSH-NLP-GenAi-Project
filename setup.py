from setuptools import find_packages, setup
from typing import List

HYPHEN_E_DOT = '-e .'

def get_requirements(file_path: str) -> List[str]:
    '''
    This function reads the requirements.txt file and returns a list of requirements.
    It removes '-e .' if present, as that is a command trigger, not a package.
    '''
    requirements = []
    with open(file_path) as file_obj:
        requirements = file_obj.readlines()
        # Remove newlines
        requirements = [req.replace("\n", "") for req in requirements]

        if HYPHEN_E_DOT in requirements:
            requirements.remove(HYPHEN_E_DOT)
    
    return requirements

setup(
    name='KDSH_2026_Hackathon_Solution',
    version='0.0.1',
    author='Prabhav Khare',  # Your Name
    author_email='your_email@example.com',
    packages=find_packages(),
    # Automatically install dependencies from requirements.txt
    install_requires=get_requirements('requirements.txt')
)