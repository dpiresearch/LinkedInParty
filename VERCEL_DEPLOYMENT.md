# 🚀 Vercel Deployment Guide for Party Planner

This guide will help you deploy your Party Planner app to Vercel in just a few minutes!

## 📋 Prerequisites

- A GitHub account
- A Vercel account (free at [vercel.com](https://vercel.com))
- Your Party Planner code pushed to GitHub

## 🎯 Step-by-Step Deployment

### 1. **Prepare Your Repository**

Make sure your code is pushed to GitHub with these files:
- `app.py` (main entry point)
- `app_vercel.py` (Flask app)
- `vercel.json` (Vercel configuration)
- `requirements.txt` (Python dependencies)
- `templates/` folder (HTML templates)
- `static/` folder (CSS, JS, images)

### 2. **Sign Up for Vercel**

1. Go to [vercel.com](https://vercel.com)
2. Click "Sign Up" and choose "Continue with GitHub"
3. Authorize Vercel to access your GitHub account

### 3. **Deploy Your App**

1. **Click "New Project"** in your Vercel dashboard
2. **Import your GitHub repository**:
   - Select your Party Planner repository
   - Vercel will automatically detect it's a Python project
3. **Configure the project**:
   - **Framework Preset**: Other
   - **Root Directory**: `./` (leave as default)
   - **Build Command**: Leave empty (Vercel will auto-detect)
   - **Output Directory**: Leave empty
   - **Install Command**: `pip install -r requirements.txt`
4. **Click "Deploy"**

### 4. **Wait for Deployment**

Vercel will:
- Install your Python dependencies
- Build your Flask app
- Deploy it to a global CDN
- Give you a URL (usually `your-app-name.vercel.app`)

## 🔧 Configuration Details

### Vercel Configuration (`vercel.json`)
```json
{
  "version": 2,
  "builds": [
    {
      "src": "app.py",
      "use": "@vercel/python"
    }
  ],
  "routes": [
    {
      "src": "/(.*)",
      "dest": "app.py"
    }
  ]
}
```

### Requirements (`requirements.txt`)
```
flask==3.0.0
flask-cors==4.0.0
werkzeug==3.1.3
```

## 🌐 Custom Domain (Optional)

1. In your Vercel dashboard, go to your project
2. Click "Settings" → "Domains"
3. Add your custom domain
4. Follow the DNS configuration instructions

## 📊 Monitoring & Analytics

Vercel provides:
- **Real-time analytics** on your dashboard
- **Performance monitoring**
- **Error tracking**
- **Deployment logs**

## 🔄 Automatic Deployments

Every time you push to your GitHub repository:
- Vercel automatically detects changes
- Builds and deploys the new version
- Updates your live site

## 🛠️ Troubleshooting

### Common Issues:

1. **Build Fails**
   - Check your `requirements.txt` has all dependencies
   - Ensure `app.py` imports correctly from `app_vercel.py`

2. **App Not Loading**
   - Check the deployment logs in Vercel dashboard
   - Verify your Flask routes are working

3. **File Upload Issues**
   - Vercel is serverless, so file uploads work differently
   - The app processes files in memory (no disk writes)

### Debug Commands:

```bash
# Test locally before deploying
python app.py

# Check if all imports work
python -c "from app_vercel import app; print('App loaded successfully')"
```

## 🎉 Success!

Once deployed, your app will be available at:
- **Production URL**: `https://your-app-name.vercel.app`
- **Preview URLs**: For each pull request

## 📈 Performance Benefits

- **Global CDN**: Your app loads fast worldwide
- **Automatic HTTPS**: Secure by default
- **Serverless**: Scales automatically
- **Edge Functions**: Low latency responses

## 💰 Pricing

- **Free Tier**: Perfect for personal projects
- **Pro Plan**: $20/month for more features
- **Enterprise**: Custom pricing for large teams

## 🔗 Useful Links

- [Vercel Documentation](https://vercel.com/docs)
- [Python on Vercel](https://vercel.com/docs/runtimes#official-runtimes/python)
- [Flask Deployment Guide](https://vercel.com/guides/deploying-flask-with-vercel)

---

**Your Party Planner app is now live on Vercel! 🎉** 