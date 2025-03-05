import pytest
import logging
from features.steps.login_steps import *
from pytest_bdd import scenario

# 配置日志
logger = logging.getLogger(__name__)

# 加载所有场景



@pytest.mark.smoke
@scenario('../features/login.feature','成功登录')
def test_successful_login():
    logger.info("开始执行登录成功测试")
    logger.debug("测试场景：成功登录")
    try:
        # 测试逻辑
        pass
    except Exception as e:
        logger.error(f"测试失败: {str(e)}")
        raise
    finally:
        logger.info("登录测试执行完成")

@pytest.mark.low
@scenario('../features/login.feature','失败登录')
def test_failed_login():
    logger.info("开始执行登录失败测试")
    logger.debug("测试场景：失败登录")
    try:
        # 测试逻辑
        pass
    except Exception as e:
        logger.error(f"测试失败: {str(e)}")
        raise
    finally:
        logger.info("登录测试执行完成")