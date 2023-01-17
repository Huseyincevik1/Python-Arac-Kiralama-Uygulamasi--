import datetime

# parent class
class VehicleRent:
    
    def __init__(self,stock):
        self.stock = stock
        self.now = 0
    
    def displayStock(self):
       
        print("{} Araç Kiralanabilir.".format(self.stock))
        return self.stock
    
    def rentHourly(self, n):
        
        if n <= 0:
            print("Sayı pozitif olmalıdır.")
            return None
        elif n > self.stock:
            print("Üzgünüz sadece {} araç kiralanabilir.".format(self.stock))
            return None
        else:
            self.now = datetime.datetime.now()
            print(" {} araç {} saatlik kiralandı.".format(n,self.now.hour))
            
            self.stock -= n 
            
            return self.now
            
    def rentDaily(self, n):
        
        if n <= 0:
            print("Sayı pozitif olmalıdır.")
            return None
        elif n > self.stock:
            print("Üzgünüz sadece {} araç kiralanabilir.".format(self.stock))
            return None
        else:
            self.now = datetime.datetime.now()
            print(" {} araç günlük {} saatliğine kiralandı.".format(n,self.now.hour))
            
            self.stock -= n 
            
            return self.now
    
    def returnVehicle(self, request, brand):
       
        car_h_price = 10
        car_d_price = car_h_price*8/10*24
        bike_h_price = 5
        bike_d_price = bike_h_price*7/10*24
        
        rentalTime, rentalBasis, numOfVehicle = request
        bill = 0
        
        if brand == "car":
            if rentalTime and rentalBasis and numOfVehicle:
                self.stock += numOfVehicle
                now = datetime.datetime.now()
                rentalPeriod = now - rentalTime 
                
                if rentalBasis == 1: # hourly
                    bill = rentalPeriod.seconds/3600*car_h_price*numOfVehicle
                
                elif rentalBasis == 2: # daily
                    bill = rentalPeriod.seconds/(3600*24)*car_d_price*numOfVehicle
                    
                if (2 <= numOfVehicle):
                    print("Ekstra %20 indiriminiz var")
                    bill = bill*0.8
                
                print("Arabanı geri verdiğin için teşekkürler")
                print("Fiyat: $ {}".format(bill))
                return bill
        elif brand == "bike":
            if rentalTime and rentalBasis and numOfVehicle:
                self.stock += numOfVehicle
                now = datetime.datetime.now()
                rentalPeriod = now - rentalTime 
                
                if rentalBasis == 1: 
                    bill = rentalPeriod.seconds/3600*bike_h_price*numOfVehicle
                
                elif rentalBasis == 2: 
                    bill = rentalPeriod.seconds/(3600*24)*bike_d_price*numOfVehicle
                    
                if (4 <= numOfVehicle):
                    print("You have extra 20% discount")
                    bill = bill*0.8
                
                print("Arabanı geri verdiğin için teşekkürler")
                print("Fiyat: $ {}".format(bill))
                return bill
        else:
            print("Araç Kiralayamazsınız")
            return None
    
# child sınıf 1
class CarRent(VehicleRent):
    
    global discount_rate
    discount_rate = 15
    
    def __init__(self, stock):
        super().__init__(stock)
    
    def discount(self, b):
        
        bill = b - (b*discount_rate)/100
        return bill
    
# child sınıf 2
class BikeRent(VehicleRent):
    
    def __init__(self, stock):
        super().__init__(stock)

# musteri 
class Customer:
    
    def __init__(self):
        self.bikes = 0
        self.rentalBasis_b = 0
        self.rentalTime_b = 0
        
        self.cars = 0
        self.rentalBasis_c = 0
        self.rentalTime_c = 0
    
    def requestVehicle(self, brand):
       
        if brand == "bike":
            bikes = input("Kaç tane bisiklet kiralamak istersiniz?")
            
            try:
                bikes = int(bikes)
            except ValueError:
                print("Sayı Giriniz")
                return -1
            
            if bikes < 1:
                print("Bisiklet sayısı sıfırdan büyük olmalıdır")
                return -1
            else:
                self.bikes = bikes
            return self.bikes
            
        elif brand == "car":
            cars = input("Kaç araba kiralamak istersiniz?")
            
            try:
                cars = int(cars)
            except ValueError:
                print("Sayı Giriniz")
                return -1
            
            if cars < 1:
                print("Araba sayısı sıfırdan büyük olmalıdır")
                return -1
            else:
                self.cars = cars
            return self.cars
            
        else:
            print("Araç hatası")
        
    def returnVehicle(self, brand):
       
        if brand == "bike":
            if self.rentalTime_b and self.rentalBasis_b and self.bikes:
                return self.rentalTime_b, self.rentalBasis_b,  self.bikes
            else:
                return 0,0,0
        elif brand == "car": 
            if self.rentalTime_c and self.rentalBasis_c and self.cars:
                return self.rentalTime_c, self.rentalBasis_c,  self.cars
            else:
                return 0,0,0
        else:
            print("Return vehicle Error")
























