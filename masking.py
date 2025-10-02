def mask(people):
    """
    TODO: Mask emails and phone numbers:
    - keep domain part of email, mask local part
    - keep last 2 digits of phone number, mask the rest with asterisks
    - return same datastructure with masked data
    """
    masked = []
    for person in people:
        email = person["email"]
        if "@" in email:
            local, domain = email.split("@", 1)
            email_masked = "*" * len(local) + "@" + domain
        else:
            email_masked = "*" * len(email)

        phone = person["phone"]
        if len(phone) > 2:
            phone_masked = "*" * (len(phone) - 2) + phone[-2:]
        else:
            phone_masked = "*" * len(phone)

        masked.append({
            "name": person["name"],
            "email": email_masked,
            "phone": phone_masked
        })
    return masked