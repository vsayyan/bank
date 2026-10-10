import pytest 

from account import Account,InsufficientFundsError

def test_new_account_has_owner_and_balance():
    account = Account("Vahe",100)
    assert account.owner == "Vahe"
    assert account.balance == 100

def test_new_account_default_balance_is_zero():
    account = Account("Vahe")
    assert account.balance == 0

def test_negative_initial_balance_raises():
    with pytest.raises(ValueError):
        Account("Vahe",-10)

def test_deposit_increases_balance():
    account = Account("Vahe",100)
    account.deposit(50)
    assert account.balance == 150

def test_deposit_non_positive_amount_raises():
    account = Account("Vahe",100)
    with pytest.raises(ValueError):
        account.deposit(-5)
    with pytest.raises(ValueError):
        account.deposit(0)

def test_withdraw_decreases_balance():
    account = Account("Vahe",100)
    account.withdraw(30)
    assert account.balance == 70

def test_withdraw_too_much_raises_and_keeps_balance():
    account = Account("Vahe",100)
    with pytest.raises(InsufficientFundsError):
        account.withdraw(500)
    assert account.balance == 100

def test_two_accounts_are_independent():
    first = Account("First",10)
    second = Account("Second",20)
    first.deposit(5)
    assert first.balance == 15
    assert second.balance == 20

def test_bank_name_is_shared():
    assert Account.bank_name == "Python Bank"
    assert Account("Vahe").bank_name == "Python Bank"

def test_str():
    assert str(Account("Vahe",100)) == "Vahe: 100"

