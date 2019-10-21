# Introduce
For some time past, I'm confused by how to create a Python project structure fast and flexible with mostly common used files. And that is why this project comes, ppsg means a Python project structure generator, it's inspired by this article `http://www.patricksoftwareblog.com/structure-of-a-python-project/` posted by `PATKENNEDY79@GMAIL.COM`.

```
I’ve read multiple blog posts and Stack Overflow answers on how to structure a Python project, but most of these recommendations are focused on created a python module that you can either open-source or distributed.  For a simple python project that you (and maybe just a few friends or colleagues) will be running, I’ve found the following file/folder structure to work well:

project_name/
    project_name/
        __init__.py
        ...source code files...
    test/
        __init__.py
        ...unit test files...
    docs/
        ...documentation files...
    project_name.py
    README.md
    LICENSE.md
    requirements.txt
    .gitignore
```
# How to install
You can install this package by `pip`

```
pip install ppsg-0.0.1-py3-none-any.whl
```

# How to use
This package provides a command line scripts

```
$ ppsg --help                                                                     
Usage: ppsg [OPTIONS]

  main

Options:
  -n, --name TEXT    项目名  [required]
  -d, --desc TEXT    项目介绍
  -a, --author TEXT  项目作者
  -m, --email TEXT   作者邮箱
  --help             Show this message and exit.

$ ppsg --name=haha --desc='what are you doing?' --author='me' --email='me@email.com'       
haha项目结构已创建!

$ tree -a --dirsfirst haha 
haha
├── docs
├── haha
├── test
├── .gitignore
├── CHANGELOG.md
├── LICENSE
├── README.md
├── requirement-dev.txt
├── requirement.txt
└── setup.py

3 directories, 7 files
```
