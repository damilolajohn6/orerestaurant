import os

from app import create_app

# Create an application instance
app = create_app(config_name='production')

if __name__ == '__main__':
    # Run the app with debug mode off for production
    app.run(debug=False, host='0.0.0.0', port=int(os.environ.get('PORT', 5000)))
