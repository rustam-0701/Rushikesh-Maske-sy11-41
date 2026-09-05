import re

# Email pattern
EMAIL_PATTERN = r'[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9.-]+'


# Function to find all emails
def find_emails(text):
    return re.findall(EMAIL_PATTERN, text)


# Function to validate one email
def is_valid_email(candidate):
    return re.fullmatch(EMAIL_PATTERN, candidate) is not None


# Main program
if __name__ == "__main__":

    sample_text = """
    Please contact us:
    support@examplecorp.com
    sales.team@business-hub.co.in
    rahul_23@gmail.com
    not-an-email
    @missing-local.com
    newsletter+promo@my-site.org
    """

    print("Original Text:")
    print(sample_text)

    # Find emails
    found = find_emails(sample_text)

    print("Found", len(found), "email address(es):")

    for email in found:
        print("-", email)

    # Validate emails
    print("\nEmail Validation:")

    test_cases = [
        "john.doe@example.com",
        "invalid-email",
        "user@site",
        "user@site.com",
        "plain.text@",
        "a.b-c_d+e@sub.domain.co.in"
    ]

    for candidate in test_cases:
        if is_valid_email(candidate):
            print(candidate, "-> VALID")
        else:
            print(candidate, "-> INVALID")