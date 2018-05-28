import xlsxwriter
def export_excel (lsleng):
    x = list(lsleng)
    workbook = xlsxwriter.Workbook('export.xlsx')
    worksheet = workbook.add_worksheet()
    bold = workbook.add_format({'bold': True})
    worksheet.set_column('A:A', 30, bold)
    for i in range (len(x)):
        worksheet.write_row(i, 0, x[i])
    workbook.close()
    print ("<<<<Export to excel successful>>>>>")