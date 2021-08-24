from os.path import abspath
from pathlib import Path

import click


_VALID_FILES = (".xls", ".xlsx")


def validate_excel_file_param(ctx, param, value):
    if Path(value).suffix in _VALID_FILES and Path(value).is_file():
        return abspath(value)
    raise click.BadParameter(f"The file '{value}' is invalid or don't exists.")
