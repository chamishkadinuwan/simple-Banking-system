from bankapp import cash_deposite,cash_withdraw
from unittest import mock
from bankapp import *

def test_1(monkeypatch):
    a = iter([123,34])
    monkeypatch.setattr('builtins.input',lambda _:next(a))
    assert cash_deposite() == "your transaction is a success"

def test_2(monkeypatch):
    a = iter([123,34])
    monkeypatch.setattr('builtins.input',lambda _:next(a))
    assert cash_withdraw() == "your transaction is a success"



