from inventory_report.product import Product


def test_product_report():
    product = Product(
        id="123456789",
        product_name="Cadeira Aeron",
        company_name="Herman Miller",
        manufacturing_date="2021-03-26",
        expiration_date="2033-03-30",
        serial_number="AER2B23DWALPG1G1G1BBBK23103",
        storage_instructions="Lorem ipsum dolor sit amet",
    )

    excepted = (
        # "The product {self.id} - {self.product_name} "
        # "with serial number {self.serial_number} "
        # "manufactured on {self.manufacturing_date} "
        # "by the company {self.company_name} "
        # "valid until {self.expiration_date} "
        # "must be stored according to the following instructions: "
        # "{self.storage_instructions}."
        "The product 123456789 - Cadeira Aeron "
        "with serial number AER2B23DWALPG1G1G1BBBK23103 "
        "manufactured on 2021-03-26 "
        "by the company Herman Miller "
        "valid until 2033-03-30 "
        "must be stored according to the following instructions: "
        "Lorem ipsum dolor sit amet."
    )

    assert str(product) == excepted
