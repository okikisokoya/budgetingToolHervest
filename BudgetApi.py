from flask import Flask, request, Response
from BudgetCalculator import standard_budget, custom_budget, essential_expenses


app = Flask(__name__)


@app.route('/<int:monthly_income>/<custom_budget_select>', methods=['GET'])
def calculation(monthly_income, custom_budget_select, needs=50, wants=30, savings=20):
    if request.method == 'GET':

        if monthly_income < 0:
            return Response('Income cannot be negative!', 400)
        if needs+wants+savings != 100:
            return Response('Percentages must add up to 100!', 400)

        budget = [0, 0, 0]
        if custom_budget_select:
            budget = custom_budget(monthly_income, 50, 15, 35)
        else:
            budget = standard_budget(monthly_income)

        return{
            "Essential Needs": budget[0],
            "Wants": budget[1],
            "Savings/Investments/Debt Contribution": budget[2]
        }


@app.route('/essential-spending-limit-reached', methods=['GET'])
def essential_limit():
    if request.method == 'GET':
        monthly_income = int(request.args.get('monthly_income'))
        transportation = int(request.args.get('transportation'))
        data_airtime = int(request.args.get('data_airtime'))
        groceries = int(request.args.get('groceries'))
        utilities = int(request.args.get('utilities'))
        rent_contribution = int(request.args.get('rent_contribution'))
        debt_repayment = int(request.args.get('debt_repayment'))
        custom_budget_select = bool(request.args.get('custom_budget_select'))
        needs_percentage = int(request.args.get('needs_percentage'))
        want_percentage = int(request.args.get('want_percentage'))
        savings_percentage = int(request.args.get('savings_percentage'))

        result = essential_expenses(monthly_income, transportation,
                                    data_airtime, groceries, utilities,
                                    rent_contribution, debt_repayment,
                                    custom_budget_select, needs_percentage,
                                    want_percentage, savings_percentage)

        return {
            "Total spending on essential needs": result[0],
            "Are we over budget?": result[1],
            "Remaining left of essential needs budget": result[2]
        }


if __name__ == "__main__":
    app.run(debug=True)
