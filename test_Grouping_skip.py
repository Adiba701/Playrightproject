import pytest

@pytest.mark.smoke
def test_login_smoke():
    print("Smoke test: Login")



@pytest.mark.regression
@pytest.mark.skip(reason="Feature under development")
def test_payment_regression():
    print("Regression test: Payment")
