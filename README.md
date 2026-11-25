<div align="center">

# 🔐 Password Complexity Checker

### Smart Password Strength Analyzer

**Check. Improve. Secure. — before you use it.**

![Python](https://img.shields.io/badge/Python-3.8%2B-3776AB?style=for-the-badge&logo=python&logoColor=white)
![zxcvbn](https://img.shields.io/badge/Engine-zxcvbn-E34F26?style=for-the-badge)
![Interface](https://img.shields.io/badge/Interface-CLI-4EAA25?style=for-the-badge&logo=gnubash&logoColor=white)
![Privacy](https://img.shields.io/badge/Privacy-100%25%20Local-2ea44f?style=for-the-badge)
![Status](https://img.shields.io/badge/Status-Active-brightgreen?style=for-the-badge)

`Strength Scoring` · `Pattern Detection` · `Personal-Word Detection` · `Crack-Time Estimation` · `Actionable Feedback`

[Features](#-key-features) · [Install](#%EF%B8%8F-installation) · [Usage](#-running-the-project) · [Examples](#-example-usage) · [Roadmap](#-future-improvements)

</div>

---

## 🎯 Overview

**Password Complexity Checker** is a Python security tool that analyzes a password *before* you use it. It looks at length, character variety, repeated characters, predictable sequences, obvious years, and personal information.

Instead of a vague "weak" or "strong" verdict, it gives you a detailed **pass/fail report** and **practical suggestions** for building a better password.

> [!WARNING]
> A password can look complex and still be easy to guess. **Analyze before you trust it.**

### What it checks

| | |
|---|---|
| 📏 Password length | 🔁 Repeated characters |
| 🔤 Uppercase & lowercase letters | 🔢 Predictable sequences (`1234`, `abcd`) |
| #️⃣ Numbers & special characters | 📅 Obvious years or dates |
| 👤 Personal words you provide | 🧠 Common patterns via `zxcvbn` |
| ⏱️ Estimated offline crack time | |

---

## ✨ Key Features

| Feature | Description |
|---|---|
| 🔐 **Strength Analysis** | Uses `zxcvbn`, a realistic password-strength estimator |
| 📏 **Length Checking** | Encourages passwords of at least 15 characters |
| 🔤 **Character Variety** | Checks lowercase, uppercase, numbers, and special characters |
| 🔁 **Repeat Detection** | Catches patterns such as `aaa` or `111` |
| 🔢 **Sequence Detection** | Flags sequences such as `1234` or `abcd` |
| 📅 **Date & Year Detection** | Detects obvious years such as `2004` or `2026` |
| 👤 **Personal Words** | Lets you enter names, cities, or other words to avoid |
| ⏱️ **Crack-Time Estimate** | Estimates how long an offline attack might take |
| 📊 **Strength Score** | Score from 0 to 4 with a clear label |
| ✅ **Pass/Fail Report** | Shows every requirement as PASS or FAIL |
| 💡 **Actionable Feedback** | Specific suggestions to fix weak passwords |
| 🛡️ **Local Privacy** | Nothing is stored or transmitted |

---

## 🏗️ Project Structure

```text
CS_02_pswd_complexity/
├── pswd_checker.py        # Main password analysis program
├── requirements.txt       # Python dependencies
├── README.md              # Project documentation
└── password_report.txt    # Optional saved report (if implemented)
```

---

## ⚙️ Installation

**Prerequisites:** Python 3.8+ and pip.

**1. Open the project folder**

```cmd
D:
cd "D:\College\Projects\PRODIGY_INTERNSHIP\CS_02_pswd_complexity"
```

**2. Install dependencies**

```cmd
python -m pip install zxcvbn
```

Or use a `requirements.txt` containing `zxcvbn`:

```cmd
python -m pip install -r requirements.txt
```

---

## 🚀 Running the Project

```cmd
python pswd_checker.py
```

You will see:

```text
🔐 Advanced Password Complexity Checker
-------------------------------------------------------
Your password is hidden and checked locally only.

Enter a password:
Enter personal words to avoid (comma-separated, optional):
```

> [!NOTE]
> The password is hidden while typing, so it never appears on screen.

---

## 🖥️ How It Works

```text
                     👤 USER
                        │
                        ▼
        ┌───────────────────────────────┐
        │  Enter password + personal    │
        │  words (hidden input)         │
        └───────────────┬───────────────┘
                        │
          ┌─────────────┴─────────────┐
          ▼                           ▼
 ┌──────────────────┐       ┌──────────────────────┐
 │ zxcvbn analysis  │       │ Custom rule checks   │
 │ patterns &       │       │ length · characters  │
 │ dictionaries     │       │ sequences · years    │
 └────────┬─────────┘       └──────────┬───────────┘
          └─────────────┬──────────────┘
                        ▼
          ┌───────────────────────────┐
          │ Strength score (0 – 4)    │
          └─────────────┬─────────────┘
                        ▼
          ┌───────────────────────────┐
          │ Pass/Fail report +        │
          │ improvement feedback      │
          └─────────────┬─────────────┘
                        ▼
  🔴 Very Weak → 🟠 Weak → 🟡 Fair → 🟢 Strong → 🟢 Very Strong
```

---

## 📊 Password Strength System

### Strength levels

| Score | Level | |
|:---:|---|:---:|
| 0 / 4 | Very Weak | 🔴 |
| 1 / 4 | Weak | 🟠 |
| 2 / 4 | Fair | 🟡 |
| 3 / 4 | Strong | 🟢 |
| 4 / 4 | Very Strong | 🟢 |

### Password rules

| Rule | Effect |
|---|:---:|
| At least 15 characters | ✅ Positive |
| Contains lowercase letters | ✅ Positive |
| Contains uppercase letters | ✅ Positive |
| Contains numbers | ✅ Positive |
| Contains special characters | ✅ Positive |
| Repeated characters | ❌ Negative |
| Predictable sequences | ❌ Negative |
| Obvious years or dates | ❌ Negative |
| Personal words detected | ❌ Negative |
| Common password pattern | ❌ Negative |

---

## 📋 Pass/Fail Report

A fully passing password looks like this:

```text
📋 Password Requirements:

   ✅ PASS | Good length: 22 characters
   ✅ PASS | Contains lowercase letters
   ✅ PASS | Contains uppercase letters
   ✅ PASS | Contains numbers
   ✅ PASS | Contains special characters
   ✅ PASS | No long repeated-character patterns
   ✅ PASS | No predictable sequences
   ✅ PASS | No obvious years detected
```

When a rule fails, you immediately see what to fix:

```text
   ❌ FAIL | Use between 15 and 128 characters
   ❌ FAIL | Add uppercase letters
   ❌ FAIL | Add special characters such as ! @ # $ %
   ❌ FAIL | Avoid obvious years or dates
```

---

## 🧪 Test Cases

| Password | Expected result |
|---|---|
| `password123` | 🔴 **Very Weak**: common password, predictable pattern |
| `P@ssw0rd` | 🟠 **Weak / Fair**: looks complex but is a common pattern |
| `abhay123` | 🔴 **Very Weak**: short, personal word, predictable number |
| `Mayank@2004` | 🟠 **Weak**: personal-style name and obvious year |
| `Aaaa1111!!!!` | 🟠 **Weak**: repeated characters, predictable pattern |
| `Sun@Moon#Rain7Cloud!` | 🟢 **Strong / Very Strong**: long and varied |
| `Blue$Tiger42Runs!Fast` | 🟢 **Very Strong**: long, varied, unpredictable |
| `correct-horse-battery-staple-42!` | 🟢 **Very Strong**: long passphrase, high entropy |

---

## 💡 Example Usage

### ✅ Strong password

```text
Enter a password: Blue$Tiger42Runs!Fast
Enter personal words to avoid (comma-separated, optional): abhay, sharma, 123, fash
```

```text
=======================================================
🔐 PASSWORD STRENGTH REPORT
=======================================================
Strength:                 Very Strong
Score:                    4/4
Estimated time to crack:  centuries

📋 Password Requirements:

   ✅ PASS | Good length: 22 characters
   ✅ PASS | Contains lowercase letters
   ✅ PASS | Contains uppercase letters
   ✅ PASS | Contains numbers
   ✅ PASS | Contains special characters
   ✅ PASS | No long repeated-character patterns
   ✅ PASS | No predictable sequences
   ✅ PASS | No obvious years detected

🎉 No major weaknesses detected.

=======================================================
```

### ❌ Weak password

```text
Enter a password: abhay123
Enter personal words to avoid (comma-separated, optional): abhay, sharma, 123, fash
```

```text
=======================================================
🔐 PASSWORD STRENGTH REPORT
=======================================================
Strength:                 Very Weak
Score:                    0/4
Estimated time to crack:  instantly

📋 Password Requirements:

   ❌ FAIL | Use between 15 and 128 characters
   ✅ PASS | Contains lowercase letters
   ❌ FAIL | Add uppercase letters
   ✅ PASS | Contains numbers
   ❌ FAIL | Add special characters such as ! @ # $ %
   ✅ PASS | No long repeated-character patterns
   ✅ PASS | No predictable sequences
   ✅ PASS | No obvious years detected
   ❌ FAIL | Remove personal words (found: abhay, 123)

⚠️  Improvement suggestions:
   • Use at least 15 characters. Longer passphrases are much harder to guess.
   • Add uppercase letters.
   • Add special characters such as ! @ # $ %
   • Remove personal words from your password.

=======================================================
```

---

## 🛠️ Tech Stack

| Layer | Technology |
|---|---|
| **Language** | Python 3.8+ |
| **Strength engine** | `zxcvbn` |
| **Pattern matching** | Python `re` module |
| **Secure input** | `getpass` |
| **Interface** | Command-line |
| **Output** | Terminal strength report |

---

## 🔐 Security Notes

- 🙈 Input is read with `getpass`, so the password stays hidden while typing.
- 💻 Analysis happens only on your machine. Nothing is saved, stored, or transmitted.
- 👤 Personal words are used only to improve local analysis.
- 🎓 This is an educational tool, not a replacement for enterprise authentication.
- 🗄️ In real applications, store passwords only as salted hashes (**Argon2id**, **bcrypt**, or **PBKDF2**).
- 📘 NIST guidance favors long passwords, allowing at least 64 characters, permitting paste, and avoiding complexity-only rules.

---

## 🚀 Future Improvements

- [ ] 🖥️ Graphical interface with Tkinter
- [ ] 👁️ Show/hide password toggle
- [ ] 🔑 Secure random password generator
- [ ] 🌐 Breached-password database check
- [ ] 📄 Save analysis reports locally
- [ ] 📊 Password entropy calculation
- [ ] 🧪 Automated unit tests
- [ ] 🌍 Multi-language support

---

## 🤝 Contributing

```bash
git checkout -b feature/your-feature-name
git commit -m "Add: your feature description"
git push origin feature/your-feature-name
# Then open a Pull Request 🎉
```

---

<div align="center">

⭐ **Star this repository if it helped you create stronger passwords!**

*Think Long · Stay Unique · Protect Your Accounts*

Made with ❤️ using **Python** · **zxcvbn** · **Regular Expressions**

</div>
