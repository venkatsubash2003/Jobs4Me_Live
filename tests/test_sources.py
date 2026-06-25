from jobs4me.sources import _load_boards, _normalize_company_board


def test_normalize_imported_company_board_schema():
    assert _normalize_company_board(
        {"company": "OpenAI", "ats": "greenhouse", "slug": "openai"}
    ) == ("greenhouse", {"company": "OpenAI", "token": "openai"})

    assert _normalize_company_board(
        {"company": "NVIDIA", "ats": "workday", "slug": "nvidia|wd5|NVIDIAExternalCareerSite"}
    ) == (
        "workday",
        {
            "company": "NVIDIA",
            "host": "nvidia.wd5.myworkdayjobs.com",
            "tenant": "nvidia",
            "site": "NVIDIAExternalCareerSite",
        },
    )


def test_load_boards_includes_imported_inventory():
    boards = _load_boards()
    assert sum(len(configs) for configs in boards.values()) > 2000
    assert any(config.get("token") == "coinbase" for config in boards["greenhouse"])
    assert any(config.get("organization") == "openai" for config in boards["ashby"])
    assert any(config.get("organization") == "cursor" for config in boards["ashby"])
