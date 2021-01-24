from datetime import datetime

class Car:
	base_price=100000
	def __init__(self,windows,doors,power):
		self.windows=windows
		self.doors=doors
		self.power=power

	def what_base_power(self):
		print(f'The base price is {self.base_power}')

	@classmethod
	def inflated_price(cls,inflation):
		cls.base_price=cls.base_price+cls.base_price*inflation
		return cls.base_price

	@staticmethod
	def year_check():
		if datetime.now().year==2021:
			return True
		else:
			return False

c=Car(4,4,2000)
print(c.base_price)
print(Car.inflated_price(0.10))
print(Car.year_check())
