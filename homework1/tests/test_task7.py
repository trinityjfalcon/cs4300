import os
import pytest
from unittest.mock import patch, Mock
import task7

# test API call and image download
@patch("task7.requests.get")
def test_dog_image(mock_get, tmp_path):
    # mock JSON response
    mock_api_response = Mock()
    mock_api_response.status_code = 200
    mock_api_response.json.return_value = {
        "message": "https://images.dog.ceo/breeds/husky/test.jpg",
        "status": "success"
    }

    # mock image content resonse
    mock_image_response = Mock()
    mock_image_response.content = b"fakeimagedata"

    mock_get.side_effect = [mock_api_response, mock_image_response]

    # temporary file path
    file_path = tmp_path / "dog.jpg"

    #call func
    task7.get_dog(save_path=file_path)

    #verify file was created
    assert os.path.exists(file_path)

    # verify file contains expected data
    with open(file_path, "rb") as f:
        content = f.read()

    assert content == b"fakeimagedata"

# test failed API response
@patch("task7.requests.get")
def test_get_dog_fail(mock_get):
    mock_response = Mock()
    mock_response.status_code = 404

    mock_get.return_value = mock_response

    result = task7.get_dog("test.jpg")

    assert result is None