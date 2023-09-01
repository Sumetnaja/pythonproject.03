#ให้ทำโปรแกรมป้อนจำนวนเงิน และจำนวนคนทางแป้นพิมพ์ และแสดงผลออกมาว่า
#จำนวนเงิน ???? บาท จำนวนคน ???? คน ต้องหารกันคนละ ???? บาท
#ให้แสดงผลโดยใช้ print ทั้ง 5 แบบ
money = input('ป้อนจำนวนเงิน : ')
person = input('ป้อนจำนวนคน : ')
print('----------------------------------------')
print(f'จำนวนเงิน {money} บาท จำนวนคน {person} คน ต้องหารกันคนละ {float(money)/int(person)} บาท')
print('จำนวนเงิน' ,money, 'บาท จำนวนคน' ,person, 'คน ต้องหารกันคนละ' ,float(money)/int(person), 'บาท')
print('จำนวนเงิน' +money+ 'บาท จำนวนคน' +person+' คน ต้องหารกันคนละ'+str(float(money)/int(person)))
print('จำนวนเงิน {} บาท จำนวนคน {} คน ต้องหารกันคนละ {:.2f} บาท '.format(money,person,float(money)/int(person)))
print('จำนวนเงิน %s บาท จำนวนคน %s คน ต้องหารกันคนละ %.2f บาท '%(money,person,float(money)/int(person)))