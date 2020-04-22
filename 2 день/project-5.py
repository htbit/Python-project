import winsound, time, os, platform


def sound():

	for i in range(2): # Количество повторений сигнала
		
		for j in range(9): # Количество звуковых сигналов
			
			winsound.MessageBeep(-1) # Проигрываемый звук
		
		time.sleep(2) # Сколько времени между звуковыми сигналами

def alarm(n):
	
	print()
	print("Время ожидания:", n, "секунд.")
	time.sleep(n) # Ждет ' n ' секунд перед воспроизведением звука
	
	sound()

def input_destinations(user_input):

	if user_input == '1':
		
		user_input = int(input("Введите количество часов: "))
		
		wait_time = (user_input * 60) * 60
		alarm(wait_time)
	
	elif user_input == '2':
		
		user_input = int(input("Введите количество минут: "))
		
		wait_time = user_input * 60
		alarm(wait_time)

	elif user_input == '3':

		user_input = int(input("Введите количество секунд: "))

		wait_time = user_input
		alarm(wait_time)

	elif user_input == '4':

		hours = int(input("Часов: "))
		minutes = int(input("Минут: "))
		seconds = int(input("Секунд: "))

		wait_time = ((hours*60)*60) + (minutes*60) + seconds
		print(wait_time)
		alarm(wait_time)

	else:
		
		try:
			os.system('cls') # If OS is Windows
			main()
			
		except:
			os.system('clear') # If OS is Linux or Mac
			main()

def main():
	print("Какую единицу времени вы хотите выбрать?\n (1) Часы\n (2) Минуты\n (3) Секунды\n (4) Комбинация")
	main_input = input("  ")
	
	input_destinations(main_input)

	return

main()