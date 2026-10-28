from app.schemas import WorkItemExtracted

def test_work_item():
    item = WorkItemExtracted(
        document_id=1,
        code="E11",
        name="Бетон",
        unit="м2",
        quantity="100",
        unit_price="3500",
        source_ref="Sheet1!A12"
    )

    assert item.document_id == 1

    