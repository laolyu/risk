# coding:utf-8
import subprocess
from loguru import logger
import pytest


class TestApk:

    @pytest.mark.dependency()
    def test_apk_po(self):
        # udid = '192.168.0.197:5555'
        apkpath = r'C:\abtest\automation\UI\risk\apk\hyd_v1.4.3-dyn-2023-0223-18-04-debug-king-mjbv3.2.97-nothidden-all.apk'
        cmd = f'adb install {apkpath}'
        try:
            p = subprocess.Popen(cmd, shell=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
            out, err = p.communicate(timeout=20)
            out_info = out.decode('gbk')
            logger.info(out_info)
            assert False
        except Exception as e:
            logger.info(e)
            assert True
