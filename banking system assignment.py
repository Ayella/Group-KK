class Bank(object):
    def __init__(self, bankId, name, location):
        self.bankId = bankId
        self.name = name
        self.location = location

    def add_teller(self, teller):
        teller.id = self.get_unique_id("teller")
        teller.bank = self
        self.__tellers.update({teller.id: teller})

    def add_customer_(self, customer, teller):
        customer.id = self.get_unique_id("customer")
        if self.teller_is_valid(teller):
            customer_id = self.get_unique_id("customer")
            self._customers.update({customer_id: customer})
            return customer_id
        else:
            return ("invalid name")

    def __add__account(self, account, customer, teller):
        if self.teller_is_valid(teller):
            self.__accounts.update({account.id: account})
        else:
            return ("invalid account")

    def _add_loan(self, loan, teller):
        if self.teller_is_valid(teller):
            self.__loans.update({loan.id: loan})
        else:
            return ("invalid user")

    def teller_is_valid(self, teller):
        if teller.id in self.__tellers:
            return True
        return False

    def get_max_id(self, data):
        return max([int(y[len(self.name.lower().replace(" ", '') + "teller"):]) for y in list(data.keys())])

    def get_unique_id(self, qualifier):
        x = 0
        if qualifier.lower() in ["teller", "customer", "loan", "account"]:
            if qualifier.lower() == "teller":
                if not list(self.__tellers.keys()):
                    return self.name.lower().replace(" ", '') + qualifier.lower() + "1"
                x = self.get_max_id(self.__tellers)

            elif qualifier.lower() == "customer":
                if not list(self._customers.keys()):
                    return self.name.lower().replace(" ", '') + qualifier.lower() + "1"
                x = self.get_max_id(self._customers)

            elif qualifier.lower() == "loan":
                if not list(self.__loans.keys()):
                    return self.name.lower().replace(" ", '') + qualifier.lower() + "1"
                x = self.get_max_id(self.__loans)

            elif qualifier.lower() == "account":
                if not list(self.__accounts.keys()):
                    return self.name.lower().replace(" ", '') + qualifier.lower() + "1"
                x = self.get_max_id(self.__accounts)

            return self.name.lower().replace(" ", '') + qualifier.lower() + str(x)
        else:
            raise Exception("Invalid Qualifier")

    def get_customer(self, id):
        if id in self._customers:
            return self._customers[id]

    def get_account(self, id):
        if self.is_valid_account(id):
            return self.__accounts[id]

    def get_loan(self, id):
        if id in self.__loans:
            return self.__loans[id]

    def update_account(self, account_id, amount):
        if self.is_valid_account(account_id):
            new_amount = self.__accounts[account_id].get_account_balance() + amount
            self.__accounts[account_id].set_account_balance(new_amount)

    def is_valid_account(self, account_id):
        if not account_id:
            raise Exception("Invalid Account")
        if not account_id in self.__accounts:
            raise Exception("Invalid Account")
        return True

    def delete_account(self, account_id):
        if self.is_valid_account(account_id):
            del self.__accounts[account_id]

class customer():
    def __init__(self, id, name, address, PhoneNo, AcctNo):
        self.id = id
        self.name = name
        self.address = address
        self.PhoneNo = PhoneNo
        self.AcctNo = Account

    def general_inquiry(self, teller):
        return

    def deposit_money(self, teller, account_id, amount):
        teller.collect_money(account_id, amount, "deposit")
        if self.AcctNo["account_id"]:
            return ("enter customer name")
        if self.name["name"]:
            return ("money deposited")
        else:
            return ("wrong account number")

    def withdraw_money(self, teller, account_id, amount):
        return

    def open_account(self, teller, account_type, initial_amount):
        data = teller.open_account(self, account_type, initial_amount)
        self.__account_id = data["account_id"]
        if data["customer_id"]:
            self.__id = data["customer_id"]

    def close_account(self, teller, account_id):
        teller.close_account(self.account_id)
        self.__account_id = account_id

    def apply_for_loan(self, teller, loan_type, amount):
        return

    def request_card(self):
        return

class Account():
    def __init__(self, id, customer_id, amount):
        self.id = id
        self.customer_id = customer_id
        self.__account_balance = amount

    def set_account_balance(self, amount):
        self.__account_balance = amount

    def get_account_balance(self):
        return self.__account_balance

class CheckingAccount(Account):
    def __init__(self, id, customer_id, amount):
        super().__init__(id, customer_id, amount)
        return self.amount

class SavingsAccount(Account):
    def __init__(self, id, customer_id, amount):
        super().__init__(id, customer_id, amount)
        return self.amount

class Teller():
    def __init__(self, name, bank):
        self.id = None
        self.name = name
        self.bank = bank
        if self.bank:
            self.bank.add_teller(self)

    def collect_money(self, account_id, amount, qualifier):
        if qualifier == "deposit":
            self.bank.update_account(account_id, amount)

    def open_account(self, customer, account_type, amount):
        if account_type in ["savings", "checking"]:
            customer_id = customer_name
            if not customer.get_account_id():
                customer_id = self.bank.add_customer(customer, self)

            elif not self.bank.get_customer(customer.get_account_id()):
                raise Exception("Customer already with bank")

            account_id = self.bank.get_unique_id("account")
            if account_type == "savings":
                account = SavingsAccount(account_id, customer.get_account_id(), amount)
                self.bank.add_account(account, self)

            else:
                account = CheckingAccount(account_id, customer.get_account_id(), amount)
                self.bank.add_account(account, self)

            return {"account_id" : account_id, "customer_id":customer_id}


        else:
            raise Exception("Invalid Account type")

    def close_account(self, account_id):
        self.bank.delete_account(account_id)

    def loan_request(self, customer_id, loan_type, amount):
        return

    def provide_info(self, customer_id):
        return

    def issue_card(self):
        if self.is_valid_account("customer_id"):
            return "issue Card"
        return "issue card"

class Loan(Bank, Account):
    def __init__obtain_loan(self, id, loan_type, account_id, customer_id):
        self.id = id
        self.loan_type = loan_type
        self.account_id = account_id
        self.customer_id = customer_id

    def is_valid_account(self, account_id):
        if not account_id:
            raise Exception("not eligible for loan")

    def