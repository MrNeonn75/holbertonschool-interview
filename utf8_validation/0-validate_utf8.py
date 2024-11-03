#!/usr/bin/python3
""" UTF-8 Validation """


def validUTF8(data):
    """
    Determines if a given data set represents a valid UTF-8 encoding.

    A character in UTF-8 can be 1 to 4 bytes long. For each character:
    - A 1-byte character starts with a '0' (binary format `0xxxxxxx`).
    - A 2-byte character starts with '110' followed by a '10' byte.
    - A 3-byte character starts with '1110' followed by two '10' bytes.
    - A 4-byte character starts with '11110' followed by three '10' bytes.

    Parameters:
    -----------
    data : List[int]
        A list of integers where each integer represents
        a byte (0-255). Only the 8 least significant bits of
        each integer are considered for UTF-8 validation.

    Returns:
    --------
    bool
        True if data represents a valid UTF-8 encoding, False otherwise.

    Examples:
    ---------
    >>> validUTF8([65])
    True
    >>> validUTF8([229, 65, 127, 256])
    False
    >>> validUTF8([197, 130, 1])
    True

    Explanation:
    ------------
    - The function iterates through each byte in the input `data`.
    - `num_bytes` is used to track how many remaining bytes are needed
    to complete the current character.
    - For each byte:
        - If `num_bytes` is 0, we determine the number of bytes
        in the current UTF-8 character.
        - If `num_bytes` > 0, we check if the current byte is a valid
        continuation byte, which must start with '10'.
    - If `num_bytes` is 0 at the end, the encoding is valid.
    """
    # Number of bytes in the current UTF-8 character
    num_bytes = 0
    # Masks to check the most significant bits
    mask1 = 1 << 7  # 10000000
    mask2 = 1 << 6  # 01000000
    for num in data:
        # Mask to only get the least significant 8 bits
        byte = num & 0xFF

        if num_bytes == 0:
            # Determine the number of bytes in the UTF-8 character
            if (byte >> 5) == 0b110:   # 2-byte character
                num_bytes = 1
            elif (byte >> 4) == 0b1110:  # 3-byte character
                num_bytes = 2
            elif (byte >> 3) == 0b11110:  # 4-byte character
                num_bytes = 3
            elif (byte >> 7):  # 1-byte character must start with 0
                return False
        else:
            # Check that the byte starts with '10' for multi-byte characters
            if not (byte & mask1 and not (byte & mask2)):
                return False
            num_bytes -= 1

    return num_bytes == 0
