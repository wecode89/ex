# Mortage Calculator

python src/calc.py > tests/data/valid_input.txt

The Problem
You are in charge of creating a loan payment calculator. A lot of people want to figure out what their payments are going to look like and how much of it is going to go towards principle vs interest. To do that calculation you will need to take in the interest rate, loan amount, downpayment and the term length. Your program is going to get data from standard input in the following format:

amount: 100000
interest: 5.5%
downpayment: 20000
term: 30

NOTE:
The last line of input is a blank line.
The term is given in years.
The interest can be given a percentage or a digit.
Your program needs to process the input including handling some human errors (upper/lower case, spacing etc) and output a JSON of the monthly payment and total interest paid.

{
"monthly payment":
"total interest":
"total payment":
}# ex
