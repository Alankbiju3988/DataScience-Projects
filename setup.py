from setuptools import find_packages,setup
from typing import List
hyphen_e_dot='-e .'
def get_requirements(file_path:str)-> List[str]:
    ''' 
    this function returns the list of requirements
    '''
    requirements=[]
    with open(file_path) as file_obj:
        requirements=file_obj.readlines()
        requirements=[req.replace('\n','') for req in requirements]
        
        if hyphen_e_dot in requirements:
            requirements.remove(hyphen_e_dot)
    return requirements

setup(
    name='Data Science project',
    version='0.01',
    author='Alan K Biju',
    author_email='alankbijualan@gmail.com',
    packages=find_packages(),
    install_requires=get_requirements('Requirements.txt')

)
