import pandas
from pandas import Series

pandas.set_option("display.max_rows", None)


def _remove_series_whitespace(series: Series, field: str = "Email"):
    return series[field].str.strip()


class DataFormatter:
    def __init__(
        self, excel_file_path: str, new_leads_sheet: str, old_leads_sheet: str
    ):
        self.excel = pandas.ExcelFile(excel_file_path)
        self._new_leads_series = pandas.read_excel(self.excel, new_leads_sheet)
        self._old_leads_series = pandas.read_excel(self.excel, old_leads_sheet)

    def leads_diff(self):
        new_leads_series = _remove_series_whitespace(series=self._new_leads_series)
        old_leads_series = _remove_series_whitespace(
            series=self._old_leads_series,
        )
        return (
            self._new_leads_series[~new_leads_series.isin(old_leads_series)],
            self._old_leads_series[~old_leads_series.isin(new_leads_series)],
        )
