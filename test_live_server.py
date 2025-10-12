import requests
import json

def test_live_server():
    base_url = "https://cryzen-discord-embeds.onrender.com"
    
    print(f"🧪 Testing live server at {base_url}")
    print("=" * 50)
    
    # Test creating an embed
    embed_data = {
        "title": "🎭 Cryzen Test Embed",
        "description": "This is a test embed from your live Discord embed server! 🚀",
        "image_url": "https://i.imgur.com/1XvNqw8.png",
        "color": "#7289da",
        "site_name": "Cryzen Live Server"
    }
    
    try:
        response = requests.post(
            f"{base_url}/create",
            headers={"Content-Type": "application/json"},
            data=json.dumps(embed_data)
        )
        
        if response.status_code == 200:
            result = response.json()
            print("✅ Live embed created successfully!")
            print(f"📋 Embed ID: {result['embed_id']}")
            print(f"🔗 Embed URL: {result['url']}")
            print(f"\n🎯 DISCORD READY URL:")
            print(f"   {result['url']}")
            print(f"\n💡 You can now use this URL in Discord messages!")
            print(f"   Just paste: {result['url']}")
            return result['url']
        else:
            print(f"❌ Failed: {response.status_code}")
            print(f"Response: {response.text}")
            return None
            
    except Exception as e:
        print(f"❌ Error: {e}")
        return None

if __name__ == "__main__":
    test_live_server()