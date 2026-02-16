import re
def luhn_check(number: str) -> bool:
    """Luhn algorithm to validate card number."""
    total = 0
    reverse_digits = number[::-1]
    for i, d in enumerate(reverse_digits):
        n = int(d)
        if i % 2 == 1:
            n *= 2
            if n > 9:
                n -= 9
        total += n
    return total % 10 == 0
 
def reg(cc: str):
    """
    Parse card input and return "PAN|MM|YY|CVC" or None if invalid.
    - Supports Amex (15-digit PAN + 4-digit CVC) and standard (16-digit PAN + 3-digit CVC).
    - Accepts inputs like "4340762019462213|9|28|825" or concatenated digits.
    - Ensures MM is two digits (pads with leading zero if needed).
    """
    # First try to split by any non-digit separator (handles |, spaces, -, etc.)
    parts = [p for p in re.split(r'\D+', cc) if p != '']
    if len(parts) >= 4:
        # Use first 4 parts as PAN, MM, YY, CVC (ignore extras)
        pan = parts[0]
        mm = parts[1].zfill(2)  # pad month to 2 digits
        yy = parts[2]
        cvc = parts[3]
        # normalize year: if 4-digit like 2026 keep it, if 2-digit keep it
        if len(yy) == 4 and (yy.startswith('20') or yy.startswith('19')):
            # keep 4-digit year
            pass
        elif len(yy) == 1:
            # unlikely, reject
            return None
        # determine card type by pan prefix
        is_amex = pan.startswith('34') or pan.startswith('37')
        expected_pan_len = 15 if is_amex else 16
        expected_cvc_len = 4 if is_amex else 3

        if not re.fullmatch(r'\d{%d}' % expected_pan_len, pan):
            return None
        if not re.fullmatch(r'\d{2}', mm) or not (1 <= int(mm) <= 12):
            return None
        if not (re.fullmatch(r'\d{2}', yy) or re.fullmatch(r'\d{4}', yy)):
            return None
        if not re.fullmatch(r'\d{%d}' % expected_cvc_len, cvc):
            return None
        if not luhn_check(pan):
            return None

        return f"{pan}|{mm}|{yy}|{cvc}"

    # Fallback: try to parse from a long digit string (no separators)
    digits = ''.join(re.findall(r'\d', cc))
    if not digits:
        return None

    # detect amex by prefix
    is_amex = digits.startswith('34') or digits.startswith('37')
    cvc_len = 4 if is_amex else 3

    # need at least pan + mm(2) + yy(2) + cvc
    min_len = (15 if is_amex else 16) + 2 + 2 + cvc_len
    if len(digits) < min_len:
        # maybe year is 4-digit (e.g., 2026) -> check slightly larger
        # but if less than minimal expected, fail
        return None

    # strategy: take cvc from end, then try to detect yy (2 or 4) and mm(2)
    cvc = digits[-cvc_len:]
    rest = digits[:-cvc_len]

    # assume yy is 2 digits normally
    yy_candidate = rest[-2:]
    mm_candidate = rest[-4:-2]
    pan_candidate = rest[:-4]

    # check if year might be 4-digit (starts with 20 or 19)
    if len(rest) >= 6 and rest[-4:-2] in ('20', '19'):
        # treat last 4 of rest as yyyy
        yy = rest[-4:]
        mm = rest[-6:-4]
        pan = rest[:-6]
    else:
        yy = yy_candidate
        mm = mm_candidate
        pan = pan_candidate

    # pad month if needed (in case parsed as single digit somehow)
    mm = mm.zfill(2)

    expected_pan_len = 15 if (pan.startswith('34') or pan.startswith('37')) else 16
    if not re.fullmatch(r'\d{%d}' % expected_pan_len, pan):
        return None
    if not re.fullmatch(r'\d{2}', mm) or not (1 <= int(mm) <= 12):
        return None
    if not (re.fullmatch(r'\d{2}', yy) or re.fullmatch(r'\d{4}', yy)):
        return None
    if not re.fullmatch(r'\d{%d}' % cvc_len, cvc):
        return None
    if not luhn_check(pan):
        return None

    return f"{pan}|{mm}|{yy}|{cvc}"
