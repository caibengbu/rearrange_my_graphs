import setuptools

setuptools.setup(
   name='rearrange_my_graphs',
   version='0.1',
   description='Rearrange My Graphs',
   author='Ye Sun',
   author_email='ye.sun1@sciencespo.fr',
   classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
   ],
   package_dir={"": "src"},
   packages=setuptools.find_packages(where="src"),
   install_requires=['pandas'], #external packages as dependencies
   python_requires=">=3.7"
)