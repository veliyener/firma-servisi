from .repositories import CompanyRepository
from .messages import Messages


class DuplicateTaxNumberError(Exception):
    pass


class CompanyNotFoundError(Exception):
    pass


class CompanyService:
    def __init__(self):
        self.repository = CompanyRepository()

    def list_companies(self):
        return self.repository.get_all()

    def get_company(self, company_id):
        company = self.repository.get_by_id(company_id)
        if company is None:
            raise CompanyNotFoundError(Messages.COMPANY_NOT_FOUND)
        return company

    def create_company(self, title: str, tax_number: str):
        if self.repository.exists_by_tax_number(tax_number):
            raise DuplicateTaxNumberError(Messages.TAX_NUMBER_ALREADY_EXISTS)
        return self.repository.create(title, tax_number)