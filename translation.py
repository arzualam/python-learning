acronyms = {'LOL': 'lough out loud',
            'IDK': 'I dont know',
            'TBH': 'To be honest'}

sentence = 'IDK' + ' what happened ' + 'TBH'
translation = acronyms.get('IDK') + ' what happened ' + acronyms.get('TBH')

print('sentence:', sentence)
print('translation:', translation)