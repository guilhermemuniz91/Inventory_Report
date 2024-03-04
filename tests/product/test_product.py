from inventory_report.product import Product


def test_create_product():
    product = Product(
        id="123456789",
        product_name="Cadeira Aeron",
        company_name="Herman Miller",
        manufacturing_date="2021-03-26",
        expiration_date="2033-03-30",
        serial_number="AER2B23DWALPG1G1G1BBBK23103",
        storage_instructions="Lorem ipsum dolor sit amet",
    )

    assert product.id == "123456789"
    assert product.product_name == "Cadeira Aeron"
    assert product.company_name == "Herman Miller"
    assert product.manufacturing_date == "2021-03-26"
    assert product.expiration_date == "2033-03-30"
    assert product.serial_number == "AER2B23DWALPG1G1G1BBBK23103"
    assert product.storage_instructions == "Lorem ipsum dolor sit amet"
