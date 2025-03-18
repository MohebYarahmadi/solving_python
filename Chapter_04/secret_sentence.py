# DMOJ problem coci08c3p2
# zepelepenapa papapripikapa -> zelena paprika
# bapas jepe doposapadnapa opovapa kepemipijapa - > bas je dosadna ova kemija
sentence = 'bapas jepe doposapadnapa opovapa kepemipijapa'

result = ''
i = 0

while i < len(sentence):
    result += sentence[i]
    if sentence[i] in 'aiueo':
        i += 3
    else:
        i += 1

print(result)
