from .repositories import CompanyRepository


class CompanyService:
    def __init__(self):
        self.repository = CompanyRepository()

    def list_companies(self):
        return self.repository.get_all()

    def create_company(self, title, tax_number):
        return self.repository.create(title, tax_number)