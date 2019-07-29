import json
import xlsxwriter
import string

alphabet = str(string.ascii_uppercase)
# props
#  - columns
#  - items - array of objects
# - fileName - file name path of output file
def write(props):
    columns = props['columns']
    fileName = props['fileName']
    items = props['items']

    print 'WRITE EXCEL-----------------------------'

    # Make excell file
    workbook = xlsxwriter.Workbook(fileName)
    worksheet = workbook.add_worksheet()

    # Set Styles
    label_format = workbook.add_format({
        'bold': True,
        'font_color': '#ffffff',
        'bg_color': '#392061'
    })

    # Write Titles
    index = 0
    for letter in alphabet:
        if letter in columns:
            worksheet.write( letter+'1', columns[letter]['label'].upper(), label_format)
            worksheet.set_column(index,index,columns[letter]['width']) #
            index += 1
        else:
            break

    # Yes in another for loop because I want to keep functionality separate
    rownumber = 2
    for item in items:
        for letter in alphabet:
            if letter in columns:
                # key exists in item
                if columns[letter]['label'] in item:
                    worksheet.write(letter+str(rownumber), item[columns[letter]['label']] )
                # Write Blank
                else:
                    worksheet.write(letter+str(rownumber), ' ')
            else:
                break
        rownumber += 1

    print 'close....'
    workbook.close()














#
