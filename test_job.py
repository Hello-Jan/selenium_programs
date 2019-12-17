import unittest
from job import Job


class TestJob(unittest.TestCase):
    def setUp(self):
        self.job=Job()

    def tearDown(self):
        self.job.driver.quit()

    def test_job(self):
        self.job.test('测试工程师')
        self.assertIn('测试工程师',self.job.driver.page_source)

    def test_city_job(self):
        self.job.test('测试工程师','北京')
        self.assertIn('北京企业最新招聘信息',self.job.driver.title)
        self.assertIn('测试工程师',self.job.driver.page_source)


if __name__ == '__main__':
    unittest.main()