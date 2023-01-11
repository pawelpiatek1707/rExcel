from openpyxl import Workbook


class SaveDataController:
    def __init__(self, path: str):
        self.path = path
        self.workbook = Workbook()

    def save_base_statistics(self, data: list):
        worksheet = self.workbook.create_sheet("Statistics")
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

    def save_changes(self):
        self.workbook.save(self.path)
