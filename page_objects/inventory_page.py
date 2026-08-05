class InventoryPage:
    def __init__(self, page):
        self.page = page

        #Locators
        self.title_label = page.locator(".title")
        self.inventory_items = page.locator(".inventory_item")

    def is_loaded(self) -> bool:
        """Checks if the inventory page has loaded successfully."""
        self.title_label.wait_for(state="visible")
        return self.title_label.inner_text() == "Products"

    def get_item_count(self) -> int:
        """Returns the number of products displayed on the page."""
        return self.inventory_items.count()