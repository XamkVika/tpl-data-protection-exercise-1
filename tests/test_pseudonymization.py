from dataprotection.pseudonymization import pseudonymize_names, restore_names

def test_roundtrip():
    names = ["Alice Example", "Bob Test"]
    encrypted = pseudonymize_names(names)
    restored = restore_names(encrypted)
    assert restored == names