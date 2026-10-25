from alex_runtime.menu_provenance import summarize_menu


def test_aggregate_menu_does_not_universalize_representative_possibility():
    receipt = summarize_menu(
        {
            "left": {"green"},
            "right": {"hold"},
        }
    )

    assert receipt["may"] == ["green", "hold"]
    assert receipt["must"] == []
    assert receipt["contributors"] == {
        "green": ["left"],
        "hold": ["right"],
    }
    assert receipt["representatives"] == {
        "left": ["green"],
        "right": ["hold"],
    }
    assert receipt["authority"] == "none"


def test_shared_possibility_is_must_only_when_every_representative_has_it():
    receipt = summarize_menu(
        {
            "left": {"advance", "green"},
            "right": {"advance", "hold"},
        }
    )

    assert receipt["may"] == ["advance", "green", "hold"]
    assert receipt["must"] == ["advance"]
    assert receipt["contributors"]["advance"] == ["left", "right"]


def test_empty_local_menu_is_preserved_as_a_representative_fact():
    receipt = summarize_menu(
        {
            "blocked": set(),
            "ready": {"advance"},
        }
    )

    assert receipt["may"] == ["advance"]
    assert receipt["must"] == []
    assert receipt["contributors"] == {"advance": ["ready"]}
    assert receipt["representatives"] == {
        "blocked": [],
        "ready": ["advance"],
    }


def test_empty_representative_family_is_refused():
    try:
        summarize_menu({})
    except ValueError as exc:
        assert str(exc) == "representative family must be non-empty"
    else:
        raise AssertionError("expected ValueError")
