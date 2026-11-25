import getpass
import re
from zxcvbn import zxcvbn


MIN_LENGTH = 15
MAX_LENGTH = 128

STRENGTH_LABELS = {
    0: "Very Weak",
    1: "Weak",
    2: "Fair",
    3: "Strong",
    4: "Very Strong"
}


def check_policy(password):
    """Check each password rule and return pass/fail results."""
    checks = []

    length = len(password)

    checks.append({
        "name": "Length",
        "passed": MIN_LENGTH <= length <= MAX_LENGTH,
        "message": (
            f"Good length: {length} characters"
            if MIN_LENGTH <= length <= MAX_LENGTH
            else f"Use between {MIN_LENGTH} and {MAX_LENGTH} characters"
        )
    })

    checks.append({
        "name": "Lowercase letters",
        "passed": bool(re.search(r"[a-z]", password)),
        "message": (
            "Contains lowercase letters"
            if re.search(r"[a-z]", password)
            else "Add lowercase letters"
        )
    })

    checks.append({
        "name": "Uppercase letters",
        "passed": bool(re.search(r"[A-Z]", password)),
        "message": (
            "Contains uppercase letters"
            if re.search(r"[A-Z]", password)
            else "Add uppercase letters"
        )
    })

    checks.append({
        "name": "Numbers",
        "passed": bool(re.search(r"\d", password)),
        "message": (
            "Contains numbers"
            if re.search(r"\d", password)
            else "Add numbers"
        )
    })

    checks.append({
        "name": "Special characters",
        "passed": bool(re.search(r"[^A-Za-z0-9\s]", password)),
        "message": (
            "Contains special characters"
            if re.search(r"[^A-Za-z0-9\s]", password)
            else "Add special characters such as ! @ # $ %"
        )
    })

    checks.append({
        "name": "No repeated characters",
        "passed": not bool(re.search(r"(.)\1{2,}", password)),
        "message": (
            "No long repeated-character patterns"
            if not re.search(r"(.)\1{2,}", password)
            else "Avoid repeating the same character three or more times"
        )
    })

    checks.append({
        "name": "No predictable sequences",
        "passed": not bool(
            re.search(
                r"(?:0123|1234|2345|3456|4567|5678|6789|abcd|bcde|cdef)",
                password.lower()
            )
        ),
        "message": (
            "No predictable sequences"
            if not re.search(
                r"(?:0123|1234|2345|3456|4567|5678|6789|abcd|bcde|cdef)",
                password.lower()
            )
            else "Avoid predictable sequences such as '1234' or 'abcd'"
        )
    })

    checks.append({
        "name": "No obvious years",
        "passed": not bool(re.search(r"\b(?:19|20)\d{2}\b", password)),
        "message": (
            "No obvious years detected"
            if not re.search(r"\b(?:19|20)\d{2}\b", password)
            else "Avoid obvious years or dates"
        )
    })

    return checks


def assess_password(password, user_inputs=None):
    """Assess password strength using zxcvbn and custom rules."""
    if not password:
        return {
            "score": 0,
            "strength": "Very Weak",
            "crack_time": "instantly",
            "guesses": 0,
            "checks": [],
            "warnings": ["Enter a password to assess it."],
            "suggestions": ["Use a long, unique passphrase."]
        }

    result = zxcvbn(
        password,
        user_inputs=user_inputs or []
    )

    checks = check_policy(password)

    failed_checks = [
        check["message"]
        for check in checks
        if not check["passed"]
    ]

    warnings = []

    if result["feedback"]["warning"]:
        warnings.append(result["feedback"]["warning"])

    warnings.extend(result["feedback"]["suggestions"])
    warnings.extend(failed_checks)
    warnings = list(dict.fromkeys(warnings))

    if warnings:
        suggestions = warnings
    else:
        suggestions = [
            "Excellent password. Keep it private, unique, "
            "and consider using a password manager."
        ]

    crack_time = result["crack_times_display"][
        "offline_slow_hashing_1e4_per_second"
    ]

    return {
        "score": result["score"],
        "strength": STRENGTH_LABELS[result["score"]],
        "crack_time": crack_time,
        "guesses": result["guesses"],
        "checks": checks,
        "warnings": warnings,
        "suggestions": suggestions
    }


def show_report(result):
    print("\n" + "=" * 55)
    print("🔐 PASSWORD STRENGTH REPORT")
    print("=" * 55)
    print(f"Strength:                 {result['strength']}")
    print(f"Score:                    {result['score']}/4")
    print(f"Estimated time to crack:  {result['crack_time']}")

    if result["checks"]:
        print("\n📋 Password Requirements:")

        for check in result["checks"]:
            if check["passed"]:
                symbol = "✅ PASS"
            else:
                symbol = "❌ FAIL"

            print(f"   {symbol} | {check['message']}")

    if result["warnings"]:
        print("\n⚠️  Improvement suggestions:")
        for item in result["warnings"]:
            print(f"   • {item}")
    else:
        print("\n🎉 No major weaknesses detected.")

    print("=" * 55 + "\n")


def main():
    print("🔐 Advanced Password Complexity Checker")
    print("-" * 55)
    print("Your password is hidden and checked locally only.\n")

    password = getpass.getpass("Enter a password: ")

    personal_input = input(
        "Enter personal words to avoid "
        "(comma-separated, optional): "
    ).strip()

    user_inputs = [
        word.strip()
        for word in personal_input.split(",")
        if word.strip()
    ]

    result = assess_password(password, user_inputs)
    show_report(result)


if __name__ == "__main__":
    main()