#!/usr/bin/env python3
"""
Test script for Cryzen Discord Embed Server
Run this to test the server locally before deployment
"""

import requests
import json
import time

def test_server(base_url="http://localhost:5000"):
    """Test all endpoints of the embed server"""
    
    print(f"🧪 Testing Cryzen Embed Server at {base_url}")
    print("=" * 50)
    
    # Test 1: Health check
    print("\n1. Testing health check endpoint...")
    try:
        response = requests.get(f"{base_url}/health")
        if response.status_code == 200:
            print("✅ Health check passed!")
            print(f"   Response: {response.json()}")
        else:
            print(f"❌ Health check failed: {response.status_code}")
            return False
    except Exception as e:
        print(f"❌ Health check error: {e}")
        return False
    
    # Test 2: Homepage
    print("\n2. Testing homepage...")
    try:
        response = requests.get(base_url)
        if response.status_code == 200:
            print("✅ Homepage loaded successfully!")
        else:
            print(f"❌ Homepage failed: {response.status_code}")
            return False
    except Exception as e:
        print(f"❌ Homepage error: {e}")
        return False
    
    # Test 3: Create embed
    print("\n3. Testing embed creation...")
    embed_data = {
        "title": "Test Embed",
        "description": "This is a test embed created by the test script!",
        "image_url": "https://i.imgur.com/1XvNqw8.png",
        "color": "#ff6b6b",
        "site_name": "Cryzen Test"
    }
    
    try:
        response = requests.post(
            f"{base_url}/create",
            headers={"Content-Type": "application/json"},
            data=json.dumps(embed_data)
        )
        
        if response.status_code == 200:
            result = response.json()
            print("✅ Embed created successfully!")
            print(f"   Embed ID: {result['embed_id']}")
            print(f"   Embed URL: {result['url']}")
            embed_url = result['url']
            embed_id = result['embed_id']
        else:
            print(f"❌ Embed creation failed: {response.status_code}")
            print(f"   Response: {response.text}")
            return False
    except Exception as e:
        print(f"❌ Embed creation error: {e}")
        return False
    
    # Test 4: View embed
    print("\n4. Testing embed viewing...")
    try:
        response = requests.get(embed_url)
        if response.status_code == 200:
            print("✅ Embed page loaded successfully!")
            if "Test Embed" in response.text and "og:title" in response.text:
                print("✅ Open Graph meta tags found!")
            else:
                print("⚠️  Open Graph meta tags might be missing")
        else:
            print(f"❌ Embed viewing failed: {response.status_code}")
            return False
    except Exception as e:
        print(f"❌ Embed viewing error: {e}")
        return False
    
    # Test 5: List embeds
    print("\n5. Testing embed listing...")
    try:
        response = requests.get(f"{base_url}/list")
        if response.status_code == 200:
            result = response.json()
            print("✅ Embed listing successful!")
            print(f"   Total embeds: {result['count']}")
            if result['count'] > 0:
                print(f"   Latest embed: {result['embeds'][0]['title']}")
        else:
            print(f"❌ Embed listing failed: {response.status_code}")
            return False
    except Exception as e:
        print(f"❌ Embed listing error: {e}")
        return False
    
    print("\n" + "=" * 50)
    print("🎉 All tests passed! Server is ready for deployment.")
    print(f"\n📋 Summary:")
    print(f"   • Server URL: {base_url}")
    print(f"   • Test embed created: {embed_url}")
    print(f"   • Ready for Discord embed usage!")
    
    return True

if __name__ == "__main__":
    print("Waiting 2 seconds for server to start...")
    time.sleep(2)
    
    # Test the server
    if test_server():
        print("\n✅ Server test completed successfully!")
    else:
        print("\n❌ Server test failed!")
        exit(1)