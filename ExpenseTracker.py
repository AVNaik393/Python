import csv
with open ("expenses.csv", mode = "a", newline = "") as file:
    write = csv.writer(file)
    if file.tell() == 0: # if file is empty
        write.writerow(["Amount", "Catergory", "Description"])

class Expense:

    def __init__(self, a, cat, d):
        self.amount = a
        self.category =  cat
        self.desc = d

class ExpenseTracker:

    def __init__(self):
        self.expenses = []

    def AddExpense(self):
        a = int(input("Enter amount: "))
        cat = input("Enter Catgory: ")
        desc = input("Enter Description: ")
        exp = Expense(a, cat, desc)
        self.expenses.append(exp)
        expset = [exp.amount, exp.category, exp.desc]
        self.addtoCSV(expset)

    def addtoCSV(self, exp):
        with open("expenses.csv", "a", newline = "") as file: #openening in append mode, as in w mode, data gets overriden
            write = csv.writer(file)
            write.writerow(exp)
            print("Added Successfully!")

    def ViewAll(self):
        with open("expenses.csv", "r") as file: 
            content = csv.reader(file)
            for row in content:
                print(f"{row[0]} | {row[1]} | {row[2]}")
            print("All Shown!")

    def TotSpend(self):
        with open("expenses.csv", "r") as file:
            sum = 0
            content = csv.reader(file)
            for row in content:
                if row[0] != "Amount":
                    sum += int(row[0]);
            print(f"The Total Spendings till now are: {sum} Rs")

def main():
    e = ExpenseTracker()
    print("-------Expense Tracker-------")
    print("1. Add New Expense")
    print("2. View All Expenses")
    print("3. Show Total Spending")

    n = int(input("Choose an Option: "))

    if n == 1:
        e.AddExpense()
    elif n == 2:
        e.ViewAll()
    elif n ==3:
        e.TotSpend()
    else:
        print("Please Enter a Valid Input!")

if __name__ == '__main__':
    main()
