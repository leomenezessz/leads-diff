import click

from leads.data import DataFormatter
from leads.validators import validate_excel_file_param


@click.command()
@click.option(
    "--new", "-n", default="novo", help="Nome da folha do excel com os novos leads."
)
@click.option(
    "--old", "-o", default="antigo", help="Nome da folha do excel com os leads antigos."
)
@click.option(
    "--excel",
    "-e",
    help="Caminho relativo do arquivo excel.",
    required=True,
    callback=validate_excel_file_param,
)
def main(new, old, excel):
    try:
        leads_to_add, leads_to_remove = DataFormatter(
            excel_file_path=excel, new_leads_sheet=new, old_leads_sheet=old
        ).leads_diff()
        click.echo(
            f"=================== Listagem de leads para remover =================== \n {leads_to_remove} \n"
        )
        click.echo(
            f"=================== Listagem de leads para adicionar =================== \n {leads_to_add} \n"
        )
    except ValueError as e:
        raise click.UsageError(e.__str__())
