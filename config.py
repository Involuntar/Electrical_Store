from pydantic_settings import BaseSettings, SettingsConfigDict


class Settings(BaseSettings):
    DB_NAME:str='default' #Название поля из .env, через двоеточие - тип поля, через знак равно - значение по умолчанию
    DB_HOST:str='localhost'
    DB_PORT:str='3306'
    DB_USER:str='root'
    DB_PASSWORD:str='password'
    TOKEN_SECRET:str='token'
    model_config=SettingsConfigDict(env_file='.env')

settings = Settings()