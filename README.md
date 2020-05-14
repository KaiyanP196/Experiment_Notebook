# Experiment_Notebook

[![PyPI Version](https://img.shields.io/pypi/v/Experiment_Notebook.svg)](https://pypi.org/project/Experiment_Notebook/)
[![Supported Python Versions](https://img.shields.io/pypi/pyversions/Experiment_Notebook.svg)](https://pypi.org/project/Experiment_Notebook/)

`expnbk` provides a class for creating an experiment with its own results directory that automatically contains a copy of the code used to run the experiment. Super useful for reproducibility.

---

## Installation

To install Experiment_Notebook, run this command in your terminal:

```bash
$ pip install -U Experiment_Notebook
```

This is the preferred method to install Experiment_Notebook, as it will always install the most recent stable release.

If you don't have [pip](https://pip.pypa.io) installed, these [installation instructions](http://docs.python-guide.org/en/latest/starting/installation/) can guide you through the process.



## Quick Start

The `expnbk` package provides a class `Experiment`. Upon instantiation,  it takes a snapshot of the current working directory and saves all files into a `results/current_time` folder within the current directory (see `Usage` for variations). It also provides functions that automatically save figures to the same output directory. Check out the following example and you shall see similar changes in your directories.  
```
$ tree
    .
    ├── file1        
    └── dir1
        └── file2
```
```python
>>> from expnbk import Experiment
>>> exp = Experiment()
>>> fig = exp.figure()
>>> fig.savefig("image1.png") 
```
```
$ tree
    .
    ├── file1
    ├── dir1
    │   └── file2
    └── results
        └── 2020-12-31_123006
            ├── <project_name>
            │   ├── file1
            │   └── dir1
            │       └── file2
            └── image1.png
```



## Usage

- Import the `expnk` package:
```python
>>> from expnbk import Experiment
```



- Create an `Experiment` class with attributes:

```python
>>> exp = Experiment(expname='some_experiemnt', results_dir='path_to_results_directory', copy_code=True, ignore_dirs=None):
```
`expname`: str, optional

       A name identifying the type of experiment run.
   
`results_dir` : str, optional

       Path to the desired results directory for storing experiment details.
   
`copy_code` : bool, optional

        Should the experiment results include the code used to generate them?
   
`ignore_dirs` : list(str), optional

        Any directories that should not be copied with the code.



- Save figures to the same output directory as above: 
```python
>>> fig = exp.figure() //Get a matplotlib figure
>>> fig.savefig("image1.png") //`savefig` function will put it in the experiment directory
```
