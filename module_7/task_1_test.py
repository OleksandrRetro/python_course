import pytest

from module_5.business import Company


@pytest.fixture()
def create_company():
    return Company('Fruits', address='Ocean street, 1')


@pytest.mark.smoke
def test_some_data(create_company):
    assert create_company.name == 'Fruits'


@pytest.mark.data_provider
@pytest.mark.parametrize("company, exp_name",
                         [(Company('Epam', address='Ocean street, 1'), 'Epam'),
                          (Company('N-iX', address='Ocean street, 11'), 'N-iX'),
                          (Company('SoftServe', address='Ocean street, 131'), 'SoftServe')]
                         )
def test_passing_provider(company, exp_name):
    assert company.name == exp_name



