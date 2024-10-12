services = { 'Air freshener' : 1 , 'Rain repellent': 2, 'Tire shine' : 2, 'Wax' : 3, 'Vacuum' : 5 }
base_wash = 10
total = 0

service_choice1 = input()
service_choice2 = input()

print('ZyCar wash')
if service_choice1 in services.keys():
    for actions, prices in services.items():
        if service_choice1 == actions:
            total += services[service_choice1]
            print(f'{service_choice1} - {prices}')
else:
    print('-')
if service_choice2 in services.keys():
    for actions, prices in services.items():
        if service_choice2 == actions:
            total += services[service_choice2]      
            print(f'{service_choice2} - {prices}')
else:
    print('-')
print('-----')
print(f'Total price: ${total+base_wash}')
