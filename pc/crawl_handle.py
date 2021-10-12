import traceback


class Crawl_handel:
    """
    爬取handle类，串联整个爬取和写入excel的过程
    """

    def crawl_wb_and_write_excel(self, crawler):
        """
        主方法：加载浏览器驱动、登录，爬取微博网页版中的数据，整理并存入指定excel
        :param crawler:
        :return:
        """

        try:
            # 1 加载驱动
            driver = self.create_driven(15)

            # 2 加载首页面，并进行登录
            cookies = self.login(driver)

            # 3 不断爬取所有微博内容数据，具体处理逻辑有crawler方法自己实现

            # 4 关闭驱动
            crawler.quiet_driver()

            # 5 爬取所有数据后，写入excel文档
            crawler.write_excel()

        except Exception:
            print("程序运行错误")
            traceback.print_exc()
