# Basic Authentication App With DJANGO

An easy-to-implement Django authentication system that handles user registration, login, profile management, and password reset functionality.

## Features

- User registration with profile support.
- User login and logout.
- Profile view and update functionality.
- Password reset through email.
- Admin panel integration for user management.
- Media file support in DEBUG mode.

## Setup and Installation

1. **Clone the Repository**:
    \`\`\`bash
    git clone [repo-link] authentication_app
    cd authentication_app
    \`\`\`

2. **Install Requirements**:
    \`\`\`bash
    pip install -r requirements.txt
    \`\`\`

3. **Run Migrations**:
    \`\`\`bash
    python manage.py migrate
    \`\`\`

4. **Run the Development Server**:
    \`\`\`bash
    python manage.py runserver
    \`\`\`

## Usage

- Navigate to the root URL to access the home page.
- Use \`/register/\` for user registration.
- Use \`/login/\` for user login.
- Access user profile using \`/profile/\`.
- For password reset:
    - Start the process using \`/password-reset/\`.
    - Confirmation message at \`/password-reset/done/\`.
    - Confirm the reset with the link provided in the email: \`/password-reset/confirm/<uidb64>/<token>/\`.
    - Completion message at \`/password-reset/complete/\`.
- Admin functionalities can be accessed using \`/admin/\`.

## Customization

- Templates are located within a folder named \`users\`. You can customize the HTML templates to match your application's design.
- Add or modify URL patterns in the \`urls.py\` file if required.

## Contributing

Pull requests are welcome! For major changes, please open an issue first to discuss the change.

## License

[MIT License](LICENSE) - so feel free to use parts of the app in your own projects.

