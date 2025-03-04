import pytest
import logging
from features.steps.login_steps import *
from pytest_bdd import scenario

# 配置日志
logger = logging.getLogger(__name__)

@pytest.mark.smoke
@scenario('../features/login.feature', '成功登录')
def test_successful_login():
    """
    这里可以添加额外的测试逻辑,比如:
    - 添加详细的日志记录
    - 截图保存
    - 额外的断言检查
    - 测试数据清理等
    """
    logger.info("开始执行登录测试")
    logger.debug("测试场景：成功登录")
    try:
        # 测试逻辑
        pass
    except Exception as e:
        logger.error(f"测试失败: {str(e)}")
        raise
    finally:
        logger.info("登录测试执行完成")
