import xlsxwriter
class ReportGenerator:

    def __init__(self, name="export.xlsx"):
        self.exp_name = str(name)

    def generate_excel(self, collen, elist):
        self.col_len = (collen)
        self.exp_list = list(elist)

        workbook = xlsxwriter.Workbook(self.exp_name)
        worksheet = workbook.add_worksheet()
        bold = workbook.add_format({'bold':True})
        worksheet.set_column('A:A', (self.col_len), bold)
        for i in range (len(self.exp_list)):
            worksheet.write_row(i, 0, self.exp_list[i])
        workbook.close()
        print("<<<<Export to excel successful>>>>>")
