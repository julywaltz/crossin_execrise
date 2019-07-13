h = float(input('身高（m)：'))
w = float(input('体重（kg）：'))
bmi = w / (h**2)
if bmi < 18.5:
    print("BMI=%d体重偏轻" % bmi)
elif 18.5 <= bmi < 24:
    print('BMI=%d，体重正常' % bmi)
else:
    print('BMI=%d，体重偏重' % bmi)
