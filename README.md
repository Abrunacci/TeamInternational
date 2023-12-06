# Data Capture Challenge
___

## System Requirements

* [pip](https://pip.pypa.io/en/stable/installation/)
* [Git](https://git-scm.com/book/en/v2/Getting-Started-Installing-Git)
* [Poetry](https://python-poetry.org/docs/)

## App set up

```shell
$ git pull https://github.com/Abrunacci/TeamInternational.git
$ cd TeamInternational
$ poetry install
$ poetry shell 
```

## Run Tests:
```shell
(teaminternational-py3.10) ~/TeamInternational$ pytest --cov
```

### Test Coverage: 100%
```shell
---------- coverage: platform linux, python 3.7.17-final-0 -----------
Name                         Stmts   Miss  Cover
------------------------------------------------
__init__.py                      0      0   100%
data_capture.py                 10      0   100%
decorators.py                   29      0   100%
stats.py                        25      0   100%
tests/__init__.py                0      0   100%
tests/test_data_capture.py      35      0   100%
------------------------------------------------
TOTAL                           99      0   100%

```

## Run:

### With DataCapture module:
```shell
(teaminternational-py3.10) ~/TeamInternational$ python
Python 3.10.12 (main, Nov 20 2023, 15:14:05) [GCC 11.4.0] on linux
Type "help", "copyright", "credits" or "license" for more information.
>>> from data_capture import DataCapture
>>> capture = DataCapture()
>>> capture.add(3)
>>> capture.add(9)
>>> capture.add(3)
>>> capture.add(4)
>>> capture.add(6)
>>> stats = capture.build_stats()
>>> stats.less(6)
3
>>> stats.greater(3)
3
>>> stats.between(4, 9)
3
```

### Without DataCapture module:
```shell
(teaminternational-py3.10) ~/TeamInternational$ python
Python 3.10.12 (main, Nov 20 2023, 15:14:05) [GCC 11.4.0] on linux
Type "help", "copyright", "credits" or "license" for more information.
>>> from stats import Stats
>>> data = [77, 89, 79, 36, 19, 87, 29, 56, 86, 6]
>>> stats = Stats(data)
>>> stats.less(36)
3
>>> stats.greater(77)
4
>>> stats.between(6, 56)
5
```