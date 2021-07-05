height = input('身高（公尺）')
weight = input('體重（公斤）') 
height = float(height)
weight = float(weight)
bmi_value = weight/height**2
    
def get_bmi_status_description(bmi_value):
    if bmi_value < 18.5:
        return '體重過輕囉，多吃點！'
    elif bmi_value >= 18.5 and bmi_value < 24:
        return '體重剛剛好，繼續保持！'
    elif bmi_value >= 24 :
        return '體重有點過重囉，少吃多運動！'

print('你的 BMI 指數為：{} {}'.format(bmi_value, get_bmi_status_description(bmi_value)))
