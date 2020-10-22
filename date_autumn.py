def date_autumn(date):
    sp_month_au = []
    for data in date:
        data = data.split('-')
        if data[0] == '09' or data[0] == '10' or data[0] == '11':
            sp_month_au.append(data)
    data = sp_month_au[0]
    maxx = int(data[0]) * 30 + int(data[1]) + int(data[2])
    for i in range(len(sp_month_au)):
        if int(sp_month_au[i][0]) * 30 + int(sp_month_au[i][1]) \
                + int(sp_month_au[i][2]) * 365 > maxx:
            maxx = int(sp_month_au[i][0]) * 30 + \
                   int(sp_month_au[i][1]) + int(sp_month_au[i][2]) * 365
            data = sp_month_au[i]
    return '-'.join(data)
