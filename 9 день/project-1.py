class Product:
    def __init__(self,pId,name,price,quantity):
        # Инициализирует атрибуты
        self.id = pId
        self.name = name
        self.price = price
        self.quantity = quantity

    def updatePrice(self,new_price):
        # Обновляет цену продукта
        if new_price > 0:
            self.price = new_price
        else:
            print ("Error! Cannot update price to lower than or equal to zero.")

    def updateQuantity(self,new_quantity,isIncrement):
        # Позволяет обновить количество продукта путем увеличения или уменьшения количества в зависимости от значения переменной isIncrement.
        if isIncrement is True:
            self.quantity += new_quantity
        elif (self.quantity - new_quantity) >= 0:
            self.quantity -= new_quantity
        else:
            print ("Ошибка, не может уменьшить дальше!")

    def getQuantity(self):
        # Возвращает текущее количество продукта.
        return self.quantity

    def viewProduct(self):
        # Отображение информации о продукте с помощью печати
        print ("Продукт ID: " + str(self.id) + ", Название: " + self.name + ", Цена: " + str(self.price) + ", Количество: " + str(self.quantity))


class Inventory:
    def __init__(self):
        # Инициализирует атрибут
        self.listProd = []

    def addProduct(self,pId):
        # Добавить новый продукт в список
        self.listProd.append(pId)

    def removeProduct(self,pId):
        # удаляет продукт из списка
        if pId in self.listProd:
            self.listProd.remove(pId)
        else:
            print ("Ошибка. Товар отсутствует в инвентаре.")
    
    def viewInventory(self):
        # Отображение списка запасов через печать
        print (self.listProd)

if __name__ == '__main__':       
    prod1 = Product(1,"colgate",2.20,5)
    print (prod1.getQuantity())
    prod1.updateQuantity(2,True)
    prod1.viewProduct()

    invent1 = Inventory()
    invent1.addProduct(1)
    invent1.removeProduct(2)
    invent1.viewInventory()