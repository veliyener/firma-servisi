from .repositories import CompanyRepository
from .messages import Messages


class DuplicateTaxNumberError(Exception):
    pass


class CompanyService:
    def __init__(self):
        self.repository = CompanyRepository()

    def list_companies(self):
        return self.repository.get_all()

    def create_company(self, title: str, tax_number: str):
        if self.repository.exists_by_tax_number(tax_number):
            raise DuplicateTaxNumberError(Messages.TAX_NUMBER_ALREADY_EXISTS)
        return self.repository.create(title, tax_number)