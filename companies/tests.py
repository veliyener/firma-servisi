import pytest
from .services import CompanyService, DuplicateTaxNumberError, CompanyNotFoundError


@pytest.mark.django_db
def test_ayni_vergi_numarasiyla_ikinci_firma_olusturulamaz():
    service = CompanyService()
    service.create_company(title="Ilk Firma", tax_number="11111111111")

    with pytest.raises(DuplicateTaxNumberError):
        service.create_company(title="Ikinci Firma", tax_number="11111111111")


@pytest.mark.django_db
def test_olmayan_id_ile_firma_istendiginde_hata_firlar():
    service = CompanyService()

    with pytest.raises(CompanyNotFoundError):
        service.get_company("00000000-0000-0000-0000-000000000000")


@pytest.mark.django_db
def test_gecerli_bilgilerle_firma_olusturulunca_kayit_gercekten_olusur():
    service = CompanyService()
    company = service.create_company(title="Test Firma AS", tax_number="22222222222")

    assert company.title == "Test Firma AS"
    assert company.tax_number == "22222222222"
    assert company.status == "active"