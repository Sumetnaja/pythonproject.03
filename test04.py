#ให้ทำโปรแกรมคำนวณทาสีที่ต้องใช้ทาด้านนอกของกล่องสี่เหลี่ยมขนาดใหญ่ 1 กล่องของทุกด้าน
#ว่าต้องใช้กี่แกลอนโดยให้ผู้ใช้ป้อนความกว้าง ความยาว ความสูงของกล่อง (หน่วยเป็นเมตร)  
#ทางแป้นพิมพ์และแสดงผลจำนวนแกลอนที่ต้องใช้ทางหน้าจอ ดังนี้
#กล่องขนาดกว้าง ?? เมตร ยาว ?? เมตร สูง ?? เมตร ใช้สีจำนวน ?? แกลอน
#ให้แสดงผลโดยใช้ print ทั้ง 5 แบบ
#ทั้งนี้สี 1 แกลอนทาได้ 5 ตารางเมตร ทั้งนี้จำนวนแกลอนที่คำนวณได้หากเป็นเลขทศนิยมให้ปัดขึ้นเป็นเลขจำนวนเต็ม
#เช่น คำนวณได้ 15.239 แกลอน เวลาแสดงผลต้องแสดงเป็น 16 แกลอน เป็นต้น
import math
width = float(input('ความกว้างของกล่อง (เมตร): '))
length = float(input('ความยางของกล่อง (เมตร): '))
height = float(input('ความสูงของกล่อง (เมตร): '))
area = 2 * (width * height + length * height)
paint = math.ceil(area / 5)
print('กล่องขนาดกว้าง {:.2f} เมตร ยาว {:.2f} เมตร สูง {:.2f} เมตร'.format(width, length, height)) 
print('ใช้สีจำนวน {} แกลอน'.format(paint))
print("กล่องขนาดกว้าง" + f'{float(width):,.2f}' + " เมตร" + " ยาว " + f'{float(length):,.2f}' + " เมตร" + " สูง " + f'{float(height):,.2f}' + " เมตร")
print("ใช้สีจำนวน " + str(paint) + " แกลอน")
print(f"กล่องขนาดกว้าง {float(width):,.2f} เมตร ยาว {float(length):,.2f} เมตร สูง {float(height):,.2f} เมตร")
print(f'ใช้สีจำนวน {paint} แกลอน')
print("กล่องขนาดกว้าง",f'{float(width):,.2f}',"เมตร","ยาว",f'{float(length):,.2f}',"เมตร","สูง",f'{float(height):,.2f}',"เมตร")
print("ใช้สีจำนวน",str(paint),"แกลอน")
print('กล่องขนาดกว้าง %s เมตร ยาว %s เมตร สูง %s เมตร'%(f'{float(width):,.2f}',f'{float(length):,.2f}',f'{float(height):,.2f}'))
print('ใช้สีจำนวน %s แกลอน'%(paint))

