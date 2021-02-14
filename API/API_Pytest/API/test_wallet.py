import pytest
from wallet import Wallet, InsufficientAmount


@pytest.fixture
def wallet():
	print('In fixture     ----------')
	print('In fixture     ----------')
	print('In fixture     ----------')
	return Wallet(20)


@pytest.fixture
def empty_wallet():
	print('In fixture   empty  ----------')
	return Wallet()


def test_default_initial_amount(empty_wallet):
	print('In test test_default_initial_amount     ----------')
	assert empty_wallet.balance == 0


def test_setting_initial_amount(wallet):
	assert wallet.balance == 20


def test_wallet_add_cash(wallet):
	wallet.add_cash(80)
	assert wallet.balance == 100


@pytest.mark.slow
def test_wallet_spend_cash(wallet):
	wallet.spend_cash(10)
	assert wallet.balance == 10


def test_wallet_spend_cash_raises_exception_on_insufficient_amount(empty_wallet):
	with pytest.raises(InsufficientAmount):
		empty_wallet.spend_cash(100)


@pytest.fixture
def my_wallet():
	'''Returns a Wallet instance with a zero balance'''
	return Wallet()


@pytest.mark.parametrize("earned,spent,expected", [
	(30, 10, 20),
	(20, 2, 18),
])
def test_transactions(my_wallet, earned, spent, expected):
	my_wallet.add_cash(earned)
	my_wallet.spend_cash(spent)
	assert my_wallet.balance == expected
