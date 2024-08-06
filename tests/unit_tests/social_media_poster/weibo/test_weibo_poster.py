import pytest
import os

from autobyteus_community_tools.social_media_poster.weibo.weibo_poster import WeiboPoster

@pytest.mark.asyncio
async def test_weibo_poster_text_only():
    weibo_poster = WeiboPoster(weibo_account_name="RyanZhengHaliluya")
    
    # Test posting only text
    movie_title = "The Matrix"
    content = "A groundbreaking sci-fi action film."
    result = await weibo_poster.execute(movie_title=movie_title, content=content)

@pytest.mark.asyncio
async def test_weibo_poster_text_with_image():
    weibo_poster = WeiboPoster(weibo_account_name="RyanZhengHaliluya")
    
    # Test posting text with an image
    movie_title = "Inception"
    content_with_image = "This is a test post with an image from an automated integration test. Please ignore."
    image_path = "/home/ryan-ai/Downloads/weibo.jpeg"  # Replace with an actual image path on your system
    
    if not os.path.exists(image_path):
        pytest.skip(f"Test image not found at {image_path}. Skipping image upload test.")
    
    result_with_image = await weibo_poster.execute(movie_title=movie_title, content=content_with_image, image_path=image_path)

@pytest.mark.asyncio
async def test_weibo_poster_error_handling():
    weibo_poster = WeiboPoster()

    # Test with missing movie_title
    with pytest.raises(ValueError, match="The 'movie_title' keyword argument must be specified."):
        await weibo_poster.execute(content="Test post")

    # Test with missing content
    with pytest.raises(ValueError, match="The 'content' keyword argument must be specified."):
        await weibo_poster.execute(movie_title="Test Movie")

    # Test with invalid image path
    with pytest.raises(ValueError, match="The 'image_path' must be a full path."):
        await weibo_poster.execute(movie_title="Test Movie", content="Test post", image_path="relative/path/to/image.jpg")

    # Test with non-existent image file
    with pytest.raises(ValueError, match="The image file does not exist at the specified path:"):
        await weibo_poster.execute(movie_title="Test Movie", content="Test post", image_path="/non/existent/path/to/image.jpg")