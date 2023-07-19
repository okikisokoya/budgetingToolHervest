
def standard_budget(monthly_income):
    needs = 0.5 * monthly_income
    wants = 0.3 * monthly_income
    savings = 0.2 * monthly_income

    return [needs, wants, savings]


def custom_budget(monthly_income, needs_percent, want_percentage, savings_percentage):
    needs = (needs_percent/100) * monthly_income
    wants = (want_percentage/100) * monthly_income
    savings = (savings_percentage/100) * monthly_income

    return [needs, wants, savings]


def essential_expenses(monthly_income, transportation, data_airtime,
                       groceries, utilities, rent_contribution, debt_repayment=0,
                       custom_budget_select=False, needs_percent=50, want_percentage=30, savings_percentage=20):

    if custom_budget_select:
        needs = custom_budget(monthly_income, needs_percent, want_percentage, savings_percentage)[0]
    else:
        needs = standard_budget(monthly_income)[0]

    total = transportation + data_airtime + groceries + utilities + rent_contribution + debt_repayment

    over = False

    if needs - total < 0:
        over = True

    return [total, over, needs-total]
