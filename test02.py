#การรับค่าข้อมูลทางแป้นพิมพ์ด้วย Python
name = input('ป้อนชื่อ : ')
yearBorn = input('ป้อนปีเกิด : ')
print('------------------------------')
#ฟังชั่นในการแปลงข้อมูลจากข้อความเป็นตัวเลข int( ), float ( )
#ฟังชั่นในการแปลงข้อมูลจากตัวเลขเป็นข้อความ str( )
print(f'ยินดีต้อนรับ {name} เกิดปี {yearBorn} อายุ {2023 - int(yearBorn) }')
print('ยินดีต้อนรับ' ,name, 'เกิดปี' ,yearBorn, 'อายุ' ,2023 - int(yearBorn))
print('ยินดีต้อนรับ '+name+' เกิดปี '+yearBorn+' อายุ ' + str(2023 - int(yearBorn)))
print('ยินดีต้อนรับ {} เกิดปี {} อายุ {}'.format(name,yearBorn,2023 - int(yearBorn)))
print('ยินดีต้อนรับ %s เกิดปี %s อายุ %d' %(name,yearBorn,2023 - int(yearBorn)))