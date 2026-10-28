
# Lab 5: Static Code Analysis- Issues Table

| No. | Issue | Type / Tool | Original Finding | How It Was Addressed |
|---:|---|---|---|---|
| 1 | Missing module docstring | Code quality — Pylint C0114 | The Python file did not describe its purpose. | Added a module-level docstring explaining the parcel tracking application. |
| 2 | Missing function docstrings | Code quality — Pylint C0116 | Functions did not document their purpose. | Added descriptive docstrings to all functions. |
| 3 | Non-standard naming conventions | Style — Pylint C0103 | Names such as `bookParcel`, `weightKg`, and `trackingId` did not follow PEP 8 conventions. | Renamed functions, arguments, and variables using `snake_case`. |
| 4 | Mutable default argument | Bug — Pylint W0102 | The `history=[]` default could be shared between function calls. | Changed the default to `None` and initialized a new list inside the function. |
| 5 | Broad exception handling | Code quality — Pylint W0718 | Catching `Exception` could hide unrelated errors. | Replaced broad exception handling with explicit handling of missing parcel IDs. |
| 6 | Insecure temporary-file creation | Security — Bandit B306 | `tempfile.mktemp()` can introduce a race condition. | Replaced it with `tempfile.NamedTemporaryFile()`. |
| 7 | Shell command injection risk | Security — Bandit B602 | A shell command used `shell=True` with concatenated input. | Removed the unused ping helper and its subprocess import. |
| 8 | Insecure OTP generation | Security — Bandit B311 | `random.randint()` is not suitable for security-sensitive tokens. | Replaced it with `secrets.randbelow()`. |
| 9 | Formatting violations | Style — Flake8 E225, E261, E231, E305 | The source contained spacing and blank-line violations. | Corrected operator spacing, comment spacing, whitespace after commas, and blank lines. |
| 10 | Subprocess-related warnings | Security — Bandit B404, B607, B603 | The ping helper introduced subprocess-related security warnings. | Removed the unused helper and the subprocess import. |

## Final verification results

| Tool | Initial Result | Final Result |
|---|---|---|
| Pylint | 4.91/10 | 10.00/10 |
| Bandit | 1 high, 1 medium, 2 low findings | 0 findings |
| Flake8 | 4 violations | 0 violations |
