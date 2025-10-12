#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
Cryzen Discord Embed Server
Standalone Flask server for creating custom Discord embeds using Open Graph meta tags
"""

from flask import Flask, render_template_string, request
import uuid
import os
from datetime import datetime

app = Flask(__name__)

# Store embed data by ID (in production, use a database)
embeds = {}

@app.route('/embed/<embed_id>')
def serve_embed(embed_id):
    if embed_id not in embeds:
        return "Embed not found", 404
        
    embed_data = embeds[embed_id]
    
    # HTML template with Open Graph meta tags
    html_template = '''
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    
    <!-- Open Graph meta tags for Discord embeds -->
    <meta property="og:title" content="{{ title }}" />
    <meta property="og:description" content="{{ description }}" />
    <meta property="og:image" content="{{ image_url }}" />
    <meta property="og:url" content="{{ url }}" />
    <meta property="og:type" content="{{ og_type }}" />
    <meta property="og:site_name" content="{{ site_name }}" />
    
    <!-- Twitter Card meta tags (for better compatibility) -->
    <meta name="twitter:card" content="summary_large_image" />
    <meta name="twitter:title" content="{{ title }}" />
    <meta name="twitter:description" content="{{ description }}" />
    <meta name="twitter:image" content="{{ image_url }}" />
    
    <!-- Theme color for Discord -->
    <meta name="theme-color" content="{{ color }}" />
    
    <title>{{ title }}</title>
    
    <style>
        body {
            font-family: 'Whitney', 'Helvetica Neue', Helvetica, Arial, sans-serif;
            background: #36393f;
            margin: 0;
            padding: 20px;
            color: #dcddde;
            min-height: 100vh;
        }
        .embed-container {
            max-width: 520px;
            margin: 0 auto;
            background: #2f3136;
            border-left: 4px solid #5865f2;
            border-radius: 4px;
            padding: 16px;
            box-shadow: 0 2px 10px rgba(0, 0, 0, 0.2);
        }
        .embed-author {
            display: flex;
            align-items: center;
            margin-bottom: 8px;
        }
        .embed-author-icon {
            width: 24px;
            height: 24px;
            border-radius: 50%;
            margin-right: 8px;
        }
        .embed-author-name {
            font-size: 14px;
            font-weight: 600;
            color: #ffffff;
        }
        .embed-title {
            font-size: 16px;
            font-weight: 600;
            color: #00aff4;
            margin-bottom: 8px;
            line-height: 1.375;
        }
        .embed-description {
            font-size: 14px;
            line-height: 1.375;
            color: #dcddde;
            margin-bottom: 16px;
            white-space: pre-line;
        }
        .embed-field {
            margin-bottom: 8px;
        }
        .embed-field-name {
            font-size: 14px;
            font-weight: 600;
            color: #ffffff;
            margin-bottom: 2px;
        }
        .embed-field-value {
            font-size: 14px;
            color: #dcddde;
            line-height: 1.375;
        }
        .embed-thumbnail {
            float: right;
            width: 40px;
            height: 40px;
            border-radius: 6px;
            object-fit: cover;
            margin-left: 12px;
            margin-top: -4px;
        }
        .embed-footer {
            font-size: 12px;
            color: #72767d;
            margin-top: 8px;
            padding-top: 8px;
            border-top: 1px solid #40444b;
        }
    </style>
</head>
<body>
    <div class="embed-container">
        <img class="embed-thumbnail" src="{{ image_url }}" alt="Thumbnail">
        <div class="embed-title">{{ title }}</div>
        
        <div class="embed-description">{{ description }}</div>
    </div>
</body>
</html>
    '''
    
    return render_template_string(html_template, **embed_data)
    
@app.route('/')
def index():
    return f'''
    <div style="font-family: Arial, sans-serif; max-width: 800px; margin: 50px auto; padding: 20px; background: #f5f5f5; border-radius: 10px;">
        <h1>🎭 Cryzen Custom Discord Embeds</h1>
        <p>This server creates custom Discord embeds using Open Graph meta tags.</p>
        <p><strong>Active embeds:</strong> {len(embeds)}</p>
        <p><strong>Status:</strong> Server is running! ✅</p>
        
        <h2>📚 API Documentation</h2>
        <div style="background: white; padding: 15px; border-radius: 5px; margin: 10px 0;">
            <h3>POST /create</h3>
            <p>Create a new Discord embed</p>
            <pre style="background: #f0f0f0; padding: 10px; border-radius: 3px;">{{
  "title": "Your Embed Title",
  "description": "Your embed description",
  "image_url": "https://example.com/image.png",
  "color": "#0099ff",
  "og_type": "website",
  "site_name": "Your Site Name"
}}</pre>
        </div>
        
        <div style="background: white; padding: 15px; border-radius: 5px; margin: 10px 0;">
            <h3>GET /list</h3>
            <p>List all active embeds</p>
        </div>
        
        <div style="background: white; padding: 15px; border-radius: 5px; margin: 10px 0;">
            <h3>GET /health</h3>
            <p>Health check endpoint</p>
        </div>
        
        <p style="margin-top: 30px; color: #666;">
            <strong>🚀 Powered by Cryzen Self-Bot</strong><br>
            Advanced Discord embed control system
        </p>
    </div>
    '''

@app.route('/create', methods=['POST'])
def create_embed():
    """API endpoint to create a new embed"""
    try:
        data = request.get_json()
        if not data:
            return {"error": "No JSON data provided"}, 400
            
        title = data.get('title', 'Cryzen Embed')
        description = data.get('description', 'Custom Discord embed')
        image_url = data.get('image_url', 'https://i.imgur.com/1XvNqw8.png')
        color = data.get('color', '#0099ff')
        og_type = data.get('og_type', 'website')
        site_name = data.get('site_name', 'Cryzen')
        
        # Generate unique ID
        embed_id = str(uuid.uuid4())[:8]
        
        # Get the base URL from the request
        base_url = request.host_url.rstrip('/')
        
        embed_data = {
            'title': title,
            'description': description,
            'image_url': image_url,
            'url': f'{base_url}/embed/{embed_id}',
            'color': color,
            'og_type': og_type,
            'site_name': site_name,
            'timestamp': datetime.now().strftime('%Y-%m-%d %H:%M:%S')
        }
        
        embeds[embed_id] = embed_data
        
        return {
            'success': True,
            'embed_id': embed_id,
            'url': f'{base_url}/embed/{embed_id}',
            'message': f'Embed created successfully'
        }
        
    except Exception as e:
        return {"error": str(e)}, 500

@app.route('/list')
def list_embeds():
    """List all active embeds"""
    embed_list = []
    for embed_id, data in embeds.items():
        embed_list.append({
            'id': embed_id,
            'title': data['title'],
            'url': data['url'],
            'created': data['timestamp']
        })
    return {'embeds': embed_list, 'count': len(embed_list)}

# Health check endpoint
@app.route('/health')
def health_check():
    return {'status': 'healthy', 'service': 'Cryzen Discord Embed Server'}

if __name__ == '__main__':
    # For local development
    port = int(os.environ.get('PORT', 5000))
    app.run(host='0.0.0.0', port=port, debug=False)