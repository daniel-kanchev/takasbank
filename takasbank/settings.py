BOT_NAME = 'takasbank'
SPIDER_MODULES = ['takasbank.spiders']
NEWSPIDER_MODULE = 'takasbank.spiders'
LOG_LEVEL = 'WARNING'
ROBOTSTXT_OBEY = True
ITEM_PIPELINES = {
   'takasbank.pipelines.DatabasePipeline': 300,
}
