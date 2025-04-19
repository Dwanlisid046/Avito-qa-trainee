import pytest

if __name__ == "__main__":
    pytest.main(["-v", "test_get_statistic_v2.py"])
    pytest.main(["-v", "test_delete.py"])
    pytest.main(["-v", "test_get_item.py"])
    pytest.main(["-v", "test_get_items_by_sellerID.py"])
    pytest.main(["-v", "test_get_statistic.py"])
    pytest.main(["-v", "test_post.py"])
