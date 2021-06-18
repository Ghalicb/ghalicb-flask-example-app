import os

class Config:
    SECRET_KEY = os.getenv("SECRET_KEY", "this-is-the-default-key")

class ProductionConfig(Config):
    pass

class StagingConfig(Config):
    pass

class DevelopmentConfig(Config):
    pass