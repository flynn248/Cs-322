#!/usr/bin/env python3
import csv

def read_csv():
    file_path = input("Enter the filepath of the CSV file: ")
    customerID = []
    kwhUsed = []
    with open(file_path, newline='') as csv_file:
        cust_reader = csv.reader(csv_file)
        for cust_info in cust_reader:
            customerID, kwhUsed = cust_info
    
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
    print("Customer ID\tkWh Used\tCharge\n\
        -------------------------------")
    total_power_usage = 0
    total_charges = 0

    for i in range(0,len(customerID)):
        cost = calculate_cost(kwhUsed[i])
        total_power_usage += kwhUsed[i]
        total_charges += cost
        print(f"{customerID[i]}\t{kwhUsed[i]}\t{cost}")


if __name__ == '__main__':
    read_csv()