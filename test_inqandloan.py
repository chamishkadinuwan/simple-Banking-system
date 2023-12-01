from bankapp import  loan_cal,account_incuiry
from unittest import mock
from bankapp import *

def test_loan(monkeypatch):
     a = iter([500000,1])
     monkeypatch.setattr('builtins.input',lambda _:next(a))
     assert  loan_cal() == 20138.888888889

def test_check(monkeypatch):
     a = iter(["123"])
     monkeypatch.setattr('builtins.input',lambda _:next(a))
     assert  account_incuiry() == "492"

