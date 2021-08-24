# leads-diff

[![Code style: black](https://img.shields.io/badge/code%20style-black-000000.svg)](https://github.com/psf/black)

This project is a simple CLI to compare two sheets of Leeds in an excel file by a column. This CLI solves my girlfriend problem to understand who is incoming and who outgoing to keep your leads database always updated.

## Install

Install in edit mode

```shell
$ pip install -e .
```


## Usage 

To run and read sheets with name "novo" and "antigo"

```shell
$ leads -e ~/Downloads/lista-leads.xlsx
```

To override sheet names

```shell
$ leads -n novo -o antigo -e ~/Downloads/lista-leads.xlsx
```


Show available commands

```
$ leads --help

Usage: leads [OPTIONS]

Options:
  -n, --new TEXT    Nome da folha do excel com os novos leads.
  -o, --old TEXT    Nome da folha do excel com os leads antigos.
  -e, --excel TEXT  Caminho relativo do arquivo excel.  [required]
  --help            Show this message and exit.

```



