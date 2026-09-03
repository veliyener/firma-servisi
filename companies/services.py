from .repositories import CompanyRepository
from .messages import Messages


class DuplicateTaxNumberError(Exception):
    pass


class CompanyNotFoundError(Exception):
    pass


class CompanyService:
    def __init__(self) -> None:
        self.repository = CompanyRepository()

    def list_companies(self, page: int = 1, size: int = 20) -> dict:
        companies = self.repository.get_page(page, size)
        total = self.repository.count_all()
        return {
            'total': total,
            'page': page,
            'size': size,
            'results': companies,
        }

    def get_company(self, company_id: str):
        company = self.repository.get_by_id(company_id)
        if company is None:
            raise CompanyNotFoundError(Messages.COMPANY_NOT_FOUND)
        return company

    def create_company(self, title: str, tax_number: str):
        if self.repository.exists_by_tax_number(tax_number):
            raise DuplicateTaxNumberError(Messages.TAX_NUMBER_ALREADY_EXISTS)
        return self.repository.create(title, tax_number)

    def update_status(self, company_id: str, status: str):
        company = self.get_company(company_id)
        return self.repository.update_status(company, status)