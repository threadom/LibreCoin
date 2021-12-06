# tmp = {}
# tmp['owned_amount'] = lc.currencies().owned_amount()['native']
# tmp['real_invest'] = lc.currencies().real_invest()['native']
# tmp['real_gain'] = lc.currencies().real_gain()['native']

# tmp['values'] = {}
# for currency in tmp['owned_amount']:
# tmp['values'][currency] = {}
#     tmp['values'][currency]['-364'] = lc.history(currency,'EUR', -364, 86400)['close']
#     tmp['values'][currency]['-182'] = lc.history(currency,'EUR', -182, 86400)['close']
#     tmp['values'][currency]['-91'] = lc.history(currency,'EUR', -91, 21600)['close']
#     tmp['values'][currency]['-28'] = lc.history(currency,'EUR', -28, 3600)['close']
#     tmp['values'][currency]['-7'] = lc.history(currency,'EUR', -7, 900)['close']
#     tmp['values'][currency]['-1'] = lc.history(currency,'EUR', -1, 300)['close']
# tmp['values'][currency]['-0'] = lc.history(currency,'EUR', -0, 60)['close']


# add header
# line = "Currency".rjust(14) + " |"
# line += "Amount".rjust(14) + " |"
# line += "Invest".rjust(14) + " |"
# line += "Gain".rjust(14) + " |"
# line += ("Day -364").rjust(12) + " |"
# line += ("Day -182").rjust(12) + " |"
# line += ("Day -91").rjust(12) + " |"
# line += ("Day -28").rjust(12) + " |"
# line += ("Day -7").rjust(12) + " |"
# line += ("Day -1").rjust(12) + " |"
# line += ("Day -0").rjust(12) + " |"
# line += ("-7/-364").rjust(8) + " |"
# line += ("-7/-182").rjust(8) + " |"
# line += ("-7/-91").rjust(8) + " |"
# line += ("-7/-28").rjust(8) + " |"
# line += ("-1/-7").rjust(8) + " |"
# line += ("-0/-1").rjust(8) + " |"
# print(line)
# line = "".rjust(204,"-")
# print(line)
# add one line by currency and build total
# total = { 'amount' : 0, 'transactions' : 0, 'gain' : 0 }
# for currency in tmp['owned_amount']:
# Name
# line = currency.rjust(14) + " |"
# Amount
# line += lc.format(tmp['owned_amount'][currency]).auto(12) + " € |"
# total['amount'] += tmp['owned_amount'][currency]
# Invest
# line += lc.format(tmp['real_invest'][currency]).auto(12) + " € |"
# total['transactions'] += tmp['real_invest'][currency]
# Gain
# line += lc.format(tmp['real_gain'][currency]).auto(12) + " € |"
# total['gain'] += tmp['real_gain'][currency]
# line += lc.format(tmp['values'][currency]['-364']).auto(10) + " € |"
# line += lc.format(tmp['values'][currency]['-182']).auto(10) + " € |"
# line += lc.format(tmp['values'][currency]['-91']).auto(10) + " € |"
# line += lc.format(tmp['values'][currency]['-28']).auto(10) + " € |"
# line += lc.format(tmp['values'][currency]['-7']).auto(10) + " € |"
# line += lc.format(tmp['values'][currency]['-1']).auto(10) + " € |"
# line += lc.format(tmp['values'][currency]['-0']).auto(10) + " € |"
# line += lc.format(lc.sub(lc.percent(tmp['values'][currency]['-7'], tmp['values'][currency]['-364']),100)).auto(8,"%") + " |"
# line += lc.format(lc.sub(lc.percent(tmp['values'][currency]['-7'], tmp['values'][currency]['-182']),100)).auto(8,"%") + " |"
# line += lc.format(lc.sub(lc.percent(tmp['values'][currency]['-7'], tmp['values'][currency]['-91']),100)).auto(8,"%") + " |"
# line += lc.format(lc.sub(lc.percent(tmp['values'][currency]['-7'], tmp['values'][currency]['-28']),100)).auto(8,"%") + " |"
# line += lc.format(lc.sub(lc.percent(tmp['values'][currency]['-1'], tmp['values'][currency]['-7']),100)).auto(8,"%") + " |"
# line += lc.format(lc.sub(lc.percent(tmp['values'][currency]['-0'], tmp['values'][currency]['-1']),100)).auto(8,"%") + " |"
# add line
# print(line)

# add footer with total
# line = "".rjust(204,"-")
# print(line)
# line = "Total ".rjust(14) + " |"
# line += lc.format(total['amount']).auto(12) + " € |"
# line += lc.format(total['transactions']).auto(12) + " € |"
# line += lc.format(total['gain']).auto(12) + " € |"
# print(line)