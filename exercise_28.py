x = float(input('体重(kg):'))
y = float(input('身高(m):'))
BMI = x/y/y
if BMI < 18.5:
    print('BMI=%0.2f,体重偏轻'% BMI)
elif 18.5 <= BMI < 24:
    print('BMI=%0.2f,体重正常' % BMI)
else:
    print('BMI=%0.2f,体重偏重'% BMI)
