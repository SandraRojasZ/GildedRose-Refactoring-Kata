import unittest
from gilded_rose import Item, GildedRose

class GildedRoseTest(unittest.TestCase):

    def test_regular_item_before_sell_date(self):
        item = Item(name="foo", sell_in=10, quality=20)
        gilded_rose = GildedRose([item])
        gilded_rose.update_quality()
        self.assertEqual(item.sell_in, 9)
        self.assertEqual(item.quality, 19)

    def test_regular_item_on_sell_date(self):
        item = Item(name="foo", sell_in=0, quality=20)
        gilded_rose = GildedRose([item])
        gilded_rose.update_quality()
        self.assertEqual(item.sell_in, -1)
        self.assertEqual(item.quality, 18)

    def test_regular_item_after_sell_date(self):
        item = Item(name="foo", sell_in=-1, quality=20)
        gilded_rose = GildedRose([item])
        gilded_rose.update_quality()
        self.assertEqual(item.sell_in, -2)
        self.assertEqual(item.quality, 18)

    def test_quality_never_negative(self):
        item = Item(name="foo", sell_in=10, quality=0)
        gilded_rose = GildedRose([item])
        gilded_rose.update_quality()
        self.assertEqual(item.quality, 0)

    def test_aged_brie_before_sell_date(self):
        item = Item(name="Aged Brie", sell_in=10, quality=20)
        gilded_rose = GildedRose([item])
        gilded_rose.update_quality()
        self.assertEqual(item.sell_in, 9)
        self.assertEqual(item.quality, 21)

    def test_aged_brie_on_sell_date(self):
        item = Item(name="Aged Brie", sell_in=0, quality=20)
        gilded_rose = GildedRose([item])
        gilded_rose.update_quality()
        self.assertEqual(item.sell_in, -1)
        self.assertEqual(item.quality, 22)

    def test_aged_brie_after_sell_date(self):
        item = Item(name="Aged Brie", sell_in=-1, quality=20)
        gilded_rose = GildedRose([item])
        gilded_rose.update_quality()
        self.assertEqual(item.sell_in, -2)
        self.assertEqual(item.quality, 22)

    def test_quality_never_exceeds_50(self):
        item = Item(name="Aged Brie", sell_in=10, quality=50)
        gilded_rose = GildedRose([item])
        gilded_rose.update_quality()
        self.assertEqual(item.quality, 50)

    def test_sulfuras_never_decreases(self):
        item = Item(name="Sulfuras, Hand of Ragnaros", sell_in=10, quality=80)
        gilded_rose = GildedRose([item])
        gilded_rose.update_quality()
        self.assertEqual(item.sell_in, 10)
        self.assertEqual(item.quality, 80)

    def test_backstage_passes_increase_quality(self):
        item = Item(name="Backstage passes to a TAFKAL80ETC concert", sell_in=15, quality=20)
        gilded_rose = GildedRose([item])
        gilded_rose.update_quality()
        self.assertEqual(item.sell_in, 14)
        self.assertEqual(item.quality, 21)

    def test_backstage_passes_increase_quality_more(self):
        item = Item(name="Backstage passes to a TAFKAL80ETC concert", sell_in=10, quality=20)
        gilded_rose = GildedRose([item])
        gilded_rose.update_quality()
        self.assertEqual(item.sell_in, 9)
        self.assertEqual(item.quality, 22)

    def test_backstage_passes_increase_quality_even_more(self):
        item = Item(name="Backstage passes to a TAFKAL80ETC concert", sell_in=5, quality=20)
        gilded_rose = GildedRose([item])
        gilded_rose.update_quality()
        self.assertEqual(item.sell_in, 4)
        self.assertEqual(item.quality, 23)

    def test_backstage_passes_drop_to_zero_after_concert(self):
        item = Item(name="Backstage passes to a TAFKAL80ETC concert", sell_in=0, quality=20)
        gilded_rose = GildedRose([item])
        gilded_rose.update_quality()
        self.assertEqual(item.sell_in, -1)
        self.assertEqual(item.quality, 0)

    def test_conjured_items_degrade_twice_as_fast(self):
        item = Item(name="Conjured Mana Cake", sell_in=10, quality=20)
        gilded_rose = GildedRose([item])
        gilded_rose.update_quality()
        self.assertEqual(item.sell_in, 9)
        self.assertEqual(item.quality, 18)

    def test_conjured_items_degrade_twice_as_fast_after_sell_date(self):
        item = Item(name="Conjured Mana Cake", sell_in=0, quality=20)
        gilded_rose = GildedRose([item])
        gilded_rose.update_quality()
        self.assertEqual(item.sell_in, -1)
        self.assertEqual(item.quality, 16)

if __name__ == '__main__':
    unittest.main()
