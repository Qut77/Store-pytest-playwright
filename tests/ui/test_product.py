def test_hover_cards_hidden(product_page):
    product_page.open()
    product_page.expect_overlay_hidden()

def test_hover_cards(product_page):
    product_page.open()
    product_page.hover_product()
    product_page.expect_overlay_visible()