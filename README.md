# Online Shop

The Online Shop is a Flask-based web application that provides a platform for customers to browse products, add them to their cart, and proceed to checkout. It also features a secure authentication system for user registration and login, as well as an admin panel for managing products. The application uses Stripe for payment processing.

## Features

- User registration and login: Users can create accounts, log in, and log out. The first registration is admin.
- Product display: Products are listed on the main page with their names, prices, and images.
- Cart management: Users can add products to their carts and view the number of items in their carts.
- Checkout: Secure checkout process using Stripe for payment.
- Administrator product management: Admin users can add, update, and delete products.

## Installation

1. Clone the repository to your local machine:

   ```bash
   git clone https://github.com/your-username/online-shop.git
   ```

2. Install the required packages using pip:

   ```bash
   pip install -r requirements.txt
   ```

3. Set up environment variables:

   - Create a `.env` file in the project directory.
   - Add your Stripe API key as follows:

     ```
     API_KEY=your_stripe_api_key_here
     ```

4. Run the application:

   ```bash
   python main.py
   ```

5. Access the application in your web browser at `http://127.0.0.1:5000`.

## Usage

- Register as a user to access the online shop.
- Browse the available products on the main page.
- Add products to your cart and proceed to checkout.
- Admin users can manage products by adding, updating, and deleting them.

## License

This project is licensed under the [MIT License](LICENSE).

Feel free to contribute to the project by submitting pull requests or opening issues. Happy coding!
