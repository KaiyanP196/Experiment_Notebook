import datetime
import os
import shutil
import matplotlib.pyplot as plt
import types

class Experiment:
    """An experiment, complete with a corresponding results directory.

    Example
    -------
    $ tree
    .
    ├── file1
    └── dir1
        └── file2
    $ python
    >>> from experiment import Experiment
    >>> exp = Experiment()
    >>> fig = exp.figure()
    >>> fig.savefig("image1.png")
    >>> exp.savefig("image2.png")
    >>> exit()
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
            ├── image1.png
            └── image2.png


    Parameters
    ----------
    expname : str, optional
        A name identifying the type of experiment run.
    results_dir : str, optional
        Path to the desired results directory for storing experiment details.
    copy_code : bool, optional
        Should the experiment results include the code used to generate them?
    ignore_dirs : list(str), optional
        Any directories that should not be copied with the code.

    Attributes
    ----------
    dirname : str
        Name of the directory for this experiment.
    dirpath : str
        Full path to the results directory for this experiment.
    """

    def __init__(self, expname=None, results_dir=None, copy_code=True, ignore_dirs=None):
        if ignore_dirs is None:
            ignore_dirs = []

        self.cwd = os.getcwd()

        now = datetime.datetime.now()
        dirname_parts = []
        if expname is not None:
            dirname_parts.append(expname)

        dirname_parts.append(now.strftime("%Y-%m-%d"))
        dirname_parts.append(now.strftime("%H%M%S"))
        self.dirname = "_".join(dirname_parts)

        if results_dir is None:
            results_dir = os.path.join(self.cwd, "results")
            ignore_dirs.append("results")

        self.dirpath = os.path.join(results_dir, self.dirname)
        os.makedirs(self.dirpath)

        if copy_code:
            src_dir = self.cwd
            dst_dir = os.path.join(self.dirpath, os.path.basename(self.cwd))

            def _ignore(directory, contents, ignore_dirs=ignore_dirs):
                if directory == src_dir:
                    return [name for name in ignore_dirs if name in contents]
                return []

            shutil.copytree(src_dir, dst_dir, ignore=_ignore)

    def figure(self, *args, **kwargs):
        """Get a matplotlib figure whose `savefig` function will put it in the experiment directory."""
        fig = plt.figure(*args, **kwargs)
        old_savefig = fig.savefig
        def new_savefig(_self, fname, *args, **kwargs):
            filepath = os.path.join(self.dirpath, fname)
            return old_savefig(os.path.join(self.dirpath, fname), *args, **kwargs)
        fig.savefig = types.MethodType(new_savefig, fig)
        return fig

    def savefig(self, fname, *args, **kwargs):
        filepath = os.path.join(self.dirpath, fname)
        plt.savefig(filepath, *args, **kwargs)



if __name__ == "__main__":
    exp = Experiment()
    fig = exp.figure()
    fig.savefig("image1.png")
    exp.savefig("image2.png")

    import sys
    print(sys.argv)

