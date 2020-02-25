import unittest

from VG_GetRepo import get_repo_info

class TestGetRepo(unittest.TestCase):
    def test_normal_response(self):
        expected = ['User: viren567',
                    'Repo: 810test Number of commits: 3',
                    'Repo: 567test Number of commits: 2',
                    'Repo: Triangle567 Number of commits: 1']
        self.assertEqual(get_repo_info(), expected)

    def test_bad_user_name(self):
        self.assertEqual(get_repo_info('qqqwwweee'), 'can not fetch repos from user')
        self.assertEqual(get_repo_info(''), 'can not fetch repos from user')


if __name__ == '__main__':
    unittest.main()
