import re


def check_password_strength(password: str) -> dict:
    """Evaluate password strength and return score with feedback."""
    checks = {
        "length": (len(password) >= 8, "Use at least 8 characters"),
        "uppercase": (any(c.isupper() for c in password), "Add an uppercase letter"),
        "lowercase": (any(c.islower() for c in password), "Add a lowercase letter"),
        "digit": (any(c.isdigit() for c in password), "Add a number"),
        "special": (bool(re.search(r"[!@#$%^&*(),.?\":{}|<>]", password)), "Add a special character"),
    }
    
    score = sum(passed for passed, _ in checks.values())
    failed = [msg for passed, msg in checks.values() if not passed]
    
    if score <= 2:
        strength = "Weak"
    elif score <= 4:
        strength = "Medium"
    else:
        strength = "Strong"
    
    return {"score": score, "strength": strength, "recommendations": failed}


def main():
    password = input("Enter password: ")
    result = check_password_strength(password)
    
    print(f"\nScore: {result['score']}/5")
    print(f"Strength: {result['strength']}")
    
    if result["recommendations"]:
        print("\nRecommendations:")
        for rec in result["recommendations"]:
            print(f"  • {rec}")


if __name__ == "__main__":
    main()
