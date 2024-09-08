import unittest
from unittest.mock import patch
import requests

from totara.backup import Backup


class TestBackupLibrary(unittest.TestCase):
    @patch('totara.backup.requests.get')
    def test_get_status_success(self, mock_get):
        mock_response = mock_get.return_value
        mock_response.status_code = 200
        mock_response.json.return_value = {'status': 'ok'}

        backup = Backup("https://api.example.com")
        result = backup.status(backup_id="test_backup")

        self.assertEqual(result, {'status': 'ok'})
        mock_get.assert_called_once_with("https://api.example.com/backup/status/test_backup")

    @patch('totara.backup.requests.get')
    def test_get_status_failure(self, mock_get):
        # Mock a failed response (non-200 status code)
        mock_response = mock_get.return_value
        mock_response.status_code = 500
        mock_response.raise_for_status.side_effect = requests.exceptions.HTTPError

        backup = Backup("https://api.example.com")

        with self.assertRaises(requests.exceptions.HTTPError):
            backup.status(backup_id="test_backup")

        mock_get.assert_called_once_with("https://api.example.com/backup/status/test_backup")


if __name__ == '__main__':
    unittest.main()
