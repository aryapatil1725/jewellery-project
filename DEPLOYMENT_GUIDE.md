# Deployment Guide for Jewellery Project

## ✅ Fixed Issues

The following critical issues have been fixed:
- ✅ Removed syntax error (`app.py (main file)=`)
- ✅ Removed redundant code (`app = app`)
- ✅ Changed hardcoded secret key to environment variable
- ✅ Changed hardcoded database credentials to environment variables
- ✅ Created `.env.example` template file

## 🔧 Pre-Deployment Checklist

### 1. Set Up Cloud Database

Your application needs a cloud database for production deployment. Options include:

#### Recommended: PlanetScale (Free Tier Available)
- Sign up at https://planetscale.com/
- Create a new database
- Get connection details (host, username, password, database name)
- Import your existing database schema

#### Alternative Options:
- AWS RDS
- Google Cloud SQL
- Azure Database for MySQL
- Railway MySQL
- Render MySQL

### 2. Generate Strong Secret Key

Run this Python command to generate a secure secret key:
```bash
python -c "import secrets; print(secrets.token_hex(32))"
```

### 3. Configure Environment Variables

For **Vercel Deployment**, set these in your Vercel dashboard:
- `SECRET_KEY` = (your generated secret key)
- `DB_HOST` = (your cloud database host)
- `DB_USER` = (your database username)
- `DB_PASSWORD` = (your database password)
- `DB_NAME` = (your database name, e.g., jewellerydb)

For **Local Development**:
1. Copy `.env.example` to `.env`
2. Fill in your local database credentials
3. The `.env` file is already in `.gitignore` for security

### 4. Database Schema Migration

Export your local database schema:
```bash
mysqldump -u root -p jewellerydb > schema.sql
```

Import to your cloud database:
```bash
mysql -h <cloud-host> -u <cloud-user> -p <cloud-db> < schema.sql
```

## 🚀 Deployment Steps

### Option 1: Deploy to Vercel

1. **Push to GitHub** (if not already done)
   ```bash
   git add .
   git commit -m "Fix deployment issues"
   git push origin main
   ```

2. **Deploy on Vercel**
   - Go to https://vercel.com/
   - Import your GitHub repository
   - Configure environment variables
   - Deploy

3. **Update `vercel.json` if needed**
   - Current configuration is basic but functional
   - Consider adding build settings if needed

### Option 2: Deploy to Railway/Render

1. Sign up at https://railway.app/ or https://render.com/
2. Connect your GitHub repository
3. Add environment variables
4. Deploy

## ⚠️ Important Notes

### Static Files Issue
Your static files are in `/static/` outside the main project folder. This may cause 404 errors in production.

**Solutions:**
1. **Recommended**: Move `static/` folder inside `jewellery project/`
2. Or configure Flask to look in the parent directory

### Folder Name with Spaces
The folder name "jewellery project" contains spaces, which can cause issues in some deployment environments.

**Solution**: Consider renaming to `jewellery-project` or `jewellery_project`

## 🧪 Testing Before Deployment

1. **Test locally with environment variables:**
   ```bash
   # Install dependencies
   pip install -r requirements.txt
   
   # Set environment variables or create .env file
   cp .env.example .env
   # Edit .env with your credentials
   
   # Run the app
   python "jewellery project/app.py"
   ```

2. **Test all routes and functionality**
3. **Test database connections**
4. **Test file uploads (if any)**

## 📋 Environment Variables Reference

| Variable | Purpose | Example |
|----------|---------|---------|
| `SECRET_KEY` | Flask session encryption | `a1b2c3d4e5f6...` (32+ chars) |
| `DB_HOST` | Database host | `aws.connect.psdb.cloud` |
| `DB_USER` | Database username | `your_username` |
| `DB_PASSWORD` | Database password | `your_secure_password` |
| `DB_NAME` | Database name | `jewellerydb` |

## 🔒 Security Best Practices

- ✅ Never commit `.env` file to git
- ✅ Use strong, unique passwords
- ✅ Rotate secrets periodically
- ✅ Use HTTPS in production
- ✅ Keep dependencies updated
- ✅ Enable database connection pooling if needed

## 🐛 Troubleshooting

### Database Connection Failed
- Check environment variables are set correctly
- Verify database host is accessible
- Ensure database user has proper permissions
- Check if IP is whitelisted (for cloud databases)

### 500 Internal Server Error
- Check Vercel/Railway logs
- Ensure all dependencies are in requirements.txt
- Verify Python version compatibility

### Static Files Not Loading
- Move static files into project folder
- Or update Flask configuration

### Session Issues
- Ensure SECRET_KEY is set
- Use the same SECRET_KEY across all instances

## 📞 Support

For deployment issues:
1. Check deployment platform logs
2. Review environment variables
3. Test database connection separately
4. Check Python version compatibility

## ✨ Ready to Deploy?

Once you've:
- ✅ Set up cloud database
- ✅ Configured environment variables
- ✅ Tested locally
- ✅ Pushed to GitHub

You're ready to deploy! 🚀