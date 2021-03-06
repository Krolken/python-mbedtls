"""Data Encryption Standard (DES) cipher developed by IBM
in the 70's."""


__author__ = "Mathias Laurin"
__copyright__ = "Copyright 2016, Elaborated Networks GmbH"
__license__ = "MIT License"


from . import _cipher
from mbedtls.exceptions import *

__all__ = ["block_size", "key_size", "new"]


block_size = 8
key_size = 8


def new(key, mode, iv=None):
    """Return a `Cipher` object that can perform DES encryption and
    decryption.

    Data Encryption Standard (DES) cipher developed by IBM in the 70's.

    Parameters:
        key (bytes or None): The key to encrypt decrypt.  If None,
            encryption and decryption are unavailable.
        mode (Mode): The mode of operation of the cipher.
        iv (bytes or None): The initialization vector (IV).  The IV is
            required for every mode but ECB and CTR where it is ignored.
            If not set, the IV is initialized to all 0, which should not
            be used for encryption.

    """
    mode = _cipher.Mode(mode)
    if len(key) != key_size:
        raise TLSError(msg="key size must be 16 bytes, got %r" % len(key))
    if mode not in {_cipher.Mode.ECB, _cipher.Mode.CBC}:
        raise TLSError(msg="unsupported mode %r" % mode)
    name = ("DES-%s" % mode.name).encode("ascii")
    return _cipher.Cipher(name, key, mode, iv)
