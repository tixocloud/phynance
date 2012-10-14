#!/user/bin/env python

# Time Value of Money calculations
def future_value_factor(interest_rate, time_period):
    return (1 + interest_rate)**time_period


def present_value_factor(interest_rate, time_period):
    return 1 / future_value_factor(interest_rate, time_period)

def future_value(present_value, interest_rate, time_period):
    return present_value * future_value_factor(interest_rate, time_period)


def present_value(future_value, interest_rate, time_period):
    return future_value / future_value_factor(interest_rate, time_period)


def annuity_present_value(payment, interest_rate, time_period):
    return payment * (1 - present_value_factor) / interest_rate

def discount_rate:
    pass

def num_periods:
    pass

