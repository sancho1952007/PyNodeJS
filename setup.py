from setuptools import setup, find_packages
setup_args=dict(
    name="PyNodeJS",
    version='1.0',
    author="Sancho Godinho",
    description="A Module to Use Some Node JS Keywords In Python!",
    long_description="Please See Docs on: https://github.com/sancho1952007/PyNodeJS",
    packages=["pynodejs"],
    keywords=['require', 'console.log'],
    url="https://github.com/sancho1952007/PyNodeJS",
    license_files = ('LICENSE.txt'),
    project_urls={
        "Bug Tracker": "https://github.com/sancho1952007/PyNodeJS/issues"
    }
)
install_requires=[]

setup(**setup_args, install_requires=install_requires)