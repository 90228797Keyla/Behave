from driver_interactions.ElementsInteractions import ElementsInteractions
from driver_interactions.InitWebDriver import InitWebDriver
import utilities.Logger as log
import time

log = log.func_logger()

def before_all(context):
    log.info("Script iniciado")

def before_scenario(context, scenario):
    context.web_driver = InitWebDriver().init_web_driver()
    context.interactions_object = ElementsInteractions(context.web_driver)
    context.interactions_object.launch_web_page("https://www.saucedemo.com")

def after_scenario(context, scenario):
    context.web_driver.quit()

def after_all(context):
    time.sleep(15)
    context.web_driver.quit()


"""def before_feature(context):

def before_scenario(context):
    
def before_step(context):"""

