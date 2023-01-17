from araçkiralamaprojesi import BikeRent, CarRent, Customer

bike = BikeRent(100)
car = CarRent(10)
customer = Customer()

main_menu = True

while True:
    
    if main_menu:
        print("""
              ***** Araç Kiralama Mağazası*****
              A. Bisiklet Menüsü
              B. Araç Menüsü
              Q. Çıkış
              """)
        main_menu = False
        
        choice = input("Seçimi girin: ")
        
    if choice == "A" or choice == "a":
        
        print("""
              ****** BİSİKLET MENÜSÜ*****
              1. Mevcut bisikletleri görüntüleyin
              2. Saatlik 5 Dolar üzerinden bisiklet talep edin
              3. Günlük olarak bisiklet talep edin 84 $
              4. Bisikleti iade edin
              5. Ana Menü
              6. Çıkış
              """)
        choice = input("Seçimi girin: ")
        
        try:
            choice = int(choice)
        except ValueError:
            print("tamsayı değil")
            continue
        
        if choice == 1:
            bike.displayStock()
            choice = "A"
        elif choice == 2:
            customer.rentalTime_b = bike.rentHourly(customer.requestVehicle("bike"))
            customer.rentalBasis_b = 1
            main_menu = True
            print("----------------")
        elif choice == 3:
            customer.rentalTime_b = bike.rentDaily(customer.requestVehicle("bike"))
            customer.rentalBasis_b = 2
            main_menu = True
            print("----------------")
        elif choice == 4:
            customer.bill = bike.returnVehicle(customer.returnVehicle("bike"),"bike")
            customer.rentalBasis_b, customer.rentalTime_b, customer.bikes = 0,0,0
            main_menu = True
        elif choice == 5:
            main_menu = True
        elif choice ==6:
            break
        else:
            print("Geçersiz Giriş. Lütfen 1-6 arasında bir sayı giriniz ")
            main_menu = True
        
    elif choice == "B" or choice == "b":
        
        print("""
              ****** ARAÇ MENÜSÜ ******
              1. Mevcut arabaları görüntüleyin
              2. Saatlik 10$ araba talep edin
              3. Günlük olarak bir araba talep edin 192 $
              4. Bir arabayı iade edin
              5. Ana Menü
              6. Çıkış
              """)
        choice = input("Seçimi girin: ")
        
        try:
            choice = int(choice)
        except ValueError:
            print("tamsayı değil")
            continue
        
        if choice == 1:
            car.displayStock()
            choice = "B"
        elif choice == 2:
            customer.rentalTime_c = car.rentHourly(customer.requestVehicle("car"))
            customer.rentalBasis_c = 1
            main_menu = True
            print("----------------")
        elif choice == 3:
            customer.rentalTime_c = car.rentDaily(customer.requestVehicle("car"))
            customer.rentalBasis_c = 2
            main_menu = True
            print("----------------")
        elif choice == 4:
            customer.bill = car.returnVehicle(customer.returnVehicle("car"),"car")
            customer.rentalBasis_c, customer.rentalTime_c, customer.cars = 0,0,0
            main_menu = True
        elif choice == 5:
            main_menu = True
        elif choice ==6:
            break
        else:
            print("Geçersiz Giriş. Lütfen 1-6 arasında bir sayı giriniz ")
            main_menu = True
        
    elif choice == "Q" or choice == "q":  
        break
    
    else:
        print("Geçersiz Giriş. Lütfen A-B-Q Girin")
        main_menu = True
    print("Araç kiralama mağazasını kullandığınız için teşekkür ederiz.")
        
              
              





















