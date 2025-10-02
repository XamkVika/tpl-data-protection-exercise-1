from cryptography.fernet import Fernet

"""
TODO:
- Generate a key once and reuse it for both pseudonymization and restoration. In a real system, this key would be securely stored.
"""


def pseudonymize_names(names):
    """
    TODO: Encrypt each name with Fernet symmetric encryption.
    - print encrypted names
    - return list of encrypted names
    """

    pass


def restore_names(encrypted: list[str]) -> list[str]:
    """
    TODO: Decrypt previously pseudonymized names.
    - print decrypted names
    - return list of decrypted names
    """

    pass