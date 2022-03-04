import fileinput


class MortgageIO:
    def __init__(self):
        pass

    def get(self):
        lines = self.get_stdin()
        args = self.get_args(lines)
        return args

    def get_stdin(self):
        lines = []
        for line in fileinput.input():
            line = line.strip()
            if line:
                lines.append(line)
            else:
                break
        return lines

    def get_args(self, lines):
        args = {}
        for line in lines:
            # split line
            splitted = line.split(':')
            splitted = [x.strip() for x in splitted]

            # add to args dict
            key = splitted[0]
            value = splitted[1]
            args[key] = value
        return args


class MortgageCalculator:
    def __init__(self, amount=None, interest=None, downpayment=None, term=None):
        # amount
        try:
            self.amount = float(amount)
        except ValueError:
            raise Exception("Valid amount is required")

        # interest
        try:
            if isinstance(interest, str) and interest.endswith('%'):
                self.interest = float(interest[:-1]) / 100
            else:
                self.interest = float(interest)
        except ValueError:
            raise Exception("Valid interest is required")

        # down payment
        try:
            self.downpayment = float(downpayment)
        except ValueError:
            raise Exception("Valid amount is required")

        # term
        try:
            self.term = int(term)
        except ValueError:
            raise Exception("Valid term is required")

        if self.term <= 0:
            raise Exception("Valid term is required")

    def get_monthly_payment(self):
        # calculate monthly payment
        try:
            payment = (self.amount - self.downpayment) * (self.interest / 12) / (1 - (1 + (self.interest / 12)) ** (-self.term * 12))
        except ZeroDivisionError:
            payment = 0
        return payment


if __name__ == "__main__":
    # get args from stdin
    mortgage_io = MortgageIO()
    args = mortgage_io.get()

    # calculate monthly payment
    mortgage_calc = MortgageCalculator(**args)
    monthly_payment = mortgage_calc.get_monthly_payment()
    print("Monthly payment: ${:.2f}".format(monthly_payment))

