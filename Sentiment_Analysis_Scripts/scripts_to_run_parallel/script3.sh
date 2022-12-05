#!/bin/bash

python increase_prices_home.py &
python increase_prices_housing.py &
python inflation.py &
python interest_rate_home.py &
python interest_rate_housing.py &
python low_income_housing.py &
python minimum_wage.py &
