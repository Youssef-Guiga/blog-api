class Config:
    SECRET_KEY = 'ccc923e4dfe6b4d02f1de4730511ba9126fe0c16504fdc043f8dda72dc256514'
    SQLALCHEMY_DATABASE_URI = 'sqlite:///site.db'
    JWT_SECRET_KEY = 'a504dd520136fa252d230df31477184e532fb16957712ba1c5f51f9b58e6a227'
    SWAGGER = {
        'title': 'My API',
        'uiversion': 3
    }
