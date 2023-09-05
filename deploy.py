
import pickle
import pandas as pd
print("Welcome! Pleas enter customer details to predict churn")
def calculate_churn_(gender, age, subl, usage, location_h, loaction_l, loaction_m, location_n, bill):
    model = pickle.load(open('model.pkl', 'rb'))
    mean = [-2.92892572e-18 , 1.43517360e-17 , 3.69044641e-17, -2.46029761e-17, 1.37659509e-17 , 2.92892572e-19,  1.02512400e-17]
    def trans(fea, index):
        fea = fea - mean[index]
        fea = fea/1
        return fea
    


    total_money = subl*bill
    total_money = trans(total_money, 4)
    usage_per_month = usage/subl
    usage_per_month = trans(usage_per_month, 5)
    bill_per_usage = bill/usage
    bill_per_usage = trans(bill_per_usage, 6)
    age = trans(age, 0)
    subl = trans(subl, 1)
    usage = trans(usage,  3)
    bill = trans(bill, 2)

    prediction_input = pd.DataFrame({
    "Age": [age],
    "Subscription_Length_Months": [subl],
    "Monthly_Bill": [bill],
    "Total_Usage_GB": [usage],
    "total_money": [subl],
    "usage_per_month": [usage/subl],
    "bill_per_usage": [bill/usage],
    "Gender_Male":[gender],
    "Location_Houston": [location_h], 
    "Location_Los Angeles":[loaction_l], 
    "Location_Miami":[loaction_m],
    "Location_New York": [location_n],
})
    print(prediction_input)
    churn_probability = model.predict(prediction_input) 
    return churn_probability
location_h = 1
location_l = 0
location_m = 0
location_n = 0
# User interface
while True:
    gender = input("Enter your gender (M/F): ").strip().lower()
    
    if gender not in ['m', 'f']:
        print("Invalid input. Please enter 'M' for Male or 'F' for Female.")
        continue
    else:
        male = 1 if gender == 'm' else 0


    while True:
        age_str = input("Enter your age: ").strip()
        if not age_str.isdigit():
            print("Invalid input. Please enter a valid age as a number.")
            continue
        else:
            age = int(age_str)
            break
    while True:
        usage_str = input("Enter your usage (in GB): ").strip()
        if not usage_str.isdigit():
            print("Invalid input. Please enter valid usage as a number.")
            continue
        else:
            usage = int(usage_str)
            break
    while True:
        subl = input("Enter your subscribtion months: ").strip()
        if not subl.isdigit():
            print("Invalid input. Please enter valid usage as a number.")
            continue
        else:
            subl = int(usage_str)
            break

    while True:
        location_h = 0
        location_l = 0
        location_m = 0
        location_n = 0
        location = input("Enter your location: \n H for Houstan, \n N for New York, \n C for Chicago \n M for Miami, \n L for Los Angelos").strip().upper()
        if location not in ['H', 'C', 'L', "N", 'M']:
                print("Invalid input. Please enter a valid location.")
                continue
        else:  
            if location == 'H':
                location_h = 1
                location_l = 0
                location_m = 0
                location_n = 0
            elif location == 'C':
                location_h = 0
                location_l = 0
                location_m = 0
                location_n = 0
            elif location == 'L':
                location_h = 0
                location_l = 1
                location_m = 0
                location_n = 0
            elif location == 'M':
                location_h = 0
                location_l = 0
                location_m = 1
                location_n = 0
            elif location == 'N':
                location_h = 0
                location_l = 0
                location_m = 0
                location_n = 1
            
            break

    
    while True:
        bill_str = input("Enter your bill amount: ").strip()
        if not bill_str.replace('.', '', 1).isdigit():
            print("Invalid input. Please enter a valid bill amount as a number.")
            continue
        else:
            bill = float(bill_str)
            break
        
    
    # Calculate churn probability
    churn_ = calculate_churn_(male, age, subl, usage,location_h,location_l,location_m,location_n, bill)
    
    print(f"Churn : {churn_[0]:.2f}")
    
    another_input = input("Do you want to calculate again? (y/n): ").strip().lower()
    if another_input != 'y':
        break



