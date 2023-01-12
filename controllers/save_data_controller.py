from openpyxl import Workbook
from openpyxl.chart import BarChart, Reference


class SaveDataController:
    def __init__(self, path: str):
        self.path = path
        self.workbook = Workbook()

    def save_base_statistics(self, data: list):
        worksheet = self.workbook.active
        worksheet.title = "Statistics"
        worksheet["A1"] = "Date"
        worksheet['B1'] = "Temperature"
        row = 2
        for forecast in data:
            worksheet[f'A{row}'] = forecast["date_txt"]
            worksheet[f'b{row}'] = forecast["temperature"]
            row += 1

        worksheet[f'A{row}'] = "Average temperature"
        worksheet[f'B{row}'] = f'=AVERAGE(B2:B{row - 1})'

        worksheet[f'A{row + 1}'] = "Max temperature"
        worksheet[f'B{row + 1}'] = f'=MAX(B2:B{row})'

        worksheet[f'A{row + 2}'] = "Min temperature"
        worksheet[f'B{row + 2}'] = f'=MIN(B2:B{row})'

    def save_chart(self):
        worksheet = self.workbook.active
        chart = BarChart()
        chart.type = "col"
        chart.title = "Wykres temperatur w Katowicach"
        chart.x_axis.title = "Data"
        chart.y_axis.title = "Temperatura [°C]"
        chart.legend = None
        chart.height += 4
        chart.width += 12

        data = Reference(worksheet, min_col=2, min_row=1, max_row=41)
        cats = Reference(worksheet, min_col=1, min_row=2, max_row=41)
        chart.add_data(data, titles_from_data=True)
        chart.set_categories(cats)
        chart.shape = 4

        worksheet.add_chart(chart, "D2")

    def save_changes(self):
        self.workbook.save(self.path)
