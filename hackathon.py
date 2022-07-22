import json

class Cars():
    FILE = 'data.json'
    id = 0

    def __init__(self, brand, model, engine_volume, color, year_of_issue, body_type, mileage, price ) -> None:
        self.brand = brand
        self.model = model
        self.engine_volume = engine_volume
        self.color = color
        self.year_of_issue = year_of_issue
        self.body_type = body_type
        self.mileage = mileage
        self.price = price
        
        self.send_cars_to_json()
    
    @classmethod
    def get_id(cls):
        cls.id += 1
        return cls.id

    @classmethod
    def get_data(cls):
        with open(cls.FILE) as file:
            return json.load(file)
 
    @staticmethod
    def get_one_car(data,id):
        car = list(filter(lambda x: x['id']==id,data))
        if not car:
            return 'Нет такой машины.'
        return car[0]

    @classmethod
    def send_data_to_json(cls,data):
            with open(cls.FILE,'w') as file:
                json.dump(data,file)

    def send_cars_to_json(self):
        data = Cars.get_data()
        car = {
            'id' : Cars.get_id(),
            'brand' : self.brand,
            'model' : self.model,
            'engine volume' : self.engine_volume,
            'color' : self.color,
            'year of issue' : self.year_of_issue,
            'body type' : self.body_type,
            'mileage' : self.mileage,
            'price' : self.price
        }
        data.append(car)

        with open(Cars.FILE,'w') as file:
                json.dump(data,file)
                return {'status':'201','msg':car}

    @classmethod
    def retrieve_data(cls,id):
        data = cls.get_data()
        car = cls.get_one_car(data,id)
        return car
    
    @classmethod
    def update_data(cls, id,**kwargs):
        data = cls.get_data()
        car = cls.get_one_car(data,id)
        index = data.index(car)
        data[index].update(**kwargs)
        cls.send_data_to_json(data)
        return {'status':'200','msg':'updated!'}

    @classmethod
    def delete_data(cls,id):
        data = cls.get_data()
        car = cls.get_one_car(data,id)

        if type(car) != dict:
            return car

        index = data.index(car)
        data.pop(index)

        cls.send_data_to_json(data)
        return {'status':'204','msg':'deleted!'}

    def liked_car(cls,id):
                data = cls.get_data()
                car = cls.get_one_car(data,id)

                if type(car) != dict:
                    return car

                index = data.index(car)
                string = input('Введите индекс понравившегося вам машины(Mercedes Benz-1;BMW-2;Lexus-3;Porsche-4;Toyota-5):')
                if string == 1:
                    return f'Вы поставли лайк на {obj1}'
                elif string == 2:
                    return f'Вы поставли лайк на {obj2}'
                elif string == 3:
                    return f'Вы поставли лайк на {obj3}'
                elif string == 4:
                    return f'Вы поставли лайк на {obj4}'
                else:
                    return f'Вы поставли лайк на {obj5}'
    

with open (Cars.FILE,'w') as file:
    json.dump([],file)

obj1 = Cars('Mercedes Benz','G-class 350II(W463)','3.0L/224ls/Diesel','black',2008,'SUV',79980,3950000)
obj2 = Cars('BMW','X5','2.0L/hybryd','black',2016,'SUV',225308,1972309)
obj3 = Cars('Lexus','ES VII 300h CVT','2.5L/hybryd','golden',2019,'sedan',12800,3936666)
obj4 = Cars('Porsche','911 VII Carrera S','3.0L/petrol','silver',2020,'Cabriolet',1700,13360805)
obj5 = Cars('Toyota','Land Cruiser 200','4.0L/petrol','white',2007,'SUV',225000,2425622)


# print('Все машины:\n',Cars.get_data())
# print('\n',Cars.retrieve_data(4))
# print(Cars.update_data(4,color='violet'))
# print(Cars.retrieve_data(4))
# print(Cars.delete_data(4))
# print('Все машины:\n',Cars.get_data())