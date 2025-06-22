# Vercel Deployment Entry Point
# This file launches the Flask app for Vercel deployment

from app_vercel import app

# Vercel requires this for serverless deployment
if __name__ == '__main__':
    app.run() 