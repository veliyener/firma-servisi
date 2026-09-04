class ErrorCodes:
    DUPLICATE_TAX_NUMBER = "DUPLICATE_TAX_NUMBER"
    COMPANY_NOT_FOUND = "COMPANY_NOT_FOUND"
    INVALID_STATUS = "INVALID_STATUS"
    VALIDATION_ERROR = "VALIDATION_ERROR"


class Messages:
    TAX_NUMBER_ALREADY_EXISTS = "Bu vergi numarasıyla kayıtlı bir firma zaten var."
    COMPANY_NOT_FOUND = "Böyle bir firma bulunamadı."
    INVALID_STATUS = "Durum yalnızca 'active' veya 'passive' olabilir."
    SIZE_TOO_LARGE = "size en fazla 100 olabilir."