# Python Email Sender README

This Python script is designed to send emails using the Gmail SMTP server. It uses the `email.message` and `smtplib` libraries to create and send an email with a specified subject and body to a recipient's Gmail account.

## Prerequisites

Before you can use this script, you need to have the following:

1. **Python Installed**: Ensure that you have Python installed on your computer. You can download it from the official website [here](https://www.python.org/downloads/).

2. **Gmail Account**: You must have a Gmail account as both the sender and recipient for this script to work.

3. **Less Secure Apps**: To use the Gmail SMTP server, you may need to allow less secure apps to access your Google account. You can do this by going to your Google Account settings and enabling "Less secure app access." Keep in mind that this option might not be available for all Google accounts, and it is recommended to use App Passwords if available.

## Configuration

Before running the script, you need to configure it with your specific email details:

- `email_send`: Replace 'Enter-Your-Email' with your Gmail email address (the sender's email).
- `email_pass`: Replace 'Enter-Your-Password' with your Gmail account password. **Note:** Storing your password directly in the script is not recommended for security reasons. Instead, consider using environment variables or other secure methods to store sensitive information.
- `email_rec`: You can enter the recipient's Gmail address when prompted or set it directly in the script.
- `subject`: Replace 'Enter Subject' with the subject of your email.
- `body`: Replace 'Enter Body' with the content of your email message.

## Usage

1. Configure the script by following the instructions in the "Configuration" section above.

2. Save the script with a `.py` extension, for example, `email_sender.py`.

3. Open your terminal or command prompt and navigate to the directory where the script is located.

4. Run the script using the command:

5. The script will prompt you to enter the recipient's Gmail account if you didn't set it directly in the script.

6. After entering the recipient's email, the script will send the email using the provided configuration.

## Security Considerations

- **Storing Password:** Storing your email password directly in the script is not recommended for security reasons. Consider using environment variables or other secure methods to store sensitive information.

- **Less Secure Apps:** Enabling "Less secure app access" on your Gmail account can expose your account to potential security risks. It's recommended to use App Passwords or OAuth 2.0 for more secure authentication.

- **App Passwords:** If available for your Google account, consider using App Passwords to generate a unique password for this script, rather than using your main account password.

## Disclaimer

This script is provided for educational purposes and as a starting point for sending emails programmatically. Be aware of potential security risks and use it responsibly. Always follow best practices for handling sensitive information and consider more secure alternatives for production use.

**Note:** This README assumes that you have Python and the required libraries installed and configured on your system. If you encounter issues, please refer to the documentation for Python, `email.message`, and `smtplib` for troubleshooting and further assistance.
