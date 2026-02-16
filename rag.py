import re

def reg_phone(phone: str):
    """
    Validate and normalize international phone numbers (E.164).
    - Supports ALL country codes (+1 … +998)
    - Accepts formats like:
      +9647701234567
      +44 7700 900123
      +1-415-555-2671
      9647701234567
    - Returns normalized format: +<countrycode><number>
    - Returns None if invalid
    """

    if not phone:
        return None

    phone = phone.strip()

   
    digits = re.sub(r"\D", "", phone)


    if not (8 <= len(digits) <= 15):
        return None

    if digits.startswith("0"):
        return None


    return f"+{digits}"
