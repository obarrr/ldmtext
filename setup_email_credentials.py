#!/usr/bin/env python3
"""
One-time setup: store the SMTP password for robert@theobarrs.com in
Windows Credential Manager (via the `keyring` package), so
send_chapter.py never needs the password typed again.

Run this yourself in a terminal (the password prompt is hidden and
never echoed, logged, or written to any file):

  py setup_email_credentials.py

To verify it was stored (prints True/False, never the password itself):
  py setup_email_credentials.py --check

To remove it:
  py setup_email_credentials.py --remove
"""
import getpass
import sys

import keyring

SERVICE = "libro_de_mormon_smtp"
USERNAME = "robert@theobarrs.com"


def main():
    if "--check" in sys.argv:
        stored = keyring.get_password(SERVICE, USERNAME) is not None
        print(f"Credential stored for {USERNAME}: {stored}")
        return
    if "--remove" in sys.argv:
        keyring.delete_password(SERVICE, USERNAME)
        print(f"Removed stored credential for {USERNAME}.")
        return

    print(f"Enter the SMTP password/app-password for {USERNAME}.")
    print("(input is hidden; nothing is echoed, logged, or written to a file)")
    password = getpass.getpass("Password: ")
    if not password:
        print("Empty password entered — aborting, nothing stored.")
        sys.exit(1)
    keyring.set_password(SERVICE, USERNAME, password)
    print("Stored in Windows Credential Manager. You will not need to enter it again.")


if __name__ == "__main__":
    main()
