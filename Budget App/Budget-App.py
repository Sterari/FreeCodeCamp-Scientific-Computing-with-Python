class Category:

    # code to instantiate objects of type category with an empty list as an instance variable
    def __init__(self, name, ledger=None):
        self.ledger = []
        self.name = name

    # creating a function which adds to an object of type category an amount and description to the ledger list
    def deposit(self, amount, description=""):
        self.amount = amount
        self.description = description
        depodic = {"amount": self.amount, "description": self.description}
        self.ledger.append(depodic)

    # function to check current balance vs an input amount
    def check_funds(self, amountc):
        self.amountc = amountc
        sumbal = 0
        for x in self.ledger:
            sumbal = sumbal + x["amount"]
        if sumbal < self.amountc:
            return False
        else:
            return True

    # adding a function to show withdrawals
    def withdraw(self, amountw, descriptionw=""):
        self.amountw = amountw
        self.descriptionw = descriptionw
        if self.check_funds(self.amountw):
            newamountw = -1 * self.amountw
            withdic = {"amount": newamountw, "description": self.descriptionw}
            self.ledger.append(withdic)
            return True
        else:
            return False

    # function to get the remaining amount after deposits and withdrawals have occured
    def get_balance(self):
        sumbal = 0
        for y in self.ledger:
            sumbal = sumbal + (y["amount"])
        return sumbal

    # function to transfer from one budget category to another
    def transfer(self, amountz, othercat):
        self.amountz = amountz
        if self.check_funds(self.amountz):
            descriptiondes = "Transfer from " + self.name
            destdic = {"amount": self.amountz, "description": descriptiondes}
            othercat.ledger.append(destdic)
            newamountz = -1 * self.amountz
            descriptionz = "Transfer to " + othercat.name
            trandic = {"amount": newamountz, "description": descriptionz}
            self.ledger.append(trandic)
            return True
        else:
            return False

    # creating string representation of instantiated class object
    def __str__(self):
        n = int((30 - len(self.name)) / 2)
        cstring = n * "*" + self.name + n * "*" + '\n'
        for x in self.ledger:
            cstring = cstring + x["description"][0:23] + (23 - len(x["description"])) * " " + (
                        7 - len(str("{:.2f}".format(x["amount"])))) * " " + str("{:.2f}".format(x["amount"])) + "\n"
        ctotal = 0
        for y in self.ledger:
            ctotal = ctotal + y["amount"]
        cstring = cstring + "Total: " + str("{:.2f}".format(ctotal))

        return cstring


def create_spend_chart(categlist=None):
    sumwithdraws = 0
    catwithdraws = []
    nlist = ["100", " 90", " 80", " 70", " 60", " 50", " 40", " 30", " 20", " 10", "  0"]

    # loop used to calculate the total withdrawals of EACH category and put them in a list
    for x in categlist:
        for y in x.ledger:
            if y["amount"] < 0:
                sumwithdraws = sumwithdraws + y["amount"]
        catwithdraws.append(sumwithdraws)
        sumwithdraws = 0

        # loop to get total withdrawals across all categories and return list of percentages
    totalwithdrawals = 0
    for z in catwithdraws:
        totalwithdrawals = totalwithdrawals + z

    # populating percentage list (category withdrawals / total withdrawals)
    percentlist = []
    for a in catwithdraws:
        b = (a / totalwithdrawals)
        b = (b * 100)
        percentlist.append(b)

    # creating string output
    outputstring = "Percentage spent by category" + "\n"
    for n in nlist:
        outputstring = outputstring + str(n) + "| "
        for per in percentlist:
            if per >= int(n):
                outputstring = outputstring + "o  "
            else:
                outputstring = outputstring + "   "
        outputstring = outputstring + "\n"
    outputstring = outputstring + 4 * " " + (3 * len(categlist) + 1) * "-" + "\n" + 5 * " "

    # whats the longers category name in categlist?
    maxcatlen = 0
    for cat in categlist:
        if int((len(cat.name))) > maxcatlen:
            maxcatlen = len(cat.name)

    for d in range(0, maxcatlen):
        for c in categlist:
            if len(c.name) > d:
                outputstring = outputstring + c.name[d] + "  "
            else:
                outputstring = outputstring + 3 * " "
        outputstring = outputstring + "\n" + 5 * " "
    return outputstring
