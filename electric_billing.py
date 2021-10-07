#!/usr/bin/env python3
import csv

def read_csv():
    file_path = input("Enter the filepath of the CSV file: ")
    print()
    customerID = []
    kwhUsed = []
    with open(file_path, newline='') as csv_file:
        cust_reader = csv.reader(csv_file)
        for cust_info in cust_reader:
            customerID.append(cust_info[0])
            kwhUsed.append(int(cust_info[1]))
    
    return customerID, kwhUsed

def calculate_cost(kwhUsed):
    cost = 0
    uc_300 = 0.12
    uc_600 = 0.10
    uc_1000 = 0.09
    uc_1000_plus = 0.08

    if kwhUsed <= 300:
        cost = uc_300 * kwhUsed
    elif kwhUsed > 300 and kwhUsed <= 600:
        cost = uc_300 * 300
        cost += uc_600 * (kwhUsed - 300)
    elif kwhUsed > 600 and kwhUsed <= 1000:
        cost = uc_300 * 300 + uc_600 * 300
        cost += uc_1000 * (kwhUsed - 600)
    elif kwhUsed > 1000:
        cost = uc_300 * 300 + uc_600 * 300 + uc_1000 * 400
        cost += uc_1000_plus * (kwhUsed - 1000)

    return cost

def display_table(customerID, kwhUsed):
    print("{:<13} {:<13} {:<13}".format("Customer ID", "kWh Used", "Charge"))
    print("--------------------------------------")
    total_power_usage = 0
    total_charges = 0
    num_customers = len(customerID)

    for i in range(0,num_customers):
        cost = calculate_cost(kwhUsed[i])
        total_power_usage += kwhUsed[i]
        total_charges += cost
        print(f"{customerID[i]:<13} {kwhUsed[i]:<13} {cost:<13,.2f}")
    
    print("======================================")
    print(f'{"Total number of customers:":<27} {num_customers}')
    print(f'{"Total power usage (kWh):":<27} {total_power_usage}')
    print(f'{"Total charges:":<27} {total_charges:.2f}')

if __name__ == '__main__':
    cid, kwh = read_csv()
    display_table(cid, kwh)