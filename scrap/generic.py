

class ScraperInit:
    
    chanel = connection.channel()
    driver = Remote(
        command_executor='http://chrome:4444/wd/hub',
        options=options,
        desired_capabilities=DesiredCapabilities.CHROME
        )