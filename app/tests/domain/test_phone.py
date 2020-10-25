from src.domain.phone import Phone


def test_initialze():
    assert Phone("sample").get_name() == "sample", "名前を初期化する"
