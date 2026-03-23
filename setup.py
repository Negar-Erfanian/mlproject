from setuptools import setup, find_packages
from typing import List


HYPHEN_E_DOT='-e .'
def get_requirements(filename: str) -> List[str]:
    '''
    This function will return the list of requirements
    :param filename: txt file path
    :return: list of requirements
    '''
    requirements = []
    with open(filename) as file_obj:
        requirements = file_obj.readlines()
        requirements = [req.replace("\n", "") for req in requirements]

        if HYPHEN_E_DOT in requirements:
            requirements.remove(HYPHEN_E_DOT)

    return requirements

setup(
    name='mlproject',
    version='0.0.1',
    author='Negar',
    author_email='n.erfanian93@gmail.com',
    packages=find_packages(),
    install_requires=get_requirements('requirements.txt'),
)