kn = int(input('Введите кнаты\n'))

gl = kn // (29*17)
ost_kn = (kn - (gl * 17 * 29))
skil = (kn - (gl * 17 * 29)) // 29

if gl != 0: print(gl, 'галлеонов')
if skil != 0: print(skil, 'скилев')
if ost_kn != 0: print(ost_kn, 'кнатов')
